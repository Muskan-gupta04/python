
str = input("Enter a sentence: ")

word_cnt = len(str.split())
digit_cnt = sum(c.isdigit() for c in str)
uppercase_cnt = sum(c.isupper() for c in str)
lowercase_cnt = sum(c.islower() for c in str)
print(f"This sentence has {word_cnt} words")
print(f"This sentence has {digit_cnt} digits")
print(f"{uppercase_cnt} upper case letters")
print(f"{lowercase_cnt} lower case letters")

