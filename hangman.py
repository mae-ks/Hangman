import extract, random

hangy1 = "  ___\n |   |\n O   |\n     |\n     |\n     |\n  ======="
hangy2 = "  ___\n |   |\n O   |\n/    |\n     |\n     |\n  ======="
hangy3 = "  ___\n |   |\n O   |\n/|   |\n     |\n     |\n  ======="
hangy4 = "  ___\n |   |\n O   |\n/|\\  |\n     |\n     |\n  ======="
hangy5 = "  ___\n |   |\n O   |\n/|\\  |\n/    |\n     |\n  ======="
hangy6 = "  ___\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n  ======="
hangy = {1: hangy1, 2: hangy2, 3:hangy3, 4:hangy4, 5:hangy5, 6:hangy6}

inp = "y"
counter = 0
while (inp == "y"):
    print("\nHello USER. Welcome to Mae's Hangman:)")
    word_list = extract.word_list
    word = random.choice(word_list)
    print("\nHere's your word.\n")

    d = {}
    for i, v in enumerate(word):
        if v not in d:
            d[v] = [i]
        else:
            d[v].append(i)

    x = "__"
    interface = [x] * len(word)
    print(" ".join(interface) + "\n")

    guesses = []
    found = False

    while not found and counter < 6:
        letter = input("Enter a letter: ")
        if letter == "word":
            print("\n" + " ".join(interface) + "\n")
        elif letter == "quit":
            quit()
        elif len(letter) != 1:
            print("\nInvalid. Please enter a letter.\n")
        elif letter in guesses:
            print("\nYou have already guessed this. Enter another letter.\n")
        elif letter in word:
            guesses.append(letter)
            for i, v in enumerate(interface):
                if i in d[letter]:
                    interface[i] = letter
            print("\n" + " ".join(interface) + "\n")
            d.pop(letter, None)
        else:
            counter += 1
            guesses.append(letter)
            print("\nTry again.\n")
            print("Your guesses are:\n")
            print(", ".join(guesses))
            print(hangy[counter] + "\n")
        if x not in interface:
            found = True
    if counter == 6:
        print("Game over:( The word is '" + word + "'.")
    else:
        print("Congratulations! The word is '" + "".join(interface) + "'!")
    inp = input("\nTry again? y/n\n\n")
    if inp == "y":
        counter = 0
