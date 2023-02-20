print("--------------------------------------------------->>>>Welcome to Libaray Management Systens<<<<-----------------------------------\n")

import datetime 
print("""Date :- """,datetime.datetime.now()
     ,"""\n@author:-""","""Ansh Srivastav \n""" ) 
import pyautogui
import random
import time
import sys
    
class digital_library:
     def __init__(self):
           self.d = {}
           self.OTP = []
           self.login_Person = {}
           self.Sign_person = {}
                
     def signin(self,Name,Mobile_number,Email_id,Password):
          if Mobile_number not in self.Sign_person.values():
               self.Sign_person[Name]=Mobile_number
               self.Sign_person[Email_id]=Password
               print( "Now Enter OTP")
               return ""
          else:
               return "User Already exist :}"
     
     def get_otp(self):
          i = 1
          while i > 0:
               time.sleep(10)
               tem = pyautogui.typewrite(str(random.randint(1000,9999)))
               pyautogui.press("Enter")
               self.OTP.append(tem)
               break
     
     def enterd_otp(self,OTP):
          x = "".join(self.OTP)
          print("Singing Successfull")
          print("Your Email and Password is Your Login ID and Password\n")
          return ""
     

     def login(self,Email_ID,Password):
          if Email_ID not in self.Sign_person:
               print("You Are not our existing Coustomer \n You have to Sigin First")
               return ""
          elif Email_ID in self.Sign_person:
               self.login_Person[Email_ID]= Password
               print("Login Sucessfully")
               return ""
          else:
               print("Already Login",end="")
               return ""
     
     def show_password(self):
          print("User Info:-",self.login_Person)


class libarary(digital_library):
     def show_Book(self):
          print("="*101)
          print("Welcome to Digital Library")
          print("="*101)
          Books = ["C++","Think Python","Think Stats","Onject Oriented Programing"]
          print("Hello ")
          print()
          print("We Have Currently these 👇 Books\n")
          for i in Books:
               print("--->>>",i)
          print("\nAvailable Right Now")


user = digital_library()
user.signin("Yash",8882334551,'yash@gmail','yash@2003')

("-"*140)
User_Name = input("Enter Your User_name Here:")
Password = input("Enter Your Password Here :")
user1 = libarary()
user1.login(User_Name,Password)
user1.show_Book()
print()
print("-"*140)

while True:
     print("*"*60,"\n")
     print("Press 1 for c++")
     print("Press 2 for Think Python")
     print("Press 3 for Think Stats")
     print("Press 4 for Object Oriented Programing\n")
     print("*"*60,"\n")
     button = int(input("Please Select a Button :-"))
     if button == 1:
          webbrowser.open("https://github.com/Anshsrivastavastava/Assignment/blob/main/Learning%20C%2B%2B.pdf")
     
     elif button ==2:
          webbrowser.open("https://github.com/Anshsrivastavastava/Digital-Library-Project/blob/main/Think%20python.pdf")
     
     elif button ==3:
          webbrowser.open("https://github.com/Anshsrivastavastava/Digital-Library-Project/blob/main/Thinks%20stats.pdf")
     
     elif button==4:
          webbrowser.open("https://archive.org/details/ost-computer-science-ooprogramming/page/n23/mode/2up?view=theater")
     
     else:
          print("Please Enter a Valid Button")
          sys.exit()

