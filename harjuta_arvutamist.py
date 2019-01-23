#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
from random import randint

calculation_count = 0
calculation_count_max = 20
correct_answers = 0

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
            fixed_factor = int(input("\nSisesta number millega arvutada tahad (1-10): "))
        except ValueError:
            print("See polnud number. Proovi veelkord.")
            continue

        if fixed_factor < 1:
            print("Ära nulli ja negatiivseid arve pane.")
            continue
        elif fixed_factor > 10:
            print("Üle 10 võib keeruliseks minna.")
            continue
        else:
            return fixed_factor

def make_multiplication():
    global calculation_count
    global correct_answers
    random_factor = randint(1,10)
    correct_result = fixed_factor*random_factor
    calculation_count += 1

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
                correct_answers += 1
                return
            else:
                print("Kahjuks vastasid valesti. Õige vastus oli " + str(correct_result))
                return

def make_division():
    global calculation_count
    global correct_answers
    random_factor = randint(1,10)
    divisible = fixed_factor*random_factor
    division_display_string = str(divisible) + " : " +  str(fixed_factor) + " = "
    calculation_count += 1

    while True:
        given_result = input(division_display_string)
        if len(given_result) == 0:
            continue
        else:
            given_result = int(given_result)
            if given_result == random_factor:
                print("Tubli! Õige vastus!")
                correct_answers += 1
                return
            else:
                print("Kahjuks vastasid valesti. Õige vastus oli " + str(random_factor))
                return

def grade_the_student():
    percent = correct_answers / calculation_count_max
    if percent >= 0.90:
        grade = 5
    elif percent >= 0.75:
        grade = 4
    elif percent >= 0.50:
        grade = 3
    else:
        grade = 2
    print("\nTegid õigesti " + str(correct_answers) + " ülesannet, hindele " + str(grade) + "\n")

# Windows compatibility section!!!
# Comment this back in when using double click to run the script in Windows
# Else the terminal will close immediately after the exercises are done and you won't see the grade
# Ignore this if you run the script straight from a *nix terminal
    # while True:
    #     exitcode = input("Sisesta j, et väljuda: ")
    #     if exitcode.lower() not in ('j'):
    #         print("Siestasid valesti. Proovi veelkord.")
    #     else:
    #         break


if __name__ == "__main__":
    print("\nProgramm annab sulle 20 ülesannet ja seejärel hindab tulemusi.\n")
    method = ask_for_method()
    fixed_factor = ask_for_factor()

    if method == 'k':
        while calculation_count < calculation_count_max:
            make_multiplication()
    elif method == 'j':
        while calculation_count < calculation_count_max:
            make_division()
    elif method == 'm':
        while calculation_count < calculation_count_max:
            coin = randint(2,3)
            if coin % 2 == 0:
                make_multiplication()
            else:
                make_division()
    else:
        print('Programm läks katki. Palun ütle õpetaja Henrile.')
    grade_the_student()
