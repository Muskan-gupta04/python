
num = input("Enter a number: ")


if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


digit_count = {}
for digit in num:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1


print("Digit occurrences:")
for digit, count in digit_count.items():
    print(f"{digit} appears {count} times")
