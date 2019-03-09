print('quiz')
question = 'if x = 8, then what is the value of 4(x + 3)?\n'
options = 'a. 35\nb. 36\nc. 40\nd. 44\n'
print(question)
print(options)

while True:
    choice = input("please choose 'a', 'b', 'c', 'd'\n")

    if choice == 'd':
        print('bingo')
        break
    else: print(':(')
    while True:
        choice = input("please choose again 'a', 'b', 'c', 'd'\n")
        if choice == 'd':
            print('bingo')
            break
        else:
            print(':(\nYou ran out of your attempts')
            stop = True
            break
    if stop:
        break




