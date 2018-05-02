one_to_nineteen = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', \
 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18: 'eighteen', 19:'nineteen'}         # Created an associative array to access the number later in the function

twenty_to_ninety = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

hundred = 'hundred'
thousand = 'thousand'

#my_number = str(input('Please enter 2 numbers between 1 up to 10000 seperated by a space: '))

my_number = input('Please enter 2 numbers between 1 up to 10000 seperated by a space: ').split()



def numberToWord(number):
    word_result = ''
    split_number = list(map(int,number))
    if len(number) == 1:                # Checking if the length of the string is one thus a single digit number
        word_result += one_to_nineteen[number]
        return word_result
    elif len(number) == 2:              # Checking if the length of the string is two thus a double digit number
        if split_number[0] == 1:
            word_result += one_to_nineteen[int(number)]
        else:
            word_result += twenty_to_ninety[split_number[0]]
            if split_number[1] != 0:
                word_result += one_to_nineteen[split_number[1]]
        return word_result
    elif len(number) == 3:                  # Checking if the length of the string is three thus a three digit number
        word_result += one_to_nineteen[split_number[0]] + ' hundred'
        if split_number[1] == 1:
            word_result += ' and ' + one_to_nineteen[int(number[1:])]
        elif split_number[1] != 0:
            word_result += ' and ' + twenty_to_ninety[split_number[1]]
            if split_number[2] != 0:
                word_result += one_to_nineteen[split_number[2]]
        elif split_number[1] == 0:
            if split_number[2] != 0:
                word_result += ' and ' + one_to_nineteen[split_number[2]]
        return word_result
    elif len(number) == 4:                      # Checking if the length of the string is four thus a four digit number
        word_result += one_to_nineteen[split_number[0]] + ' thousand '
        if split_number[1] != 0:
            word_result += ',' + one_to_nineteen[split_number[1]] + ' hundred '
        if split_number[2] == 1:
            word_result += 'and ' + one_to_nineteen[int(number[2:])]
        elif split_number[2] != 0:
            word_result += 'and ' + twenty_to_ninety[split_number[2]]
            if split_number[3] !=0:
                word_result += one_to_nineteen[split_number[3]]
        return word_result
    elif len(number) == 5:                  # Checking if the length of the string is five thus a five digit number
        word_result += 'Ten thousand'
        return word_result



def rangeFunction(numberRange):             # Function that checks if the input is a list and if so itterate through that range else it itterates through the whole 10000 numbers
    if isinstance(numberRange,list):
        number1 = int(numberRange[0])
        number2 =int(numberRange[1])
        for number in range(number1,number2):
            return(numberToWord(str(number)))
    else:
        for i in range(10001):
            return (numberToWord(i))

#result = numberToWord(my_number)

result = rangeFunction(my_number)
print(result)
