# Reference : https://tinyurl.com/ykfmzjf9
# Example   : 105263157894736842 -> 210526315789473684

from functools import reduce


def find_number(last_digit):
    digits = [last_digit]
    reminder = 0

    while True:
        reminder, next_to_add = divmod(digits[0] * 2 + reminder, 10)
        digits.insert(0, next_to_add)
        if next_to_add == digits[-1]//2 and reminder == 0:
            break

    return reduce(lambda x, y: x * 10 + y, digits)


def main():
    number = find_number(2)
    nbr_digits = len(str(number))
    moved = (number // 10) + (number % 10 * 10**(nbr_digits-1))
    print(f'{number} --> {moved} (Valid: {number * 2 == moved})')


if __name__ == '__main__':
    main()
