def GenerateFibonacciSeries(prm_input):  
   if prm_input <= 1:  
       return prm_input
   else:  
       return(GenerateFibonacciSeries(prm_input - 1) + GenerateFibonacciSeries(prm_input - 2))  

# take input from the user  
threshold = int(input("Please mention the threshold value to stop the series."))  

# check if threshold is valid  
if threshold <= 0:  
   print("The Threshold value is invalid, cannot generate the series.")  
else:  
   print("Fibonacci sequence:")  
   for i in range(threshold):  
       print(GenerateFibonacciSeries(i))  