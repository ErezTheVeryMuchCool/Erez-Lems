# import TeamGenerator, JudgingSession
from colorama import Fore
import random
import json

passwords = "Passwords.txt"
jobs = 6
def password_generator(amount):
    with open(passwords, 'w') as file:
        for i in range(amount):
            password = str(random.randint(100000, 999999))
            file.write(password + "\n")

def get_password(number):
    with open (passwords, "r") as file:
        gyatt = file.readlines()
        return gyatt[number - 1].strip()
password_generator(6)

joblist = {
    "Room Judge" : get_password(1),
    "Feild Judge": get_password(2),
    "John Meshulam(Master)": get_password(3),
    "Caller" : get_password(4),
    "Rizzler" : get_password(5),
    "Bortholomrew" : get_password(6)
}
joblistlist = list(joblist.keys())

print("Hello volunteer and welcome to the erez-lems. a better alternative for john-lems.")

print(Fore.CYAN + "\nplease enter your job number. choose either:")
for i in range(jobs):
    print(f"{i+1}. " + joblistlist[i])
job = int(input(" "))

if job > jobs or job < 1:
    print("Thats not a real job mate! try again.")
