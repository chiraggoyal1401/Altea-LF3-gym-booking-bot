import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
from datetime import timedelta, date


def userInfo():
    myemail = "youremailaddress" #update with your email address
    mypassword = "yourpassword" #update with your password

    email = driver.find_element("xpath", '//input[@id="mat-input-1"]') #update xpath according to your gym
    email.send_keys(myemail)

    passwrd = driver.find_element("xpath", '//input[@id="mat-input-2"]') #update xpath according to your gym
    passwrd.send_keys(mypassword)

    time.sleep(2)
    login()

def login():
    try:
        loginButton = driver.find_element("xpath", '//*[@class="mat-focus-indicator ng-tns-c190-4 mat-flat-button mat-button-base mat-primary"]') #update xpath according to your gym
        driver.execute_script("arguments[0].click();", loginButton)
        print('Successfull login')
    except:
        print('unable to log in')

    time.sleep(5)
    bookingPage()

def bookingPage():
    try:
        newBooking = driver.find_element("xpath",'//*[@routerlink="/workouts"]') #update xpath according to your gym
        driver.execute_script("arguments[0].click();", newBooking)
        print("On booking bookingPage")

    except:
        print('unable to go to booking page')
        driver.quit()
        driver.close()
  
    time.sleep(10)
    chooseDay() 
 
def chooseDay():   
    try:
        dateToday = date.today() + timedelta(days=2) #update time delta according to your wish
        print(date.today())
        formattedDate = dateToday.strftime("%d")
        print(formattedDate)
        #print(type(formattedDate))
        bookyesButton = driver.find_element("xpath", f'//p[contains(text(), "{formattedDate}")]') #update xpath according to your gym. this is take date in advance to book
        driver.execute_script("arguments[0].click();", bookyesButton)
        print("day selected fine")
    except:
        print("issue in choose day")
        driver.quit()
        driver.close()

    time.sleep(5)
    selectTime()

def selectTime():
    try:
        bookTimeSlots = driver.find_element("xpath", '//*[contains(text(), "8:30 - 9:15 AM")]') # update time of your choice and xpath according to your gym
        driver.execute_script("arguments[0].click();", bookTimeSlots)
        print("Time selected and now navigating to confirmation page")
    except:
        print("issue in select time")
        driver.quit()
        driver.close()

    time.sleep(15)
    confirmBooking()

def confirmBooking():
    try:
        bookyesButton = driver.find_element("xpath", '//*[contains(text(), "Confirm Booking")]') #xpath selected. Run for after few days while checking
        driver.execute_script("arguments[0].click();", bookyesButton) # uncomment after date issue
        print("booking confirmed")
    except:
        print("booking not confirmed")

        driver.quit()
        driver.close()


if __name__ == '__main__':
    # Load chrome
    driver = webdriver.Chrome()
    driver.get("https://myaltea.club/") #name of your gym

    time.sleep(2)

    userInfo()
    driver.quit()
    driver.close()
