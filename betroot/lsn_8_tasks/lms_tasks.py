if __name__ == '__main__':
    # Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
    # The function should then print “My favorite movie is named {name}”.
    def favourite_movie():
        your_movie = input('Enter your favourite movie :D')
        print(f'My favourite movie is named {your_movie}')


    # Create a function called make_country, which takes in a country’s name and capital as parameters.
    # Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
    # Make the function print out the values of the dictionary to make sure that it works as intended.

    def make_country(name, capital, dictionary=None):
        if dictionary == None:
            dictionary = {}
        dictionary[name] = capital
        return dictionary


    dict_misc = input('Name of country , name of capital').split()
    print(make_country(dict_misc[0], dict_misc[1]))


    # Вопрос есть , как сделать чтобы юзер мог еще и название выбрать для словаря 0_о

    # Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
    # (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
    # and an arbitrary number of arguments (only numbers) as the second parameter.
    # Then return the sum or product of all the numbers in the arbitrary parameter

    def make_operation(operator, *args):
        rez = 0
        if operator == '+':
            rez = sum(args)
            return rez
        elif operator == '-':
            for i in args:
                rez -= i
                return rez
        elif operator == '*':
            rez += 1
            for i in args:
                rez *= i
                return rez
        else:
            return 'Wrong format of operator'


    print(make_operation('+', 1, 3, 4, 2, 32))
