"""
123456 -> one hundered twenty three  four hundred fifty six 

1-9 
10-100 multiples of 10's 
1000 -> thousand 
1000000 -> million 
1000000000 -> billion
counter = 1, 
counter = (counter + 1 )% 3 -> 0 to 2  
digit = 4 
unit_digit = digit * (10**counter)  
1 2 3 4
      ^ 

counter = 1 to 3 
1 -> 1 
2 -> 100 (1)
3 -> 1000 (10 ** (3-1))
"""
number = input("Number: ")[::-1]
word = ""
counter = 0 
for index in range(0,len(number),3): 
    num = number[index:index+3][::-1]
    w = "" 
    for digit in num: 
        if counter != 2: 
            unit_digit = int(digit) * (10 ** (counter))
        else: 
            unit_digit = int(digit)

        match unit_digit: 
            case 1: 
                w += "one"
            case 2: 
                w += "two"
            case 3: 
                w += "three"
            case 4: 
                w += "four"
            case 5: 
                w += "five"
            case 6: 
                w += "six"
            case 7: 
                w += "seven"
            case 8: 
                w += "eight"
            case 9: 
                w += "nine"
            case 10: 
                w += "ten"
            case 20: 
                w += "twenty"
            case 30: 
                w += "thirty"
            case 40: 
                w += "forty"
            case 50: 
                w += "fifty"
            case 60: 
                w += "sixty"
            case 70: 
                w += "seventy"
            case 80: 
                w += "eighty"
            case 90: 
                w += "ninety"
        w += " " # three digit word 
        if counter == 0: 
            w += "hundred "
        counter = (counter + 1 ) % 3 
    word = w + word # whole number word 

print(word)
