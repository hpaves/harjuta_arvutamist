#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
from random import randint

calculation_count = 0
calculation_count_max = 20
correct_answers = 0
clean_array = [1,2,3,4,5,6,7,8,9,10]
multiplication_array = clean_array.copy()
division_array = clean_array.copy()

def invalid_symbol_message():
    print("Siestasid valesti. Proovi veelkord.")


def ask_for_method():
    while True:
        method = input("Korrutad, jagad, või teed mõlemat? (sisesta k, j \
või m): ")
        if method.lower() not in ('k', 'j', 'm'):
            invalid_symbol_message()
        else:
            return method

def ask_for_factor():
    while True: # Stackoverflow: https://bit.ly/2HEdD7k
        try:
            # Quora: https://bit.ly/2Tdrsed
            fixed_factor_input = list(map(int, input("\nSisesta numbrid \
millega arvutada tahad (eralda komaga): ").split(",")))
        except ValueError:
            invalid_symbol_message()
            continue
        return fixed_factor_input

def give_random_fixed_factor():
    random_index = randint(0,len(fixed_factor_array) - 1)
    randomly_selected_number = fixed_factor_array[random_index]
    return randomly_selected_number

def give_non_repeat_random_number(array):
    if len(array) == 0:
        array = clean_array.copy()
    random_index = randint(0,len(array) - 1)
    randomly_selected_number = array.pop(random_index)
    return randomly_selected_number

def make_multiplication():
    global calculation_count
    global correct_answers
    fixed_factor = give_random_fixed_factor()
    random_factor = give_non_repeat_random_number(multiplication_array)
    correct_result = fixed_factor*random_factor
    calculation_count += 1

    coin = randint(2,3)
    if coin % 2 == 0:
        multiplication_display_string = str(fixed_factor) + " * " \
        + str(random_factor) + " = "
    else:
        multiplication_display_string = str(random_factor) + " * " \
        + str(fixed_factor) + " = "

    while True:
        try:
            given_result = int(input(multiplication_display_string))
        except ValueError:
            invalid_symbol_message()
            continue

        if given_result == correct_result:
            print("Tubli! Õige vastus!")
            correct_answers += 1
            return
        else:
            print("Kahjuks vastasid valesti. Õige vastus oli " \
            + str(correct_result))
            return

def make_division():
    global calculation_count
    global correct_answers
    fixed_factor = give_random_fixed_factor()
    random_factor = give_non_repeat_random_number(division_array)
    divisible = fixed_factor*random_factor
    division_display_string = str(divisible) + " : " +  str(fixed_factor) \
    + " = "
    calculation_count += 1

    while True:
        try:
            given_result = int(input(division_display_string))
        except ValueError:
            invalid_symbol_message()
            continue

        if given_result == random_factor:
            print("Tubli! Õige vastus!")
            correct_answers += 1
            return
        else:
            print("Kahjuks vastasid valesti. Õige vastus oli " \
            + str(random_factor))
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
    print("\nTegid õigesti " + str(correct_answers) + " ülesannet, hindele " \
    + str(grade) + "\n")

# Windows compatibility section!!!
# Necessary when using double click to run the script in Windows
# Else the terminal will close immediately after \
# the exercises are done and you won't see the grade
# You can comment this out if you run the script straight from a *nix terminal
    while True:
        exitcode = input("Sisesta j, et väljuda: ")
        if exitcode.lower() not in ('j'):
            invalid_symbol_message()
        else:
            break

if __name__ == "__main__":
    print("\nProgramm annab sulle 20 ülesannet ja seejärel hindab tulemusi.\n")
    method = ask_for_method()
    fixed_factor_array = ask_for_factor()

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
