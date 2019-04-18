my_str = input("Enter a string: ")

words = my_str.split()

# sort the list
words.sort()

print("The sorted words are:")
for word in words:
   print(word)