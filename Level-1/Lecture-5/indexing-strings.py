number = "123456"
"""
index will tell you how many elements you need to skip to reach 
that particular element 
1 -> 0 
2 -> 1 
3 -> 2 
4 -> 3 
5 -> 4 
6 -> 5 
"""
# print(len(number)) # it will give your the length of a string 
length = len(number)
# for index in range(length): # 0 to length -1 
#     print(number[index])

# we getting hundres position from the loop 
for index in range(0,length,3): # 0,1,2,3,4,5
    print(number[index: index+3])