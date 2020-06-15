
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from calories import calories
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import requests
import string
# from height_Convetror import height_convertor
#from wieght_conversion import lbs_2_kg



# Firefox driver used for bs4 as better for parsing info and ignoring pop-ups
User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/72.0"
headers = {"user-agent" : User_agent}
daily_calories = []


def Calorie_tracker():
    print("Hello and welcome to my calorie counting app. This assumes that you Live in the United Kingdom, but will be updated to include other countries in the future.")

    print("Factors that this app takes into account: Gender, Height, weight, Age, Diet.")
    print("Factors that this app does not take into account: Health, Genetics, Environmental factors, Drugs.")
    print("The calorie values of the food are taken from the nutracheck.co.uk website.")
    print("The Harris-Benedict Equation was used to determine Basal Metabolic rate.")
    
    # Breakfast
    while sum(daily_calories) == 0:
        Breakfast = input("Did you have Breakfast in the morning (Y/N)? \n").upper()
        if Breakfast == "Y" or Breakfast == "N":
            # print("Congrats")
            break
        else:
            print("Invlaid input, please neter Y for yes or N for no")

    if Breakfast == "Y":
        while Breakfast == "Y":
            b_num = input("How many foodstuffs did you have for Breakfast? \nThis must be expressed as an integer: ")
            b_failcount = 0
            for i in b_num:
                if i not in string.digits:
                    b_failcount += 1

            if b_failcount == 0:
                break
                    
            else:
                print("Invalid input, please answer the question with a numerical integer that is greater than 0.")
        
        b_num = int(b_num)
        b_count = 0
        b_cals = []
        
        
        while b_count < b_num:
    
            def b_calories():

                consuemd = input("Enter the #{0} item you ate/drank: ".format(int(b_count + 1)))
                quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
                query = consuemd.replace(' ', '+')

                # Website used for the quires
                URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
                resp = requests.get(URL, headers=headers)
                soup = BeautifulSoup(resp.content, 'html.parser')

                # Identifier that the code should parse all text from the webpage contained within the specified class 
                text = soup.find_all('a', class_='textNoDecoration')
                # Instantiated list to hold the parsed results
                list = []

                # loops through all details contained within the parsed text
                for details in text:
                    calorie_content = details.text

                    # String characters used later with the strip command to limit parsed text to calorific values
                    letters = str(string.ascii_letters)
                    characters = str(string.punctuation)
                    numbers = str(string.digits)
                    spaces = " "
                    newline = "\n "
                    combination = letters + characters + numbers + spaces
                    nutritional_details = calorie_content.lstrip(combination)
                    nutritional_details = nutritional_details.lstrip(newline)
                    nutritional_details2 = nutritional_details.rstrip(letters + numbers + ". ")
                    just_calories = nutritional_details2.rstrip(spaces + characters + letters)
                    
                    list.append(int(just_calories))

                average_calories = quantity * sum(list)/len(list)
                
                print("On average there are {0} calories contianed within a {2} portions of {1}.".format(average_calories, consuemd, quantity))
                # global b_cals
                
                b_cals.append(average_calories)
                
            b_calories()
            b_count += 1

        breakfast_cals = sum(b_cals)
        daily_calories.append(breakfast_cals)
        print("Breakfast calorific intake is {0} calories".format(breakfast_cals)) 
    
    # Brunch
    else:
        while sum(daily_calories) == 0:
            Brunch = input("Did you have Brunch instead of Breakfast (Y/N)? \n").upper()
            if Brunch == "Y" or Brunch == "N":
                break
            else:
                print("Invalid input, enter Y for yes or N for no")

        if Brunch == "Y":
            while Brunch == "Y":
                br_num = input("How many foodstuffs did you have for Brunch? \nThis must be expressed as an integer: ")
                br_failcount = 0
                for i in br_num:
                    if i not in string.digits:
                        br_failcount += 1

                if br_failcount == 0:
                    break
                        
                else:
                    print("Invalid input, please answer the question with a numerical integer that is greater than 0.")

            br_num = int(br_num)
            br_count = 0
            br_cals = []
            
            while br_count < br_num:

                def brunch_calories():

                    consuemd = input("Enter the #{0} item you ate/drank: ".format(int(br_count + 1)))
                    quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
                    query = consuemd.replace(' ', '+')
                    # Website used for the quires
                    URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
                    resp = requests.get(URL, headers=headers)
                    soup = BeautifulSoup(resp.content, 'html.parser')
                    # Identifier that the code should parse all text from the webpage contained within the specified class 
                    text = soup.find_all('a', class_='textNoDecoration')
                    
                    # Instantiated list to hold the parsed results
                    list = []

                    # loops through all details contained within the parsed text
                    for details in text:
                        calorie_content = details.text

                        # String characters used later with the strip command to limit parsed text to calorific values
                        letters = str(string.ascii_letters)
                        characters = str(string.punctuation)
                        numbers = str(string.digits)
                        spaces = " "
                        newline = "\n "
                        combination = letters + characters + numbers + spaces
                        nutritional_details = calorie_content.lstrip(combination)
                        nutritional_details = nutritional_details.lstrip(newline)
                        nutritional_details2 = nutritional_details.rstrip(letters + numbers + ". ")
                        just_calories = nutritional_details2.rstrip(spaces + characters + letters)
                        
                        list.append(int(just_calories))

                    average_calories = quantity * sum(list)/len(list)
                    
                    print("On average there are {0} calories contianed within a {2} portions of {1}.".format(average_calories, consuemd, quantity))
                    
                    br_cals.append(average_calories)
                    
                brunch_calories()
                br_count += 1       

            brunch_cals = sum(br_cals)
            daily_calories.append(brunch_cals)
            print("Brunch calorific intake is {0} calories".format(brunch_cals))    

    # Lunch
    if Breakfast == "Y" or Breakfast and Brunch == "N":
        while True:
            Lunch = input("Did you have lunch (Y/N)? \n").upper()
            if Lunch == "Y" or Lunch == "N":
                break
            else:
                print("Invalid input, please enter Y for yes or N for no")

        if Lunch == "Y":
            while Lunch == "Y":
                l_num = input("How many foodstuffs did you have for Lunch? \nThis must be expressed as an integer: ")
                l_failcount = 0
                for i in l_num:
                    if i not in string.digits:
                        l_failcount += 1

                if l_failcount == 0:
                    break
                    
                else:
                    print("Invalid input, please answer the question with a numerical integer that is greater than 0.")

            l_num = int(l_num)
            l_count = 0
            l_cals = []
            
            while l_count < l_num:

                def lunch_calories():

                    consuemd = input("Enter the #{0} item you ate/drank: ".format(int(l_count + 1)))
                    quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
                    query = consuemd.replace(' ', '+')
                    # Website used for the quires
                    URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
                    resp = requests.get(URL, headers=headers)
                    soup = BeautifulSoup(resp.content, 'html.parser')
                    # Identifier that the code should parse all text from the webpage contained within the specified class 
                    text = soup.find_all('a', class_='textNoDecoration')
                    
                    # Instantiated list to hold the parsed results
                    list = []

                    # loops through all details contained within the parsed text
                    for details in text:
                        calorie_content = details.text

                        # String characters used later with the strip command to limit parsed text to calorific values
                        letters = str(string.ascii_letters)
                        characters = str(string.punctuation)
                        numbers = str(string.digits)
                        spaces = " "
                        newline = "\n "
                        combination = letters + characters + numbers + spaces
                        nutritional_details = calorie_content.lstrip(combination)
                        nutritional_details = nutritional_details.lstrip(newline)
                        nutritional_details2 = nutritional_details.rstrip(letters + numbers + ". ")
                        just_calories = nutritional_details2.rstrip(spaces + characters + letters)
                        
                        list.append(int(just_calories))

                    average_calories = quantity * sum(list)/len(list)
                    
                    print("On average there are {0} calories contianed within a {2} portions of {1}.".format(average_calories, consuemd, quantity))
                    
                    l_cals.append(average_calories)
                    
                lunch_calories()
                l_count += 1       

            lunch_cals = sum(l_cals)
            daily_calories.append(lunch_cals)
            print("Lunch calorific intake is {0} calories".format(lunch_cals)) 

    while sum(daily_calories) == True:
        Afternoon_Snacks = input("Have you eaten any snacks today (Y/N) \n").upper()
        if Afternoon_Snacks == "Y" or Afternoon_Snacks == "N":
            break
        else:
            print("Invlaid input, Please enter Y for yess or N for no")

    if Afternoon_Snacks == "Y":
        while Afternoon_Snacks == "Y":
            as_num = input("How many snacks have you had? \nThis must be expressed as an integer: ")
            as_failcount = 0
            for i in as_num:
                if i not in string.digits:
                    as_failcount += 1

            if as_failcount == 0:
                break
                    
            else:
                print("Invalid input, please answer the question with a numerical integer that is greater than 0.")

        as_num = int(as_num)
        as_count = 0
        as_cals = []
            
        while as_count < as_num:

            def as_calories():

                consuemd = input("Enter the #{0} item you ate/drank: ".format(int(as_count + 1)))
                quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
                query = consuemd.replace(' ', '+')
                # Website used for the quires
                URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
                resp = requests.get(URL, headers=headers)
                soup = BeautifulSoup(resp.content, 'html.parser')
                # Identifier that the code should parse all text from the webpage contained within the specified class 
                text = soup.find_all('a', class_='textNoDecoration')
                
                # Instantiated list to hold the parsed results
                list = []

                # loops through all details contained within the parsed text
                for details in text:
                    calorie_content = details.text

                    # String characters used later with the strip command to limit parsed text to calorific values
                    letters = str(string.ascii_letters)
                    characters = str(string.punctuation)
                    numbers = str(string.digits)
                    spaces = " "
                    newline = "\n "
                    combination = letters + characters + numbers + spaces
                    nutritional_details = calorie_content.lstrip(combination)
                    nutritional_details = nutritional_details.lstrip(newline)
                    nutritional_details2 = nutritional_details.rstrip(letters + numbers + ". ")
                    just_calories = nutritional_details2.rstrip(spaces + characters + letters)
                    
                    list.append(int(just_calories))

                average_calories = quantity * sum(list)/len(list)
                
                print("On average there are {0} calories contianed within a {2} portions of {1}.".format(average_calories, consuemd, quantity))
                
                as_cals.append(average_calories)
                
            as_calories()
            as_count += 1       

        AS_cals = sum(as_cals)
        daily_calories.append(as_cals)
        print("Snack calorific intake is {0} calories".format(AS_cals))

    while sum(daily_calories) == True:
        Dinner = input("Did you eat dinner today (Y/N) \n").upper()
        if Dinner == "Y" or Dinner == "N":
            break
        else:
            print("Invlaid input, please neter Y for yes or N for no")

    if Dinner == "Y":
        while Dinner == "Y":
            d_num = input("How many foodstuffs did you have for Dinner? \nThis must be expressed as an integer: ")
            d_failcount = 0
            for i in d_num:
                if i not in string.digits:
                    d_failcount += 1

            if d_failcount == 0:
                break
                    
            else:
                print("Invalid input, please answer the question with a numerical integer that is greater than 0.")
        
        d_num = int(d_num)
        d_count = 0
        d_cals = []
            
        while d_count < d_num:

            def d_calories():

                consuemd = input("Enter the #{0} item you ate/drank: ".format(int(d_count + 1)))
                quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
                query = consuemd.replace(' ', '+')
                # Website used for the quires
                URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
                resp = requests.get(URL, headers=headers)
                soup = BeautifulSoup(resp.content, 'html.parser')
                # Identifier that the code should parse all text from the webpage contained within the specified class 
                text = soup.find_all('a', class_='textNoDecoration')
                
                # Instantiated list to hold the parsed results
                list = []

                # loops through all details contained within the parsed text
                for details in text:
                    calorie_content = details.text

                    # String characters used later with the strip command to limit parsed text to calorific values
                    letters = str(string.ascii_letters)
                    characters = str(string.punctuation)
                    numbers = str(string.digits)
                    spaces = " "
                    newline = "\n "
                    combination = letters + characters + numbers + spaces
                    nutritional_details = calorie_content.lstrip(combination)
                    nutritional_details = nutritional_details.lstrip(newline)
                    nutritional_details2 = nutritional_details.rstrip(letters + numbers + ". ")
                    just_calories = nutritional_details2.rstrip(spaces + characters + letters)
                    
                    list.append(int(just_calories))

                average_calories = quantity * sum(list)/len(list)
                
                print("On average there are {0} calories contianed within a {2} portions of {1}.".format(average_calories, consuemd, quantity))
                
                d_cals.append(average_calories)
                
            d_calories()
            d_count += 1       

        D_cals = sum(d_cals)
        daily_calories.append(d_cals)
        print("Dinner calorific intake is {0} calories".format(D_cals))
    

    total = sum(daily_calories)
    print("You consumed {0} calories today".format(total))





