import re

if __name__ == '__main__':
    # Make a program that has some sentence (a string) on input and
    # returns a dict containing all unique words as keys and the number of occurrences as values.
    SPECIAL_CHAR = '@,_,!,$,%,^,&,*,(,),<,>,?,/,\,|,},{,~,:,;,.,[,]'.strip(',')

    sentence = input('Say something -_-')
    editing_list = sentence.split()
    d = {}

    def version_1():
        greedy_list = [w.strip(SPECIAL_CHAR) for w in sentence.split()]
        d = dict((i, greedy_list.count(i)) for i in set(greedy_list))
        return d

    # вроде бы первая версия очень классная, спец символы убрали все дела , но на деле нечитабельно *_*

    def version_2():

        for i in editing_list:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    # вариант от народа для народа

    print(version_1())
