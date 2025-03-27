# Task:-
# 1.implement the count method on a list by taking input from the user without using the actual method.

List_of_number = [1,2,1,4,3,5,7,9,8,5,5,3,6,4,2,1,8,6,1,11,2,10,1,4,22,11,11,14,10,3,2,1,5,1,4,1,3,2,1,0,2,11,0,11,88,7,7,6,6,2,2,1]
num = int(input("please enter a number to find the count of the number in list : "))
count = 0
for i in range(1,len(List_of_number)+1,1):
    count+=1
print(List_of_number.count(num))



# 2.implement the copy method on a list just as the above condition.

list1 = [1,"BCA",654,1,2,5,4,7,5,7,7,5,4,7,"name","hemanth","coding","range"]
list2 = list1.copy()
print("original list",list1)
print("copied list",list2)
