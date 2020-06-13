def calories():

    from bs4 import BeautifulSoup
    from selenium import webdriver
    from urllib.request import urlopen
    import requests
    import string
    # import re

    consuemd = input("Enter what you ate/drank: ")
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

    global average_calories
    average_calories = sum(list)/len(list)
    
    print("On average there are {0} calories contianed within a portion/serving of {1}.".format(average_calories, consuemd))

if __name__ == "__main__":
    
    calories()
