# movies = []
# mov1 = input("Enter First Movie: ")
# mov2 = input("Enter Second Movie: ")
# mov3 = input("Enter Third Movie: ")


# ##We can directly take input into movies.append()
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


#list = [1, 2, 1]

#  input using a loop  



# n = int(input("Enter Number of Value :"))

# list = []

# for i in range(n):
#     element = input("Enter element {}: ".format(i+1))
# list.append(element)

# print("List:",list)


# copy_list = list.copy()
# copy_list.reverse()
# if(copy_list == list):
#      print("palindrome")
# else:
#      print("not palindrome")

#  input using a loop  
# creating an empty list
# Code to take input of a list
# from the user.

# Take input of the size of the list
n = int (input ("Enter number of elements: ")) 

# Declare an empty list
list = []

# Iterate for n times take inputs
for i in range (n):
    # Take input of ith element as x.
    x = int(input())
    # Append 'x' to the list.
    list.append(x)

# Print the list
#print("List:", list)


copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
      print("It is a palindrome")
else:
      print("not palindrome")