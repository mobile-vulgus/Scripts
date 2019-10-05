import time
import os
import sys
import random

# "Loading" effect
def oracle_connect():
    os.system('clear')
    print("Connecting to Oracle.")
    time.sleep(.5)
    os.system('clear')
    print("Connecting to Oracle..")
    time.sleep(.5)
    os.system('clear')
    print("Connecting to Oracle...")
    time.sleep(.5)
    os.system('clear')
    print("Connecting to Oracle....")
    time.sleep(1.5)
    os.system('clear')
    time.sleep(.5)
    print("Connected")
    time.sleep(1)
    os.system('clear')

# Visual letter-by-letter typing effect
def delay_print(s):
    os.system('setterm -cursor off')
    for c in s:    #for character in string
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)
    os.system('setterm -cursor on')

# Realistic randomized-speed typing
typing_speed = 80 #wpm
def slow_type(t):
    os.system('setterm -cursor off')
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')
    os.system('setterm -cursor on')

# 49x6 characters+2 spaces either side=51 wide
def oracle_ascii():
    os.system('clear')
    os.system('setterm -cursor off')
    delay_print("""
  ██████╗ ██████╗  █████╗  ██████╗██╗     ███████╗
 ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║     ██╔════╝
 ██║   ██║██████╔╝███████║██║     ██║     █████╗  
 ██║   ██║██╔══██╗██╔══██║██║     ██║     ██╔══╝  
 ╚██████╔╝██║  ██║██║  ██║╚██████╗███████╗███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
              V E R S I O N    1.4.2              
""")
    slow_type("""
     WHAT WILL YOU DO AT THE END OF THE WORLD?            
""")
    print("\n")
    os.system('setterm -cursor on')

def linebreaker():
    os.system('setterm -cursor off')
    delay_print('-' * 51)
    print('\n')
    os.system('setterm -cursor on')

def prompt():
    os.system('setterm -cursor off')
    slow_type("              Fight, Flee, or Freeze?              \n")
    os.system('setterm -cursor on')

def gas_breath():
    while True:
        amount = input("~ ")
        try:
            val = int(amount)
            if val >= 3:
                break
            else:
                slow_type("\nThe poison is still too thick.\n")
        except ValueError:
            slow_type("\nAmount must be a number, try again\n")
    return val 

# Define input questions/responses
def questions():
    while True:
        prompt()
        linebreaker()
        choice = input("~ ")
        if choice in ['help', 'h', 'q', 'quit', 'exit', 'leave']:
            slow_type("\nIs it really so hard?\n\n~ ")
            linebreaker()
        
        # Fight
        elif choice.lower() in ['fight']:
            slow_type("\nYou hold your ground against apocalypse.\n")
            slow_type("The end comes by the air. A poison cloud unseen.\n")
            slow_type("Do you breathe it in?\n")
            breathe = input("~ ")
            if breathe in ['yes', 'Yes', 'YES', 'Y', 'y']:
                slow_type("\nYou died. It was poison...\n")
                linebreaker()
            else: 
                slow_type("\nHow many minutes can you hold your breath?\n")
                gas_breath()
                linebreaker()
        
        # Flee
        elif choice.lower() in ['flee']:
            slow_type("\nThe sky fades as you hide underground.\n")
            linebreaker()    
        
        # Freeze
        elif choice.lower() in ['freeze']:
            slow_type("\nYou watch the world disintegrate around you.\n")
            linebreaker()

        else:
            slow_type("\nI don't understand.")
            os.system('setterm -cursor off')
            time.sleep(3)
            oracle_ascii()


# Begin Program
os.system('setterm -cursor off')
oracle_connect()
oracle_ascii()
questions()
