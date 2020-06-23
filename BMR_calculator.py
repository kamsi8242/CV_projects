

def BMR():
    import string

    # Conversions
    lbs_to_kg = 0.453592
    ft_to_cm = 30.48
    inch_to_cm = 2.54
    weight_calories_m = 13.397

    # numbers and floats
    numbers = string.digits
    numbers_no_zero = numbers.lstrip("0")
    floats = string.digits + "."

    # error counter:
    error_counter = 0
    age_counter = 0

    # The Age component
    while 1 > 0:
        Age = input("Enter your age: ")
        age_counter = 0
        for i in Age:
            if i not in numbers_no_zero:
                age_counter += 1

        if age_counter == 0:
            break
        
        else:
            print("Please enter your age")

    Age = int(Age)

    while 1 > 0:
        gender = input("Please enter your gender (M/F): ").upper()
        if gender == "M" or gender == "F":
            break

        else:
            print("Enter M for male or F for female")
    
    # The weight component
    while 1 > 0:
        Weight = input("Select a weight measurement unit? \n1. kg \n2. lbs \n")
        if Weight == "1" or Weight == "2":
            break

        else:
            M_BMR()

    if Weight == 2:
        while 1 > 0:
            lbs = input("Enter your weight in lbs: ")
            error_counter = 0
            for i in lbs:
                if i not in floats:
                    error_counter += 1

            if error_counter == 0:
                break

        weight_kg = float(lbs) * lbs_to_kg
        # print("you are {0} kg".format(weight_kg))
                    
    else:
        while 1 > 0:
            weight_kg = input("Enter your weight in kg: ")
            error_counter = 0
            for i in weight_kg:
                if i not in floats:
                    error_counter += 1
            
            if error_counter == 0:
                break
        
        weight_kg = float(weight_kg)
    
    # The height component
    while 1 > 0:
        Height = input("Select either of the following options: \n1. cm  \n2.ft and inchs \n")
        if Height == "1" or Height == "2":
            break

        else:
            print("Enter 1 to put height in terms of cm.\n Enter 2 to put height in terms of Foot and Inches")

    if Height == "2":
        while 1>0:
            error_counter = 0
            ft = input("Enter height in ft: ")
            for i in ft:
                if i not in numbers:
                    error_counter += 1
                    print(error_counter)
            inches = input("Enter height in inches: ")
            for i in inches:
                if i not in numbers:
                    error_counter += 1

            if error_counter == 0 :
                break
            
            
        ft_2_cm = float(ft) * ft_to_cm
        inch_2_cm = float(inches) * inch_to_cm
        height = ft_2_cm + inch_2_cm
        print("you are {0} cm".format(height))    

    
    else:
        while 1 > 0:
            height = input("Enter height in cm: ")
            for i in height:
                if i in numbers or i in floats:
                    break

                else:
                    print("Invalid characters were entered, please enter again")

    # Male BRM
    if gender == "M":
        def M_BMR():
            #Weight component
            weight_component = weight_calories_m  * weight_kg
            print("The weight component of is: {0}".format(round(weight_component)))

            height_calories_m = 4.799
            height_component = height_calories_m * float(height)
            #print("The height component is: {0}".format(height_component))

            #Age component
            age_calories_m = 5.677
            age_compnent = age_calories_m * float(Age)
            #print(age_compnent)

            male_BMR = 88.362 + float(weight_component) + float(height_component) - float(age_compnent)
            male_BMR = round(male_BMR, 2)
            print("Your Basal metabolic rate is: {0} calories per day".format(male_BMR))

        M_BMR()

    # Female BMR
    if gender == "F":
        def F_BMR():
            # Weight component            
            weight_calories_f = 9.247
            weight_component =  weight_calories_f * weight_kg
            print("The weight component of is: {0}".format(weight_component))

            # The height component
            height_calories_f = 3.098
            height_component = height_calories_f * float(height)
            print("The height component is: {0}".format(height_component))

            # Age component
            age_calories_f = 4.330
            age_compnent = age_calories_f * float(Age)
            print("The age component is: {0}".format(age_compnent))

            female_BMR = 447.593 + float(weight_component) + float(height_component) - float(age_compnent)
            print("Your Basal metabolic rate is: {0} Calories per day".format(female_BMR))

        F_BMR()

if __name__ == "__main__":

    BMR()