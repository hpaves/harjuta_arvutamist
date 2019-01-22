import string
from random import randint

# def ask_for_method():
#     while True:
#         method = input("Korrutad, jagad, või teed mõlemat? (sisesta k, j või m): ")
#         if method.lower() not in ('k', 'j', 'm'):
#             print("Siestasid valesti. Proovi veelkord.")
#         else:
#             return method

# limit = 100

def ask_for_factor():
    while True: # https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659
        try:
            factor = int(input("Sisesta number millega arvutada tahad (1-10): "))
        except ValueError:
            print("See polnud number. Proovi veelkord.")
            #better try again... Return to the start of the loop
            continue

        if factor < 1:
            print("Ära nulli ja negatiivseid arve pane.")
            continue
        elif factor > 10:
            print("Üle 10 võib keeruliseks minna.")
            continue
        else:
            #shift was successfully parsed!
            #we're ready to exit the loop.
            return factor

def make_multiplication():
    randomfactor = randint(1,10)
    correctresult = factor*randomfactor

    multstring1 = str(factor) + " * " +  str(randomfactor) + " = "
    multstring2 = str(randomfactor) + " * " +  str(factor) + " = "
    coin = randint(2,3)
    if coin % 2 == 0:
        multstring = multstring1
    else:
        multstring = multstring2

    while True:
        givenresult = input(multstring)
        if len(givenresult) == 0:
            continue
        else:
            givenresult = int(givenresult)
            if givenresult == correctresult:
                print("Tubli! Õige vastus!")
                return
            else:
                print("Kahjuks vastasid valesti. Õige vastus oli " + str(correctresult))
                return


if __name__ == "__main__":
    factor = ask_for_factor()
    while True:
        make_multiplication()