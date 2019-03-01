def CalculatePower(prm_input , prm_power):
    if(prm_power == 1):
        return(prm_input)
    if(prm_power != 1):
        return(prm_input * CalculatePower(prm_input, prm_power - 1))
        
user_input = int(input("Enter the number: "))
power = int(input("Enter the power value: "))
print("Result:",CalculatePower(user_input , power))