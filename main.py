# 1. banking management system (Oops)

class bank_acount:  

    def __init__(self,name,balance=0):
        self.name = name
        self.__balance = balance


    def deposit (self,amount):
        if self.__balance > 0:
            self.__balance += amount
            print(self.name,"added succcessfully ! \n your balance is ",self.__balance)
        else:
            print(self.name,"you have an Invalid Amount.")

    def widthdow(self,amount):
        if amount <= 0:
            print(self.name,"you cannoy widthraw amount! \n first deposit amount to widthraw")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(self.name,"widthrow sussfully! \n your balance is ",self.__balance)
        else:
            print(self.name,"insufficant balance")
    def check_balance(self):
        print("account holder :", self.name)
        print("balance :", self.__balance)

    def transfer_amount(self,other_account,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount
            print(self.name,"transfer successfully \n your balance is ",self.__balance)
        else:
            print(self.name,"insuffiant balance")



print("\n -------------- Account 1 holder history --------------- ")
account = bank_acount("rizwan",50000)
account1 = bank_acount("amaan",7000)
account.transfer_amount(account1,2000)
account.deposit(4000)
account.widthdow(40000)
account.check_balance()

print("\n -------------- account 2 holder history --------------- ")
account1.transfer_amount(account1,2000)
account1.deposit(4000)
account1.widthdow(40000)
account1.check_balance()

print("*"*30)
print(account.check_balance())
print(account1.check_balance())





# 2. Student Management system

class student:

    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_average(self):
        average = sum(self.marks)/ len(self.marks)
        return average

    def calculate_persentage(self):
        persentage = (sum(self.marks)/len(self.marks)*100)*100
        return persentage

    def calculate_grade(self):
        persentage = self.calculate_persentage()

        if persentage >= 90:
            return "A+"
        elif persentage >= 80: 
            return "A"
        elif persentage >= 70: 
            return "B+"
        elif persentage >= 60: 
            return "B"
        elif persentage >= 50: 
            return "C"
        elif persentage >= 40: 
            return "D"
        else :
            return "fail"

    def display(self):
        print("=============== student Details ===============")
        print(f"Name : {self.name}")
        print(f"Roll number : {self.roll_no}")
        print(f"Marks : {self.marks}")
        print(f"Average : {self.calculate_average()}")
        print(f"Persentage : {self.calculate_persentage()}")
        print(f"Grade : {self.calculate_grade()}")


students = {}

n = int(input("how many student info you need to enter : "))

for i in range(n):
    print(f"enter details of students {i+1}")

    name = input("enter your name : ")
    roll_no = int(input("enter your roll number : "))

    marks = []
    for j in range(3):
        mark = float(input(f"Enter your marks {j+1} :"))
        marks.append(mark)

    stu = student(name,roll_no,marks)

    students[roll_no] = stu

for roll_no , stu in students.items():
    stu.display() 





# 3. library managrement System

class book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(self.title,"issued successfully")
        else:
            print("Book is already issued")

    def return_book(self):
        if self.available is False:
            self.available = True 
            print(self.title,"return successfully ")
        else:
            print(self.title,"This book is not issued")

    def display(self):
        print("========== library books ============")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"book Available : {self.available}")
        # print(f"Book issue : {self.issue_book()}")
        # print(f"Book return : {self.return_book()}")



class member:

    def __init__(self,name):
        self.name = name

    def borrow(self,book):
        print(self.name,"is borroeing a book")
        book.issue_book()

    def returnBook(self,book):
        print(self.name,"is returning a book")
        book.return_book()
        

books = {}

n = int(input("how many books you want to enter : "))

for i in range(n):
    print(f"enter details of book {i+1}")

    title = input("enter book title : ")
    author = input("enter book author : ")

    book1 = book(title,author)
    books[title] = book1

for title,book1 in books.items():
    book1.display()

stu = book("python","John")
stu.display()
stu.issue_book()
# stu.return_book()
stu1 = member("Amaan")
stu1.borrow(stu)
stu1.returnBook(stu)




# 4. bike rental system 

class Vehical:

    def __init__(self,brand,price_per_day):
        self.brand = brand
        self.price_per_day = price_per_day
        self.is_available = True

    def is_Available(self):
        if self.is_available:
            print("Vehical is Available")
        else:
            print("vehical is not available")

    def cal_cost(self,days):
        return self.price_per_day * days

    def display(self,days):
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price_per_day}")
        print(f"Total Cost : {self.cal_cost(days)}")

    

class Car(Vehical):
    def cal_cost(self, days):
        return super().cal_cost(days) + days*500


class bike(Vehical):
    def cal_cost(self, days):
        return super().cal_cost(days) + 100


car1 = Car("toyota",2000)

bike1 = bike("bulet",5000)

n = int(input(" How many days a car for rent : "))
car1.is_Available()
car1.display(n)

m = int(input(" How many days a car for rent : "))
bike1.is_Available()
bike1.display(n)




# 5. employe payroll system

class Employee:

    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_sal(self):
        raise NotImplementedError(
            "Child must calculate salary"
        )

    def display(self):
        print(f"Name : {self.name}")
        print(f"Employee Id : {self.emp_id}")
        print(f"salary : {self.calculate_sal()}")

class FullTime(Employee):

    def __init__(self, name, emp_id,month_salary):
        super().__init__(name, emp_id)
        self.monthly_Sal=month_salary

    def calculate_sal(self):
        return self.monthly_Sal

class PartTime(Employee):

    def __init__(self, name, emp_id,hours,hour_rate):
        super().__init__(name, emp_id)
        self.hours = hours
        self.hour_rate = hour_rate

    def calculate_sal(self):
        return self.hours * self.hour_rate


emp_1 = FullTime("rizwan" , 101 , 70000 )
emp_2 = PartTime("amaan" , 102 , 100 , 250)

emp_1.display()
print()
emp_2.display()



# 6. online shopping cart system.

from abc import ABC , abstractmethod

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        print(product.name," added to cart!")

    def show_cart(self):
        total = 0
        print("your shopping cart!")

        for product in self.products:
            print(product.name,"-",product.price)
            total += product.price

class payment(ABC):
    @abstractmethod
    def pay(self,amont):
        pass

class upiPayment(payment):
    def pay(self,amount):
        print(amount,"paying amount using Upi!")

class CardPayment(payment):
    def pay(self,amount):
        print(amount,"paying amount using card!")


pro1 = Product("kayboard", 5000)
pro2 = Product("laptop" , 50000)

cart = ShoppingCart()
cart.add_product(pro1)
cart.add_product(pro2)
print()
cart.show_cart()
print()
payment = upiPayment()
payment.pay(55000)

