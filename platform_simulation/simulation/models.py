from django.db import models

#In this section we designed our model for the DataBase
#To do so, a little overview of the CSV file is needed.

#For header we have 10 values, 9 quantitative and 1 qualitative:
	#Agent_Breed --> Qualitative value
	#Policy_ID
	#Age
	#Social_Grade
	#Payment_at_Purchase
	#Attribute_Brand
	#Attribute_Price
	#Attribute_Promotions
	#Auto_Renew
	#Inertia_for_Switch

#This class is abstract it makes easier the expansion
class Agent(models.Model):

	BREEDS = (
		('Breed_C', 'Breed C'),
		('Breed_NC', 'Breed NC'),
		('temp', 'temp_values')
		)

	breed = models.CharField(max_length = 8, choices = BREEDS, verbose_name = "breed")
	policy_id = models.CharField(max_length = 150, verbose_name = "policy id")
	age = models.IntegerField(verbose_name = "age")
	social_grade = models.IntegerField(verbose_name = "social grade")
	payment = models.IntegerField(verbose_name = "paymenent at purchase")
	attribute_brand = models.DecimalField(decimal_places = 1, max_digits = 5, verbose_name = "attribute brand")
	attribute_price = models.DecimalField(decimal_places = 1, max_digits = 5, verbose_name = "attribute price")
	attribute_promotions = models.DecimalField(decimal_places = 1, max_digits = 5, verbose_name = "attribute promotions")
	auto_renew = models.BooleanField(verbose_name = "auto renew")
	inertia = models.IntegerField(verbose_name = "inertia for switch")

	class Meta: 
		abstract = True

#Inherit from the class above
class Simulator(Agent): 
   
	BREEDS = (
		('Breed_C', 'Breed C'),
		('Breed_NC', 'Breed NC'),
		)

    #new attributes useful for this simulation
    #keeping track of the initial breed
	initial_breed = models.CharField(max_length = 8, choices = BREEDS, verbose_name = "initial breed")
	#useful for finding regained breed C
	c_lost = models.BooleanField(verbose_name = "breed c lost", default = False) 
	