print("answer quiz: ")
quiz_1 = {'question':'if x = 8, then what is the value of 4(x + 3)?',
         1: 35,
         2: 36,
         3: 40,
         4: 44
}
number_of_correct_answers = 0

print("first quiz: ", quiz_1)
for i, j in quiz_1.items():
    print(i, j)
    n = int(input("Your choice is: "))
    if n == 4:
        print('bingo')
        number_of_correct_answers +=1
        break
    else: print(':(')
    while True:
        n = int(input("please choose again: "))
        if n == 4:
            print('bingo')
            number_of_correct_answers +=1
            stop = True
            break
        else:
            print(':(\nYou ran out of your attempts')
            stop = True
            break
    break



