## list is ds that hold the ordered collection of items
## enclosed in square braces
## [10,20,30] list of integres
## ["Kirat",'Hello'] list of strings
## we can create a list inside the another list
## list inside other list caled the nested list
from pandas.core.common import maybe_make_list

integers=[1,2,3,4,5]
print(integers)
mixed_list=['kirat',89,90.09,'spam',45]
print(mixed_list)
## nested list

list=[1,2,3,4,[1.5,1.8],['test']]
print(list)
empty=[]
print((empty))


## ACCESSING AND THE TRAVERSE THE LIST

shopping_list = ['milk', 'Bread', 'Cheese', 'Eggs']
for i in shopping_list:
    print(i)
print(shopping_list[-1]) ## return the items form the last .

for i in range(len(shopping_list)):
    shopping_list[i] = shopping_list[i]+"+"
    print(shopping_list[i])

## UPDATE AND INSERT THE LIST

myList=[1,2,3,4,5,6,7]
print(myList)
myList[2]=33   ## time complexity 0(1)
print(myList)  ## space complexity is 0(1) itself

##  INSERTION
myList1=[1,2,3,4,5,6,7]
## insert Append and the extend method
print(myList1)
myList1.insert(0,23)     ## time comp.is 0(N)
print(myList1)
myList1.append(55)
print(myList1)
## append method is 0(1)
new_list=[11,12,13,14]
myList1.extend(new_list)   ## 0(N)
print(myList1)

## SLICE AND DELETE A LIST
 # for slicing we use the slice operator
my_list=['a','b','c','d','e','f','g']
print(my_list[0:2]) ## exclude the 2nd index.
print(my_list[:1])
myList[0:2]=['x','y']
print(myList[:])


## delete pop remove and delete method
myList.pop(1)    ## 0(1)
## but to delete the element form the begging from the list the o(n) is the complexity to delete it
## if not any index is provided here the pop method delete teh lst element automatically
## delete method
del myList[1]    ##0(n)
print(myList)
## we can delete more than 11 element from the slicing
del myList[1:4]
print(myList)

## REMOVE METHODS
myList.remove(7)   ## 0(n)
print(myList)

## SEARCHING FROM THE LIST
my_List_1=[10,20,30,40,50,60,70,80,90]
target = 50
"""if target in my_List_1:        ## 0(n)
    print(f"{target} is in myList")
else:
    print(f"{target} is not in the mylist")"""

## LINEAR SEARCH
my_List_1=[10,20,30,40,50,60,70,80,90]
target = 50
def linear_search(p_list,p_target):
    for i, value in enumerate(p_list):   ##0(N)
        '''enumerate(p_list) returns pairs: (index, element)

So, on each loop:

i → index (0, 1, 2, …)

value → element of the list'''
        if value == p_target:            ##0(1)
            return i                     ##0(1)
    return -1                            ##0(1)

print(linear_search(my_List_1,target))

##********************** LIST OPERATIONS **********************
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)


### * OPERATOR
a=[10]
a=a*4    ## 4 times repeated
print(a)

## *******************LIST FUNCTIONS********************************
a=[0,1,2,3,4,5,6]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))

listum = list()

while True:
    inp = input("Enter Numbers: ")
    if inp == 'done':
        break
    value = float(inp)
    listum.append(value)

average = sum(listum) / len(listum)

print("Average:", average)

