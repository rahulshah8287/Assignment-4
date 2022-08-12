# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]


li = []

Elements = int(input("Enter number of elements to be Stored : "))

for i in range(Elements):
    li.append(int(input(" Enter the Elements :")))

print(f'original list{li}')


l2 = list(map(lambda x:x*3,li))
print(f'Result list{l2}')
