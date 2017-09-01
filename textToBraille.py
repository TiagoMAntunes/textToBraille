def answer(plaintext):
    main = ["1000","1100","1010","1011","1001","1110","1111","1101","0110","0111"]
    word = ""
    for s in plaintext:
        if(ord(s) == 32):
            word += "000000"
        else:
            if(ord(s) > 96):
                id = ord(s)-97;
            else:
                id = ord(s) - 65
                word += "000001"
            if(id <= 9 >= 0):
                number = main[id]
                word += number[:2] + "0" + number[2:] + "0"
            elif(id > 9 and id < 20):
                number = main[id-10]
                word += number[:2] + "1" + number[2:] + "0"
            elif(id > 19 and id < 22):
                number = main[id-20]
                word += number[:2] + "1" + number[2:] + "1"
            elif(id > 22):
                id = id - 1
                number = main[id-20]
                word += number[:2] + "1" + number[2:] + "1"
            elif(id == 22):
                word += "010111"
    return(word)

def printToReal(word):
    done = False
    i = 0
    while not done:
        isDone = False
        j = 0
        while not isDone:
            print(word[i+j], end ='')
            j += 3
            if j >= len(word):
                isDone = True
                print()
        i += 1
        if i == 3:
            done = True

word = answer(input("Please type in the text you want to make in braille text: "))
print()
printToReal(word)
