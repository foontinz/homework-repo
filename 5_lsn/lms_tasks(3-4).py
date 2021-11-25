import random

if __name__ == '__main__':
    # Words combination

    num = 5
    word = input('Enter word you want to combine')
    amount = len(word)
    for i in range(num):
        editing_word = word
        new_word = ''
        # print(editing_word)
        j = 0
        while j < amount:
            j += 1
            if len(editing_word) == 0:
                break
            index = random.randint(0, len(editing_word) - 1)
            # print(index, 'index')
            new_word = new_word + editing_word[index]
            # print(new_word, 'new word')
            editing_word = editing_word[:index] + editing_word[index + 1:]
            # print(editing_word, 'editing word')
        print(new_word)
