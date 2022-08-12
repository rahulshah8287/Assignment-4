# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

li = []

Elements = int(input("Enter number of elements to be Stored : "))

for i in range(Elements):
    li.append(int(input(" Enter the Elements :")))

print(f'original list{li}')

def square(x):
    return x**2

l2 = list(map(square,li))
print(l2)
