import platform
import psutil
import subprocess
import socket
from zipfile import *
import os

class Main:

    def Boot():
            boot_check = open('Startup/boot_check', 'w')
            boot_check.write('True')
            boot_check.close

    def Check_Info():
        def Specs():
            #system specs
            try:
                system = platform.uname()
                print("System Specs:")
                print("")
                #cpu
                cpu = system.processor
                print("cpu: ", cpu)
                #battery
                battery = psutil.sensors_battery()
                print("battery: ", battery.percent)
                print("Power Connected:", battery.power_plugged)

                os = open("Startup/Data/OS_Name.txt")
                os_name = os.read()
                print("OS: ",os_name)
            except:
                print("Unable To Find System Specs:(")

        #network
        def Network():
            try:
                devices = subprocess.check_output(['netsh','wlan','show','network'])
                devices = devices.decode('ascii')
                devices = devices.replace("\r","")
                print("")
                print("Wireless Network Available:")
                print(devices)
            except:
                print("Unable To Find Wireless Network:(")

        #ip
        def ip():
            try:
                name = socket.gethostname()
                host_ip = socket.gethostbyname(name)
                print("")
                print("Desktop Name:", name)
                print("Internet Protocol:", host_ip)
            except:
                print("Unable To Get The Host Internet Protocol:")
            

        #running the functions
        Specs()
        ip()
        Network()

    def Startup():
        def Start():
            opp = "[Y/N]: "
            print("Start with the startup?")
            option = input(opp)    

            if option == "Y" or option == "y":
    
                def Name_Pass():

                        def Pass():
                            password = input(str("Enter your password: "))
                            with open("Startup/Data/Users/user_pass.txt", "w") as file:
                                file.writelines(password)
                            print("Do you want your user password to be '"+password+"'") 
                            opp = "[Y/N]"
                            option = input(opp)

                            if option == "Y" or option == "y":
                                print(str("Your User password is " + password))
                                print("Continue with the setup?")
                                conti = input(str("[Y/N]"))

                                if conti == "Y" or conti == "y":
                                    os.startfile("login.py")
                                elif conti == "N" or conti == "n":
                                    Pass()
                                elif conti == "quit" or conti == "Quit":
                                    quit()
                                else:
                                    print("Press 'quit' to quit")

                            elif option == "N" or option == "n":
                                Pass()
                            elif option == "quit" or option == "Quit":
                                quit()
                            else:
                                print(str("Write quit to quit."))
                                Pass()

                        def Name():
                            name = input(str("Enter your username: "))
                            with open("Startup/Data/Users/user_name.txt", "w") as file:
                                file.writelines(name)
                            print("Do you want your user name to be '"+name+"'") 
                            opp = "[Y/N]"
                            option = input(opp)

                            if option == "Y" or option == "y":
                                print(str("Your Username is " + name))
                            elif option == "quit" or option == "Quit":
                                quit()
                            elif option == "N" or option == "n":
                                print(str("Write quit to quit."))
                                Name()
                            else:
                                print(str("Write quit to quit."))
                                Name()

                        def Input_Runner():
                            Name()
                            Pass()


                        #running the function   
                        Input_Runner()
                        # Name()    

                #running the function
                Name_Pass()

            elif option == "N" or option == "n":
                print("")
            
            else:
                print("Please Choose your option " + opp)
                Start()

        # def
        #running the functions
        Start()
        
    if __name__ == "__main__":
        Check_Info()
        Startup()


        #run the function boot at the end so i can make sure that startup is done:)
        Boot()