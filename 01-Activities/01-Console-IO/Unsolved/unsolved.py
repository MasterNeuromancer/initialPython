#!/usr/bin/python3

###############################################################################
#
# BRIEF //
#   Your firm is implementing its student management prototype in Python.
#   It's a command-line program, which the registrar's office will use to
#   add students to the database upon enrollment.
#
#   The program should prompt the user for a student's first name; last name;
#   middle initial; physical address; email address; and phone number.
#
#   After each prompt, the program should wait for the user's input.
#
#   Once the user has entered every piece of information, the program should
#   print it all back to the console, and prompt the user to enter Y if the
#   information is correct, or any other key otherwise.
#
#   For now, you should collect the user's response--i.e., y or otherwise--but
#   don't worry about handling it. We'll get to that shortly.
#
###############################################################################

# What function prints a message to the screen and waits for user input?
# Use it here to collect a student's information--first name, last name, etc.
###############################################################################
# ...Your Code Here...
firstName = input('What is your first name?')

lastName = input('What is your last name?')

address = input('Please enter the your address. ')
email = input('Please enter the your email. ')
phone_number = input('Please enter the your phone_number. ')

# Print a separator. This wasn't part of the assignment, so it's okay if you
# don't have this part. :)
print('-' * 18)


print('Welcome to the new school {0} {1}.'.format(firstName, lastName))
# Once you've gotten all of that, print it all back to the screen.
###############################################################################
# ...Your Code Here...
correctInfo = input('Is the information above correct?')
# Then, use the same function you used to prompt users for information to ask
# them to confirm whether or not the information is correct. Save their
# response, but don't worry about doing anything with it yet!
###############################################################################
# ...Your Code Here...
