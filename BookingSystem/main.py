import calendar
import csv

with

name = input("What is your name?: ")
age = input("What is your age?: ")
gender = input("What is your gender?: ")
country = input("Which country do you live in?: ")
city = input("Which city do you live in?: ")
phoneNumber = input("What is your phonenumber?: ")
eMail = input("What is your E-Mail?: ")
Height = input("How tall are you in centimeters?: ")
Weight = input("How much do you weigh in kilograms?: ")
Smoke = input("Do you smoke? If yes, please specify how many cigarettes you approximately smoke per day: ")
Diabetes = input("Do you have any sort/type of diabetes?: ")
Hypertension = input("Do you have Hypertension?: ")
CardiacDiseases = input("Do you have any cardiac diseases?: ")
other = input("Do you have any other conditions?: ")
Operation = input("Which area of your body do you wished to have changed? please specify: ")
OnlineConsultation = input("We can have our online consultation in WhatsApp, Instagram, Skype, Zoom, or Facebook Messenger. In which platform, do you wish to have the consultation? please specify the wished platform and provide me with your account information: ")
Date = input("Please have a look at the calendar, and choose a date + time for the online consultation:")
print("The calendar for the year 2021 is: ")
print(calendar.calendar(2021, 2, 1, 6))

print(f"The name you have entered is {name}")
