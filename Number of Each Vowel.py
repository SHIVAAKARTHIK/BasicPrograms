vowels = 'aeiou'

original_str = input("Enter a string: ")

original_str = original_str.casefold()

count = {}.fromkeys(vowels, 0)

for char in original_str:
    if char in count:
        count[char] += 1

print(count)
