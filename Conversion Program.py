print("Program running.....")
x= int(input("type a number in the box ")) #Defines input function 

def conversion (unit): #Declare the functions
    mililiters = unit * 29.57353 # Set the parameters
    return mililiters
 
print(conversion(x)) #substitute 'x' for any number
