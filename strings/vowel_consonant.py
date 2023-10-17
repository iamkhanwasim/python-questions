# Count Vowels and Consonants:
# Create a function that counts the number of vowels and consonants in a given string.

class VowelsConsonant:
    def __init__(self) -> None:
        pass

    def count_vowles_consonant(self, input_string):
        """
        Counts the number of vowels and consonants in the string.\n
        Return Count of vowels and count of consonant
           """
        vowels = "aeiou"
        # lst_vowels = vowels.split(",")
        count_vowels, count_consonant = 0, 0
        input_string = input_string.replace(" ","")

        for str in input_string:
            if str.isalpha():
                if str.lower() in vowels:
                    count_vowels +=1
                else:
                    count_consonant +=1
                    
        return count_vowels,count_consonant

my_string = "How are you Aaron?"
vow_cons = VowelsConsonant()
vow , cons = vow_cons.count_vowles_consonant(my_string)

print("Vowels",vow)
print("Consonant",cons)