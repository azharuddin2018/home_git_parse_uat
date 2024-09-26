# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "avacado"]
# newlist = []

# for x in fruits:
#   if "a" or "e" in x:
#     newlist.append(x)

# print(newlist)


#List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "avacado"]
# newlist = []

# for x in fruits:
#   if "a" or "e" in x:
#     newlist.append(x)

# print(newlist)


#Descending [reverse = True]
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)\


# #copy list
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#Concatenate
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)



# x = lambda a, b, c : a * b + c + 10
# print(x(5,10,15))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class student():
    
#     @staticmethod
#     def abcd():
#         print("Chickado, Grill")

#     def __init__(self, name, marks):#, marks1, marks2, marks3):
#         self.name = name
#         self.marks = marks
#         # self.marks2 = marks2
#         # self.marks3 = marks3
#         print(name, marks)#, marks2, marks3)

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum + val
#         print("Hi ", self.name, "your average marks is :", sum/3)

# s1 = student("Azhar",[98,90,80])

# s1.avg_marks()
# get_name = input(print("Enter Student's Name"))
# get_marks1 = int(input(print("Enter Marks for First Subject")))
# get_marks2 = int(input(print("Enter Marks for Second Subject")))
# get_marks3 = int(input(print("Enter Marks for Third Subject")))
# s1 = student(get_name,get_marks1,get_marks2,get_marks3)



class bank():
    
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs :", amount, " was debited!!")
        print("total balance is :", self.rem_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs :", amount, " was credit!!")
        print("total balance is :", self.rem_balance())

    def rem_balance(self):
        return self.balance
    
acc1 = bank(10000, 12345)
print("Account: ",acc1.account, "Balance: ",acc1.balance)
acc1.debit(1000)
acc1.credit(500)
