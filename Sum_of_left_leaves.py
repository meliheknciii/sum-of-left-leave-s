import numpy as np
# sum of left leaves - LeetCode
sum = 0
arr = np.random.randint(50,size =20)
new_Arr = []
for i in range(0,20):
    if i % 4 == 1:
        new_Arr=np.append(new_Arr,arr[i])
        sum = sum + arr[i]

print(f"Left leaves : {new_Arr} \n "
      f"sum left leaves = {sum}")

# n = null
#  +        +        +        +
#3 9 20 n n 15 7 n n 5 44 n  n  33 2
#0 1 2  3 4  5 6 7 8 9 10 11 12 13 14 <- index
# The remainder 1 divided by 4 is equal to the left leaf.


