# Reverse a String:
# Write a Python function to reverse a given string.

class ReverseString:
    def __init__(self, input) -> None:
        self.input = input

    def reverse_string(self):
        return self.input[::-1]
    
input_string = "mystring"
reverser = ReverseString(input_string)
reversed_string = reverser.reverse_string()
print(reversed_string)