"""
324 -> three two four 
100 -> one zero zero 


1st our goal is to convert 1digit -> word 
0 -> zero 
1 -> one 


word = "onetwo"

word = word + "two"
word += "two" short cut version 

1234 

1 
2
"""
number = input("Number: ")
word = "" 
for digit in number: 
    digit = int(digit) # converting string to int 

    match digit: 
        case 0:
            word += "zero" 
        case 1: 
            word += "one"
        case 2: 
            word += "two"
        case 3: 
            word += "three"
        case 4: 
            word += "four"
        case 5: 
            word += "five"
        case 6: 
            word += "six"
        case 7: 
            word += "seven"
        case 8: 
            word += "eight"
        case 9: 
            word += "nine"
    word+= " "
print(f"In words: {word}")