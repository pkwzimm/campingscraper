#!/bin/python3

#this is a selenium-based web scraper to check availability for Steep Ravine campground (Mt Tamalpais St Park).

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #to be able to input data in search fields
from selenium.webdriver.chrome.options import Options #options (for running headless)
from selenium.webdriver.support.ui import Select #to handle dropdowns
import sys #you need this for command line input
#from selenium.common.exceptions import NoSuchElementException
import os #to save things
import pyautogui #not actually sure if you need this
import time #for date stamp on file
import email, smtplib, ssl #for emailing results
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date #for handling input
from datetime import datetime #for handling input
from dateutil.relativedelta import relativedelta

# instantiate a chrome options object so you can set the size and headless preference
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

#browser = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Chromedriver\\chromedriver.exe') #open up your browser (windows version)
#browser = webdriver.Chrome(chrome_options=chrome_options) #open up your browser (Ubuntu version, with headless flags)
browser = webdriver.Chrome() #with visible browser for debugging

#STEEP RAVINE CAMPGROUND (MT TAM)
#browser.get("https://www.reservecalifornia.com/CaliforniaWebHome/Default.aspx") #fetch url
browser.get("https://www.reservecalifornia.com/CaliforniaWebHome/Facilities/SearchViewUnitAvailabity.aspx") #fetch url for CA state parks system website
print("Navigating to URL...")

#find park
#browser.find_element_by_id("txtSearchparkautocomplete").clear();
#park = browser.find_element_by_id('txtSearchparkautocomplete')
browser.find_element_by_id("txtCityParkSearch").clear();
park = browser.find_element_by_id('txtCityParkSearch')
park.send_keys('SAMPLEPARKNAME') #insert whatever search term you want that will get the number of choices down to ONE - i.e. "Mount Tam" will bring up 'Mt Tamalpais SP'
time.sleep(1)
park.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
park.send_keys(Keys.ENTER)
print("Searching for Park")

#Find date field
arrdate = browser.find_element_by_id('mainContent_SearchUnitAvailbity_txtArrivalDate')
arrdate.click()

#calculate max possible date (6 months from today) and enter in field
six_months_old = date.today() + relativedelta(months=6)
six_months = datetime.strptime(str(six_months_old),'%Y-%m-%d')
six_months_new = six_months.strftime('%m/%d/%Y')
#arrdate.send_keys(str(six_months_new))
#arrdate.send_keys(Keys.ENTER)
date_pick = browser.find_element_by_xpath("//div[@class='ranges']/ul/li[3]")
date_pick.click()

#select number of nights (8 is max)
length = Select(browser.find_element_by_id('ddlNightsSearchUnitAvailbity'))
length.select_by_value('8')

#click search button
search_button = browser.find_element_by_link_text('Search')
search_button.click()

browser.implicitly_wait(5)

#find Steep Ravine button
#reserve_button = browser.find_element_by_xpath("//div[contains(@class,'table_data_box') and contains(@class,'table-responsive')]/table/tbody/tr[contains(.,'S Rav Camp Area')]/td[a[contains(@class,'btn_green')]]")
reserve_button = browser.find_element_by_xpath("//tr[contains(.,'NAMEOFCAMPSITE')]/td[a[contains(@class,'btn_green')]]") #You will need to search to find the name of your campsite here.  It will be in the table on the right-hand side of the screen, in the "facilities" column.  Your text search should be EXACT.
reserve_button.click()
print("Fetching availability")

# Find the table rows
tables = browser.find_elements_by_class_name('unitdata')
# Iterate over each row of the table, and save th
for table in tables[:1]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)  #This is set for up to SEVEN campsites.  For larger campgrounds, copy and repeat
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en01 = "Campsite EN01 available on " + str(six_months_new)
    else:
        en01 = ""
    print("EN01: " + row_class)
for table in tables[1:2]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en02 = "Campsite EN02 available on " + str(six_months_new)
    else:
        print("EN02: " + row_class)
        en02 = ""
for table in tables[2:3]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en03 = "Campsite EN03 available on " + str(six_months_new)
    else:
        en03 = ""
    print("EN03: " + row_class)
for table in tables[3:4]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en04 = "Campsite EN04 available on " + str(six_months_new)
    else:
        en04 = ""
    print("EN04: " + row_class)
for table in tables[4:5]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en05 = "Campsite EN05 available on " + str(six_months_new)
    else:
        en05 = ""
    print("EN05: " + row_class)
for table in tables[5:6]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en06 = "Campsite EN06 available on " + str(six_months_new)
    else:
        en06 = ""
    print("EN06: " + row_class)

for table in tables[6:7]:
    # get the text from the second td in each row (first day of availability - td #1 is a label column)
    row = table.find_element_by_xpath(".//td[2]")
    row_class = row.get_attribute("class")
    if "blue_brd_box" in row_class:
        en07 = "Campsite EN07 available on " + str(six_months_new)
    else:
        en07 = ""
    print(row_class)

#email results
#if every en variable is an empty string, then sad trombone
if all(v is "" for v in [en01, en02, en03, en04, en05, en06, en07]):
    print("::sad trombone:: No campsite availability on " + str(six_months_new))
else:
    print("Available site! Emailing results")
if all(c is "" for c in [en01, en02, en03, en04, en05, en06, en07]):
    print("Will check again tomorrow")
else:
    subject = "Awesome campsite available on " + str(six_months_new_day)
    sender_email = "YOURDEV@EXAMPLE.COM" #you need to set up a development email to link to your sever.  The Option 1 section in this article helps explain how - https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
    receiver_email = "YOUREMAIL@EXAMPLE.COM" #Your email

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    #Add all the campsite results into one big body string, separated by spaces
    body = '----- CAMPSITENAME -----\n' + str(en01) + '\n' + str(en02) + '\n' + str(en03) + '\n' + str(en04) + '\n' + str(en05) + '\n' + str(en06)  + '\n' + str(en07)
    message.attach(MIMEText(body,'plain'))

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, "PASSWORD") #yes, I know raw passwords are a bad idea.  This is a throwaway one only used for this purpose.
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

browser.close() #clean up after yourself.
