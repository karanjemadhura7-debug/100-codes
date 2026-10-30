# 27. Vowel or Consonant

char = input("Enter an alphabet: ").lower()

if len(char) != 1 or not char.isalpha() or not char.isascii():
    print("Please enter a single English alphabet.")
elif char in "aeiou":
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")
