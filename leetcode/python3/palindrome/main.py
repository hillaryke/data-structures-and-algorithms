# An integer is a palindrome when it reads the same forward and backward.
#
# For example, 121 is a palindrome while 123 is not.

def is_palindrome(num1):
    num = 12345
    digits = [int(digit) for digit in str(num)]
    num_centre = int(sum(digits) / len(digits))

    print(num_centre)
    return num_centre

    my_list = [10, 20, 30, 40, 50]

    for index, value in enumerate(my_list):
        print(f"Index: {index}, Value: {value}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_palindrome(121)


