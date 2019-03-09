print("answer quiz: ")
quiz = []
quiz_1 = {'question':'if x = 8, then what is the value of 4(x + 3)?',
         1: 35,
         2: 36,
         3: 40,
         4: 44
}
quiz_2 = {'question':'Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?', 
         1: 'About 55',
         2: 'About 65',
         3: 'About 75',
         4: 'About 85'
}
quiz.append(quiz_1)
quiz.append(quiz_2)
number_of_correct_answers = 0

print("first quiz: ", quiz_1)
for i, j in quiz_1.items():
    print(i,':', j)
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

while True:
    next = input("Go to the next quiz?\nChoose 'y' for yes or 'n' for no.\n")
    if next == 'y':
        print("second quiz: ", quiz_2)
        for h, k in quiz_2.items():
            print(h,':', k)
        while True: 
            n = int(input("Your choice is: "))
            if n == 2:
                print('bingo')
                number_of_correct_answers +=1
                break
            else: print(':(')
            while True:
                n = int(input("please choose again: "))
                if n == 2:
                    print('bingo')
                    number_of_correct_answers +=1
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
    else: print("INVALID INPUT! Only 'y' or 'n' for your choice")
    break
print('The number of correct answer', number_of_correct_answers, 'from', len(quiz), 'question')

        

 


