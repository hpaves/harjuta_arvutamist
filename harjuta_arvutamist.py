import string
from random import randint

def ask_for_method():
    while True:
        method = input("Korrutad, jagad, või teed mõlemat? (sisesta k, j või m): ")
        if method.lower() not in ('k', 'j', 'm'):
            print("Siestasid valesti. Proovi veelkord.")
        else:
            return method

def ask_for_factor():
    while True: # https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659
        try:
            fixed_factor = int(input("Sisesta number millega arvutada tahad (1-10): "))
        except ValueError:
            print("See polnud number. Proovi veelkord.")
            #better try again... Return to the start of the loop
            continue

        if fixed_factor < 1:
            print("Ära nulli ja negatiivseid arve pane.")
            continue
        elif fixed_factor > 10:
            print("Üle 10 võib keeruliseks minna.")
            continue
        else:
            #shift was successfully parsed!
            #we're ready to exit the loop.
            return fixed_factor

def make_multiplication():
    random_factor = randint(1,10)
    correct_result = fixed_factor*random_factor

    coin = randint(2,3)
    if coin % 2 == 0:
        multiplication_display_string = str(fixed_factor) + " * " +  str(random_factor) + " = "
    else:
        multiplication_display_string = str(random_factor) + " * " +  str(fixed_factor) + " = "

    while True:
        given_result = input(multiplication_display_string)
        if len(given_result) == 0:
            continue
        else:
            given_result = int(given_result)
            if given_result == correct_result:
                print("Tubli! Õige vastus!")
                return
            else:
                print("Kahjuks vastasid valesti. Õige vastus oli " + str(correct_result))
                return

def make_division():
    random_factor = randint(1,10)
    divisible = fixed_factor*random_factor
    division_display_string = str(divisible) + " : " +  str(fixed_factor) + " = "

    while True:
        given_result = input(division_display_string)
        if len(given_result) == 0:
            continue
        else:
            given_result = int(given_result)
            if given_result == random_factor:
                print("Tubli! Õige vastus!")
                return
            else:
                print("Kahjuks vastasid valesti. Õige vastus oli " + str(random_factor))
                return

if __name__ == "__main__":
    print("\nProgrammist väljumiseks vajuta CTRL+C\n")
    method = ask_for_method()
    fixed_factor = ask_for_factor()

    if method == 'k':
        while True:
            make_multiplication()
    elif method == 'j':
        while True:
            make_division()
    elif method == 'm':
        while True:
            coin = randint(2,3)
            if coin % 2 == 0:
                make_multiplication()
            else:
                make_division()
    else:
        print('Programm läks katki. Palun ütle õpetaja Henrile.')

