class Mathematician:
    def square_nums(sequence):
        return [num ** 2 for num in sequence]

    def remove_positives(sequence):
        return [num for num in sequence if num > 0]

    def filter_leaps(sequence):
        return [num for num in sequence if (not num % 4 and num % 100 > 0) or not num % 400]


a = [7, 11, 5, 4]
a1 = [-1, 32, 11, -32, -4]
a2 = [2001, 1884, 1995, 2003, 2020]
m = Mathematician
print(m.square_nums(a))
print(m.remove_positives(a1))
print(m.filter_leaps(a2))
