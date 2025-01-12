def bmi(the_weight,the_height):
	the_BMI = the_weight / (the_height/100)**2  
	print(the_BMI)
	return the_BMI
if __name__ == '__main__':
	bmi()