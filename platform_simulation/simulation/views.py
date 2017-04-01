#Other packages
import os

#Django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import F, ExpressionWrapper, DecimalField

#App imports
from simulation.models import Simulator
from simulation.forms import SimulationForm


#Our views

#Index page view
def index(request):
    if request.method == 'POST':
    	#load form data
        form = SimulationForm(request.POST)

        #check form data
        if form.is_valid(): 
            brand_factor = form.cleaned_data['brand_factor']
            #start the simulation
            return HttpResponseRedirect(reverse('results', kwargs = {'brand_factor':brand_factor})) 
    else:
    	#display empty form if not a POST request
        form = SimulationForm()

    return render(request, 'simulation/index.html', {'form':form})


#Count the number of Agent for each breed
def countBreeds():
	#Breed C
    c_count = Simulator.objects.filter(breed = "Breed_C").count() 
    #Breed NC
    nc_count = Simulator.objects.filter(breed = "Breed_NC").count() 
    
    return {'c_count':c_count, 'nc_count':nc_count}


#move the CSV to our dataBase
def importCSV():
	#current directory
    pwd = os.path.dirname(__file__) 
    #array where imported objects are stored
    agents = [] 
    #open the CSV file
    with open(pwd + '/file/AgentTest.csv') as f: 
        for line in f:
            line = line.split(',')
            #create an empty Simulator object
            agent = Simulator() 

            #fill the object with values from CSV
            agent.breed = line[0]
            agent.policy_id = line[1]
            agent.age = line[2]
            agent.social_grade = line[3]
            agent.payment = line[4]
            agent.attribute_brand = line[5]
            agent.attribute_price = line[6]
            agent.attribute_promotions = line[7]

            #AutoRenew Test (0 or 1)
            if line[8] == '1':
                agent.auto_renew = True
            else:
                agent.auto_renew = False

            agent.inertia = line[9]
            agent.initial_breed = line[0]
            
            #add the object to the array
            agents.append(agent) 

    #insert the array into the database
    Simulator.objects.bulk_create(agents) 


#Inialize DataBase from CSV and return descriptive statistics
def initialiseDatabase():
	#delete results of the previous simulation
    Simulator.objects.all().delete() 
    #populate the db with values from CSV
    importCSV() 
    #number of breeds before the simulation
    return countBreeds() 


#Launch the simulation and return the result 
#Based on the model inside the xslx file
def runSimulation(brand_factor):
	#converting from string to decimal
    brand_factor = float(brand_factor) 

    #run for 15 years
    for year in range(0, 15): 
    	#increment age of all agents
        Simulator.objects.all().update(age = F("age") + 1) 

        #select agents with auto_renew = false
        query = Simulator.objects.filter(auto_renew = False) 
        #calculate affinity for selected agents
        query = query.annotate(affinity = ExpressionWrapper(F("payment")/F("attribute_price") + (2 * F("attribute_promotions") * F("inertia")), output_field = DecimalField())) 
        #agents of breed C with affinity < (social_grade * attribute_brand)
        C = query.filter(breed = 'Breed_C', affinity__lt = (F("social_grade") * F("attribute_brand")))
        #agents of breed NC with affinity < (social_grade * attribute_brand * brand_factor)
        NC = query.filter(breed = 'Breed_NC', affinity__lt = (F("social_grade") * F("attribute_brand") * brand_factor)) 

        #swap breeds
        C.update(breed = "temp", c_lost = True) 
        NC.update(breed = "Breed_C")
        Simulator.objects.filter(breed = "temp").update(breed = "Breed_NC")

    #breed stats
    breedStats = countBreeds() 
    #number of NC -> C
    c_lost = Simulator.objects.filter(breed = "Breed_NC", initial_breed = "Breed_C").count() 
    #number of C -> NC
    c_gained = Simulator.objects.filter(breed = "Breed_C", initial_breed = "Breed_NC").count() 
    #number of C -> NC -> C
    c_regained = Simulator.objects.filter(breed = "Breed_C", initial_breed = "Breed_C", c_lost = True).count()

    return {'c_count': breedStats['c_count'], 'nc_count': breedStats['nc_count'], 'c_lost':c_lost, 'c_gained':c_gained, 'c_regained':c_regained}

#Run simulation and display results
def results(request, brand_factor):
	#initialise db, get stats before the simulation
    pre_analyse = initialiseDatabase() 
    #run simulation, get stats after the simulation
    post_analyse = runSimulation(brand_factor) 
    return render(request, 'simulation/simulation.html', {'brand_factor':brand_factor, 'pre_analyse':pre_analyse, 'post_analyse':post_analyse})


