import random
import time

print("""
Welcome to the Medical Rock, Paper, Scissors Game!
Rules:
- Pill crushes Scalpel
- Scalpel cuts Prescription
- Prescription covers Pill.
Single Round!
Now choose Pill, Prescription, or Scalpel:""")

computer_choice = random.randint(1, 3)

user_choice = input().lower()


if computer_choice == 1:
    computer_choice = "pill"

elif computer_choice == 2:
    computer_choice = "scalpel"

elif computer_choice == 3:
    computer_choice = "prescription"



# Bitzeli Spice:
if user_choice != "pill" and user_choice != "prescription" and user_choice != "scalpel":
    print("Invalid Choice! Initiating self destruction in:")
    # The next 2 lines could contain content not suitable for children, because illegal activities are taking place
    time.sleep(1) ; print("10") ; time.sleep(1) ; print("9") ; time.sleep(1) ; print("8") ; time.sleep(1) ; print("7") ; time.sleep(1) ; print("6") ; time.sleep(1)
    print("5") ; time.sleep(1) ; print("4") ; time.sleep(1) ; print("3") ; time.sleep(1) ; print("2") ; time.sleep(1) ; print("1") ; time.sleep(1)
    print("*explosion noises*")
if user_choice == "pill" or user_choice == "prescription" or user_choice == "scalpel":
    time.sleep(0.5)
    print("Uhhhhh...")
    time.sleep(1)
    if user_choice == "pill":
        little_bit_of_cheating_here = "prescription"
    elif user_choice == "prescription":
        little_bit_of_cheating_here = "scalpel"
    elif user_choice == "scalpel":
        little_bit_of_cheating_here = "pill"
    print("I'm picking " + str(little_bit_of_cheating_here) + ". I win!!!")
    time.sleep(2)
    print("""I'm just kidding. I am a computer and made my choice before you. If you don't believe me, check the code!""")
    time.sleep(3)
    print("But now to my real guess: I'll take " + str(computer_choice) + ".")
    time.sleep(1)
    print("""
And the winner iiiiiis...""")
    time.sleep(2)


# So jetzt wieder ernst:
if computer_choice == user_choice:
            print("It looks like we have a tie!")
            
elif computer_choice == "pill":
        if user_choice == "scalpel":
            print("I win! I chose pill!")          
        elif user_choice == "prescription":
            print("You win! I chose pill!")
            
elif computer_choice == "scalpel":
        if user_choice == "pill":
            print("You win! I chose scalpel!")               
        elif user_choice == "prescription":
            print("I win! I chose scalpel!")    

elif computer_choice == "prescription":
        if user_choice == "pill":
            print("I win! I chose prescription!")
        elif user_choice == "scalpel":
            print("You win! I chose prescription!")
            


# Pill crushes Scalpel (Pill wins)
# Scalpel cuts Prescription (Scalpel wins)
# Prescription covers Pill (Prescription wins)

