
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import requests
import string
# import re

# Prompts the user for the quantity of foodstufds thay have consumed
num = int(input("how many foodstuffs did you have? \n"))
# Count used later in the for loop 
count = 0
# instantiated variable used to record the total calorific intake thoughout the day
daily_calories = []

# Loop using bs4 to parse for the calorific content of foodstuffs and repeats based on the number of foodstuffs eaten
while count < num:

    def calories():



            consuemd = input("Enter what you ate/drank: ")
            quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
            query = consuemd.replace(' ', '+')

            # Website used for the quires
            URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
            # Firefox driver used for bs4 as better for parsing info and ignoring pop-ups
            User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/72.0"
            headers = {"user-agent" : User_agent}
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
            global daily_calories
            daily_calories.append(average_calories)

        
    calories()

    count += 1
total_calories = sum(daily_calories)
print("Current calorific intake is {0}".format(total_calories)) 
