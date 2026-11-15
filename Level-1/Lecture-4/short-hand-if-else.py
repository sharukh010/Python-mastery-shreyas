import random 

num = random.randint(0,1)

# result = ""
# if result == 1: 
#     result = "heads"
# else: 
#     result = "tails"

result = "heads" if num == 1 else "tails"
print(result)