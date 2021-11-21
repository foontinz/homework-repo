if __name__ == '__main__':
    # Write a program, which has two print statements to print the following text (capital letters “O” and “H”, made from “#” symbols):
    print("#########\n#\t\t#\n#\t\t#\n#\t\t#\n#########\n")
    print("#\t\t#\n#\t\t#\n#########\n#\t\t#\n#\t\t#")


    #Create a python program named “task2”, and use the built-in function `print` in it several times. Try to pass “sep”, “end” params and pass several parameters separated by commas.
    # LMS
    print('L', 'M', 'S', sep='')
    # 20-11-2021
    print('20', '11', '2021', sep='-')
    # betroot@academy.com
    print('betroot', 'academy.com', sep='@')
    # Python@rolling.thunder
    print("Python", end='@')
    print("rolling.thunder")



    # Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
    # “Good day <name>! <day> is a perfect day to learn some python.”
    name = 'Dima'
    day = 'Saturday'
    print(f'Good day {name}!{day} is a perfect day to learn some python')
    # print('Good day {}!{} is a perfect day to learn some python'.format(name,day))

    # Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
    surname = 'Yurinoff'
    print(surname + ' ' + name)

    # Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
    a = 12
    b = 4
    print(f'{a+b}\n{a-b}\n{a/b}\n{a*b}\n{a**b}\n{a%b}\n{a//b}')

