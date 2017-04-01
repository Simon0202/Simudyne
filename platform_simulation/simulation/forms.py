from django import forms

#User input
class SimulationForm(forms.Form):
	
	brand_factor = forms.DecimalField(required = True, min_value = 0.1, max_value = 2.9, label = "Enter a factor in range [0.1 , 2.9]")