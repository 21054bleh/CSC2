# main funcion
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'

        elif response == 'no' or response == 'n':
            return 'no'
        
        else:
            print("Please enter yes or no")

# main routine goes here
want_instructions=''
while want_instructions != 'yes' and want_instructions != 'no':
    want_instructions = yes_no('Do you want to read the instructions? ')


if want_instructions == 'yes':
    print('Instructions go here')

print('Program continues')
print()
