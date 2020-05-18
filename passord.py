def passwords():
    import string
    import random
    password = string.ascii_letters
    numbers = string.digits
    punc = string.punctuation



    website = input("Enter the website: ")
    for i in range(1):
        list = []
        for i in password:
            list.append(i)
        for j in numbers:
            list.append(j)
        for k in punc:
            list.append(k)
        # print(list)

        gen_pass = "".join(random.choice(list) for l in range(12))
        # print(gen_pass)

        p = open("random_passwords", "a")
        p.write("{}:{}\n".format(website, gen_pass))

        p.close()







passwords()
