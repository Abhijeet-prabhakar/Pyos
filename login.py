import os
from Startup import *

class Main:
    def Login():
        open_name = open("Startup/Data/Users/user_name.txt")
        read_name = open_name.read()

        print("User: "+ read_name)

        def CheckPass():
            open_pass = open("Startup/Data/Users/user_pass.txt")
            read_pass = open_pass.read()
            password = input(":")

            if password == read_pass:
                os.startfile("input_reader.py")
            else:
                print("Wrong Password")
                CheckPass()
        
        CheckPass()

    Login()