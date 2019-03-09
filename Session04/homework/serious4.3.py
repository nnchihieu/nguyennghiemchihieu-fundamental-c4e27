print('quiz')
question = 'if x = 8, then what is the value of 4(x + 3)?\n'
options = '1. 35\n2. 36\n3. 40\n4. 44\n'
print(question)
print(options)

while True:
    choice = input("please choose '1', '2', '3', '4'\n")

    if choice == '4':
        print('bingo')
        break
    else: print(':(')
    while True:
        choice = input("please choose again '1', '2', '3', '4'\n")
        if choice == '4':
            print('bingo')
            break
        else:
            print(':(\nYou ran out of your attempts')
            stop = True
            break
    break 




