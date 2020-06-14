
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
import requests
import string
# import re

num = int(input("how many foodstuffs did you have? \n"))
count = 0
daily_calories = []
while count < num:

    def calories():



            consuemd = input("Enter what you ate/drank: ")
            quantity = float(input("Enter how many portions of {0} you had: ".format(consuemd)))
            query = consuemd.replace(' ', '+')

            URL = 'https://www.nutracheck.co.uk/CaloriesIn/Product/Search?desc=' + query
            User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/72.0"
            headers = {"user-agent" : User_agent}
            resp = requests.get(URL, headers=headers)
            soup = BeautifulSoup(resp.content, 'html.parser')

            text = soup.find_all('a', class_='textNoDecoration')
            list = []

            for details in text:
                calorie_content = details.text
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
