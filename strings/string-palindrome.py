# String Palindrome:
# Write a function to check if a string is a palindrome. A palindrome is a word, phrase, or sequence of characters 
# that reads the same forward and backward.


class Palindrome:
    def __init__(self, input_string) -> None:
        self.input_string = input_string

    def is_str_palindrome(self):
        return self.input_string == self.input_string[::-1]
    

my_string = "radar"
palindrome = Palindrome(my_string)
print("String is palindrome" if palindrome.is_str_palindrome() else "String is not a palindrome")