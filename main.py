import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
from datetime import timedelta, date


def userInfo():
    myemail = "emailaddress" #Please update this with your email address
    mypassword = "mypassword" #Please update this with your password 

    email = driver.find_element("xpath", '//input[@id="mat-input-1"]') #Xpath for email field
    email.send_keys(myemail) 

    passwrd = driver.find_element("xpath", '//input[@id="mat-input-2"]') #Xpath for Password field
    passwrd.send_keys(mypassword)

    time.sleep(2)
    login()

def login():
    try:
        loginButton = driver.find_element("xpath", '//*[@class="mat-focus-indicator ng-tns-c190-4 mat-flat-button mat-button-base mat-primary"]') #Xpath for Login button
        driver.execute_script("arguments[0].click();", loginButton)
        print('Successfull login')
    except:
        print('unable to log in')

    time.sleep(5)
    bookingPage()

def bookingPage():
    try:
        newBooking = driver.find_element("xpath",'//*[@routerlink="/workouts"]')  ##Xpath for navigating to booking page
        driver.execute_script("arguments[0].click();", newBooking)
        #print("On booking bookingPage")  #Un-comment if script doesnt work

    except:
        print('unable to go to booking page')
        driver.quit()
        driver.close()
  
    time.sleep(10)
    #chooseDay()
    selectTime() # update once chooseday works
 
def selectTime():
    try:
        bookTimeSlots = driver.find_element("xpath", '//*[contains(text(), "8:00 - 8:30 PM")]') #update time of your choice
        driver.execute_script("arguments[0].click();", bookTimeSlots)
        #print("onconfirmation page") 
    except:
        driver.quit()
        driver.close()

    time.sleep(5)
    confirmBooking()

# only working for current date
######################## working till here ######################################################
def chooseDay():
    try:
        bookingDate = date.today() + + timedelta(days=2)
        #print(dateToday)
        #formatted_date = dateToday.strftime("%A %B %d")
        #formatted_Bdate = 27
        formatted_Bdate = bookingDate.strftime("%d")
        print(formatted_Bdate)  

        #-------------------------------------------  
        xyz = driver.find_element("xpath",'//*[.="27"]') # update with variable later
        #print("test")
        print(xyz)


        #driver.execute_script("arguments[0].click();", xyz) # this line is not working and requires some work
        #driver.execute_script("arguments[0].click();", xyz)
        #print("working new booking, p[lease select time now]")

    except:
        print('unable to select day')
        #driver.quit()
        #driver.close()


    #time.sleep(5)
    #selectTime()

# --------------------------------------updated but can only be checked after choose date sorts out--------------------#   

def confirmBooking():
    try:
        bookyesButton = driver.find_element_by_xpath("xpath", '//*[contains(text(), "Confirm Booking")]') #xpath selected. Run for after few days while checking
        driver.execute_script("arguments[0].click();", bookyesButton)
    except:
        driver.quit()
        driver.close()


if __name__ == '__main__':
    # Load chrome
    driver = webdriver.Chrome()
    driver.get("https://myaltea.club/")

    time.sleep(2)

    userInfo()
    driver.quit()
    driver.close()