"""

    # Gender component
    gender = input("What gender are you (M/F): \n").upper()
    if gender == 'M':
        
        # Weight component
        Weight = int(input("Select a weight measurement unit? \n1. kg \n2. lbs \n"))
        if Weight == 2:
            lbs = int(input("Enter your weight in lbs: "))
            weight_kg = float(lbs) * 0.453592
            print("you are {0} kg".format(weight_kg))
                        
        else:
            weight_kg = float(input("Enter your weight in kg: "))
        
        weight_component = 13.397  * weight_kg
        print("The weight component of is: {0}".format(weight_component))

    
        # The height component
        Height = int(input("Select either of the following options: \n1. cm  \n2.ft and inchs \n"))

        if Height == 2:
            ft = int(input("Enter height in ft: "))
            inches = int(input("Enter height in inches: "))
            ft_2_cm = float(ft) * 30.48
            inch_2_cm = float(inches) * 2.54
            height = ft_2_cm + inch_2_cm
            print("you are {0} cm".format(height))    

        
        else:
            height = str(input("Enter height in cm: "))


        height_component = 4.799 * float(height)
        print("The height component is: {0}".format(height_component))

        # Age component
        Age = int(input("Enter your age: "))
        age_compnent = 5.677 * float(Age)
        print(age_compnent)

        male_BMR = 88.362 + float(weight_component) + float(height_component) - float(age_compnent)
        print("Your Basal metabolic rate is: {0}".format(male_BMR))

##########################################################################################################################################

    elif gender == 'F':
         # Weight component
        Weight = int(input("Select a weight measurement unit? \n1. kg \n2. lbs \n"))
        if Weight == 2:
            lbs = int(input("Enter your weight in lbs: "))
            weight_kg = float(lbs) * 0.453592
            print("you are {0} kg".format(weight_kg))
                        
        else:
            weight_kg = float(input("Enter your weight in kg: "))
        
        weight_component = 9.247  * weight_kg
        print("The weight component of is: {0}".format(weight_component))

    
        # The height component
        Height = int(input("Select either of the following options: \n1. cm  \n2.ft and inchs \n"))

        if Height == 2:
            ft = int(input("Enter height in ft: "))
            inches = int(input("Enter height in inches: "))
            ft_2_cm = float(ft) * 30.48
            inch_2_cm = float(inches) * 2.54
            height = ft_2_cm + inch_2_cm
            print("you are {0} cm".format(height))    

        
        else:
            height = str(input("Enter height in cm: "))


        height_component = 3.098 * float(height)
        print("The height component is: {0}".format(height_component))

        # Age component
        Age = int(input("Enter your age: "))
        age_compnent = 4.330 * float(Age)
        print(age_compnent)

        female_BMR = 447.593 + float(weight_component) + float(height_component) - float(age_compnent)
        print("Your Basal metabolic rate is: {0}".format(female_BMR))
"""
Calorie_tracker()
            
