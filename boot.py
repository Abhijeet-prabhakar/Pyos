import os

class Main:

    def Boot():    

        boot_check = open('Startup/boot_check')
        boot_check_data = boot_check.read()

        start_file = "Startup/start.pys"

        if boot_check_data == "True":
            os.startfile('login.py')
            quit()
        else:
            os.startfile("startup.py")
            quit()

    if __name__ == "__main__":
        Boot()
    