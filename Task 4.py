#1 Print even and odd numbers in seperate list..................................
from multiprocessing.reduction import duplicate

org_list = [10,501, 22,37, 100, 999, 87, 351]

#new list with even and odd numbers:
even_numbers = []
odd_numbers = []

#based on below condition list can spitted
for num in org_list:
    if num %2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Given list", org_list)
print("Even number list", even_numbers)
print("Odd number list", odd_numbers)

#2 Find prime number.....................................................

list1 = [10,501, 22,37, 100, 999, 87, 351]

for nums in list1:
    if nums > 1:
        for i in range (2, nums):
            if nums % i == 0:
                break
        else:
            print("Prime number is", nums)

#3 No idea how to proceed.............................................

#4 sum of first and last digit of a integer.................................................

#getting input from user
num = (input("Enter a number: "))

#accessing data based in index =
first_number = int(num[0])
last_number = int(num[-1])

# sum of first and last number
sum = first_number + last_number

print("First number = ", first_number)
print("Last number = ", last_number)
print("Sum of first and last number =", sum)


#5 Coin change...............................................................................

total = 10

for one in range (total+1):
    for two in range (total // 2 + 1):
        for five in range (total// 5 + 1):
            for ten in range (total // 10 + 1):
                if one * 1 + two * 2 + five * 5 + ten * 10 == total:
                    result = (
                            "1$ *" + str(one) + "," +
                            "2$ *" + str(two) + "," +
                            "5$ *" + str(five) + "," +
                            "10$ *" + str(ten)
                    )
print(result)

#6 To find duplicates in the list................................................

#Creating list:
List1 = ["Apple", "Orange", "Cherry"]
List2 = ["Grapes", "Cherry", "Pineapple"]
List3 = ["Grapes", "Cherry", "Mango"]

#grouping lists
group = List1+List2+List3
print("To find duplicate from:", group)

#Store value in empty list
Duplicate = []

# Check each item in list:
for item in group:
    if group.count(item) > 1 and item not in Duplicate:
        Duplicate.append(item)

#Print duplicate list:
print("Duplicate elements: {}".format(Duplicate))

#7 Non repeating items...................................

value = [1,2,3,4,5,2,3,6,7,9,1,5,6,8,8,2]

unique = []

for data in value:
    if value.count(data) == 1:
        unique.append(data)
print("Unique items in list:", unique)

#8 minimum element in list...................................

minimum = [5,10,11,33,6,22,98,13]
val = minimum[0]

print("The mininum value is:", val)

#9 Triplet...............................................

given = [10,20,30,9]
target = 59

#check if triplet is found
got = False

#check each number
for i in range(len(given)):
    for j in range (i+1, len(given)):
        for k in range(j+1, len(given)):
            if given[i] + given[j] + given[k] == target:
                print("Triplet is:", given[i], given[j], given[k])
                print("Sum of triple", given[i], "+" , given[j], "+" , given[k], "=" , given[i]+given[j]+given[k])
                got = True
if not got:
    print("No luck to find triple for target", target)

#10 find subset with sum of zero - No idea..................................................















