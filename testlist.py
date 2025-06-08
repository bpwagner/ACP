def change_letter(index):
    letter = input("Enter a letter: ")
    if len(letter) > 1 or len(letter) < 1:
        return "Must be exactly one character!"
    elif letter != letter.lower():
        return "Character must be a lowercase letter!"
    else:
        letter_list[index] = letter
        return "".join(letter_list)


word = input("Enter a word: ")
letter_list = list(word)
keep_going = True

index = int(input("Enter an index (-1 to quit): "))
while (index != -1):
    print(change_letter(index))
    index = int(input("Enter an index (-1 to quit): "))

print("Done")
