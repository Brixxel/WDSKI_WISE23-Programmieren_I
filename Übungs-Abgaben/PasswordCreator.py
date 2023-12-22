import string
import random
import os

## @Felix_Regler 
## Version: 1.0
## 29.11.2023

## Exercise_2: Password Generator
## After specifying the length and the underlying character set and the number of passwords, 
## the console program should output such passsords either in the console, as a .txt-file or in the pointer tray

# intialize character_sets
letters = list()                                                # nur Buchstaben (klein)
for i in range(97,123):
    letters.append(chr(i))

all_letters = list()                                            # nur Buchstaben (klein und groß)
for i in range(65,91):
    all_letters.append(chr(i))
all_letters += letters

numbers = list()                                                # nur Zahlen
for i in range(48,58):
    numbers.append(chr(i))

letters_numbers = list()                                        # Buchstaben und Zahlen
letters_numbers = numbers + all_letters

all_charackters = list()                                        # Buchstaben und Sonderzeichen
for i in range(33, 127):
    all_charackters.append(chr(i))


# programm_sequence function
def programm():
    print("A new programm sequence: ")
    print("#########################")
    specs = user_input()
    passwords = create_password(specs)
    output(passwords, specs[3])
    

# user_input function
def user_input():
    inputs: list = []
    incorrect_input = True

    # user input - number of passwords
    temp_input = int(input("Please insert the number of passwords, you want to create: "))
    inputs.append(temp_input)        

    # user input - lenght of passwords
    temp_input = int(input("Please insert the lenght of your passwords, you want to create: "))
    inputs.append(temp_input)
    
    # user input - lenght of passwords
    while incorrect_input:                                        
        temp_input = int(input("Please choose the characterset (letters[1]; all_letters[2]; numbers[3]; letters & numbers [4]; all_characters[5]): "))
        if(temp_input < 6 and temp_input > 0):                           # cheking for correct input
            incorrect_input = False
            inputs.append(temp_input)
    incorrect_input = True

    while incorrect_input:                                        
        temp_input = int(input("Please choose how you want to have your password: (consol Output [1]; as an .txt file [2]; both [3]; clipboard [4]): "))
        if(temp_input < 5 and temp_input > 0):                           # cheking for correct input
            incorrect_input = False
            inputs.append(temp_input)

    return inputs

# create_password function
def create_password(specs: list):
    passwords: list = []
    characters = list()

    if specs[2] == 1:                                                   # das gewünschte Zeichenset sind nur Buchstaben
        characters = letters
    elif specs[2] == 2:                                                 # das gewünschte Zeichenset sind alle Buchstaben
        characters = all_letters
    elif specs[2] == 3:                                                 # das gewünschte Zeichenset sind alle Zahlen
        characters = numbers
    elif specs[2] == 4:                                                 # das gewünschte Zeichenset sind alle Buchstaben und Zahlen
        characters = letters_numbers
    else:                                                               # das gewünschte Zeichenset sind alle Zeichen
        characters = all_charackters

    for i in range(0, specs[0]):                                        # durch die Anzahl an gewünschten Passwörtern itterieren
        temp_password: string = ""
        for j in range(0, specs[1]):                                    # über die länge der gewünschten Passwörter itterieren
            temp_password += random.choice(characters)                  # den aus dem ausgewählten zeichenset zufällig gewählte Buchstaben dem Passaort hinzufügen
        passwords.append(temp_password)                                 # das neue Passwort der Liste an Passwörtern hinzufügen

    return passwords


# output function
def output(passwords: list, type: int):
    if type == 1:
        print("your passwords: ", passwords)                            # Gibt PAssswörter in der Konsole aus
    elif type == 2:
        with open("passwords.txt", "w") as output:                      # speichert das passwort extrem sicher in eine txt Datei
            output.write(str(passwords))
    elif type == 3:
        with open("passwords.txt", "w") as output:                      # speichert das passwort extrem sicher in eine txt Datei
            output.write(str(passwords))
        print("your passwords: ", passwords)                            # Gibt PAssswörter in der Konsole aus
    elif type == 4:
        command = 'echo ' + str(passwords).strip() + '| clip'           # speichert dei Passwörter in die Zwischenablage
        os.system(command)

# #######################
# start programm_sequence
programm()
