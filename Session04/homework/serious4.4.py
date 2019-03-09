print("quiz")
print("question:\nif x = 8, then what is the value of 4(x + 3)?\n")
print("options:\n1. 35\n2. 36\n3. 40\n4. 44\n")

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
            stop = True
            break
        else:
            print(':(\nYou ran out of your attempts')
            stop = True
            break
    if stop:
        break

while True:
    next = input("Go to the next question?\nChoose 'y' for yes and 'n' for no.\n")
    if next == 'y':
        print("Question:\n Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
        print("Options:\n 1. About 55\n2. About 65\n3. About 75\n4.About 85\n")

        while True:
            choice = input("please choose '1', '2', '3', '4'\n")
            if choice == '2':
                print('bingo')
                break
            else: print(':(')
            while True:
                choice = input("please choose again '1', '2', '3', '4'\n")
                if choice == '2':
                    print('bingo')
                    stop = True
                    break
                else: 
                    print(':(\nYou ran out of your attempts')
                    stop = True
                    break
            if stop:
                break
        break
    elif next == 'n':
        break
    else: print("INVALID INPUT! Only 'y' of 'n' for your choice")
    break

        

 


