if __name__ == '__main__':
    # Make a program that has some sentence (a string) on input and
    # returns a dict containing all unique words as keys and the number of occurrences as values.
    SPECIAL_CHAR = r'@,_,!,$,%,^,&,*,(,),<,>,?,/,\,|,},{,~,:,;,.,[,]'.strip(',')

    sentence = input('Say something -_-')
    editing_list = sentence.split()
    d = {}


    def version_1():
        iterating_list = [w.strip(SPECIAL_CHAR) for w in sentence.split()]
        final_dict = dict((i, iterating_list.count(i)) for i in set(iterating_list))
        return final_dict


    def version_2():
        for i in editing_list:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    # вариант от народа для народа

    # Create a function which takes as input two dicts with structure mentioned above,
    # then computes and returns the total price of stock.
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }


    def price_calc():
        for amount in stock:
            stock[amount] *= prices[amount]
        return stock


    # Use a list comprehension to make a list containing tuples (i, j)
    # where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

    my_tuple_1 = tuple(i for i in range(11))
    my_tuple_2 = tuple(i ** 2 for i in range(11))
    my_list = [my_tuple_1, my_tuple_2]
    print(my_list)
