
def bmr(gender, age, weight, height):
   bmr = 0 # Initialize the bmr 
   if gender == 'M' or gender == 'm':
      # Figure out and print the BMR
      bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)

   if gender == 'F' or gender == 'f':
      # Figure out and print the BMR
      bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

   print ('Your BMR is: ', bmr)
   return bmr


if __name__ == '__main__':
	bmr()