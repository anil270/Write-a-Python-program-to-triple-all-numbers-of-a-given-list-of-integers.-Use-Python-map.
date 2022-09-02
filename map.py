#Write a Python program to triple all numbers of a given list of integers. Use Python map.


list1 = list(map(int ,input("Enter the element of list :").split()))
list2 = list(map(lambda x:x*3,list1))
print("Before list :",list1)
print("After the list :",list2)