def encryption():
    import string
    import re
    e = open('random_passwords', 'r')
    file_contents = e.read()

    e.close()
    ultimate_list = []
    punc = string.punctuation
    punc_list = []
    for i in punc:
        punc_list.append(i)
        ultimate_list.append(i)
    punc_2 = str(" ".join(punc))

    letters = string.ascii_letters
    letters_list = []
    for i in letters:
        letters_list.append(i)
        ultimate_list.append(i)
    letters_2 = str(" ".join(letters))

    digits = string.digits
    digits_list = []
    for i in digits:
        digits_list.append(i)
        ultimate_list.append(i)
    digits_2 = str(" ".join(digits))

    ultimate_list.append('\n')

    # print(ultimate_list)
    # print(len(ultimate_list))
    """
    print(len(punc_list)) # middle is 16
    print(punc_2)
    print(punc_list)  # middle is 16
    print(len(letters_list)) # middle is 26
    print(letters_list)
    print(len(digits_list)) # middle is 5
    print(digits_list)
    """
    # If the character is a punctuation, a letter or a digit, find its location in the list, then swap it with its
    # equivalent character in the list based on the mean.
    new_contents = []
    print(file_contents)
    # For punctuation, there are 32 characters, therefore using 16 characters

    for i in file_contents:
        position = ultimate_list.index(i)
        encrypted_letters = ultimate_list[(95 - position)]
        new_contents.append(encrypted_letters)
        # print(position)

    text = "".join(new_contents)
    print(text)

    file = open("random_passwords", "w")
    file.write(text)
    file.close()

    # print(new_contents)


# The punctuation and numbers will follow the same encryption methodology
# for punc punc_list[10-c]


encryption()
