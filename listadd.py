#This program takes the input of list from user and adds it
def sum_numbers(list1):
    total = 0
    for elements in range(0, len(list1)):
     total = total + list1[elements]
    return total
list1=[]
num_elements = int(input("Enter the number of elements"))
for i in range(0,num_elements):
    elements = int(input(0))
    list1.append(elements)
print("The list entered by user is :", list1)
sum_numbers([list1])
print("Sum of all elements in given list: ", sum_numbers)
