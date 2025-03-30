def inputfunction():
    master_data = input("Please input a number from 1 to 100:  ")
    master_data_int = int(user_data)

    if master_data_int < 1 or user_data_int > 100:
        print("the number inserted is out of bounds")
    else: 
        print(f"The number inputed is {master_data_int} and is in the bounds") 
inputfunction()
