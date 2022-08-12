# print("hi")
# print(oct(10))
#
# firstName = "john"
# lastName = "k"
# age = 25
# ssn = 12312434243
# height = "172 cm"
# weight = "54 kg"
#
# print(len(firstName))
#
# myNumber = 10
# floatNumber = 20.54
# myBoolean = True
# myString = "I am the best"
#
# print(myNumber, '\n', floatNumber, '\n', myBoolean, '\n', myString)
#
# countriesList = ["India", "Pakistan", "Nepal"]
# countriesList.append("USA")
# del countriesList[2]
# countriesList.insert(2,"Sri Lanka")
# print(countriesList)
#
# countriesSet = {"India", "Pakistan", "Nepal"}
# countriesSet.add("USA")
# print(countriesSet)
#
# availToppings = ["Onions", "Lettuce", "Tomato", "Olives", "Peppers", "Tomatoes"]
# print("Available Toppings : ")
# for topping in availToppings:
#     print(topping)
# print("Pick Three Toppings : ")
# toppings, total = [], 0
# for i in range(3):
#     toppings.append(input("Topping {} : ".format(i+1)))
# for topping in toppings:
#     if not availToppings.__contains__(topping):
#         print(topping, "is not available")
# noOfSw = int(input("How Many SandWiches : "))
# total = noOfSw * 5
# print("Total Price : {}".format(total))
#
# subjects = {"maths": 0, "physics": 0, "chemistry": 0}
# total, avg, grade = 0, "Fail", "No Grade - Fail"
# for subject in subjects.keys():
#     subjects[subject] = float(input("Enter {} Mark : ".format(subject)))
#     if subjects[subject] < 35.0:
#         subjects[subject] = -1
#     total += subjects[subject]
# if -1 not in subjects.values():
#     avg = total/(len(subjects))
#     if avg <= 59:
#         grade = "C"
#     elif avg <= 69:
#         grade = "B"
#     else:
#         grade = "A"
# print("Average : {}".format(avg))
# print("Grade : {}".format(grade))
#
# x = 2
# y = 10
# if x % 2 == 0: x = x+1
# while x <= y:
#     print(x)
#     x = x + 2
#
# for i in range(20):
#     if i%3 == 0:
#         continue
#     print(i)
#
# assert False, "tataatata"
# print("ajdsajkdna")
#
# lst = [int(x) for x in input("Enter elements of an list : ").split()]
# finalList = list(set(lst))
# print(finalList)
#
# lst = [int(x) for x in input("Enter elements of an list : ").split()]
# finaList = []
# for i in lst:
#     if i not in finaList:
#         finaList.append(i)
# print(finaList)
#
# vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
# word = input("Enter the word : ")
# for i in word:
#     if i in vowels:
#         vowels[i]+=1
# for vowel in vowels.keys():
#     if vowels[vowel]>0:
#         print(vowel,"is present ",vowels[vowel],"times")
#
# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     if i > 100:
#         break
#     elif i % 10 == 0:
#         continue
#     else:
#         print(i)
#
# n = int(input("Enter a number : "))
# m = round(n/2)
# for i in range(2, m):
#     if n % i == 0:
#         print("not a prime")
#         break
#     else:
#         print("prime")
#         break
#
# str = input("Enter a string : ")
# print(string[::-1])
# result = ''
# for i in range((len(string)-1), -1, -1):
#     result += string[i]
# print(result)
#
# n = input("enter ")
# # s = "Enter " + n + "'s number : "
# str = input("Enter {}'s number : ".format(n))
#
# print(''.join(reversed(string)))
#
# result = ' '.join(string.split()[::-1])
# print(result)
#
# spl = string.split()
# for i in range(len(spl)):
#     spl[i] = spl[i][::-1]
# print(' '.join(spl))
#
# temp = []
# for i in str:
#     if i not in temp:
#         temp.append(i)
# print(''.join(temp))
#
# for i in temp:
#     print(i, "-", str.count(i), " times")
#
# n = int(input("Enter a number : "))
# for i in range(1, n+1):
#     print(' '*(n-i), end='')
#     print('* '*i)
#
# sc = input("Enter the search word : ")
# pos = -1
# while str[(pos+1):].__contains__(sc):
#     pos = str.find(sc, pos+1, len(str))
#     print("found at {}".format(pos))
# if pos == -1:
#     print("not found")
#
# import sys
# print(sys.argv)
# print(int(sys.argv[1])*int(sys.argv[2]))
#
# import sys
# accBal = 10000
# if int(sys.argv[1]) == 1:
#     print("Account balance : rs {}/-".format(accBal))
# elif int(sys.argv[1]) == 2:
#     amWith = int(input("Enter the amount to withdraw : "))
#     accBal -= amWith
#     print("rs {}/- withdraw done".format(amWith))
#     print("Account Balance : rs {}/-".format(accBal))
# elif int(sys.argv[1]) == 3:
#     depcash = int(input("Enter the amount to deposit as cash : "))
#     accBal += depcash
#     print("rs {}/- deposited as cash".format(depcash))
#     print("Account Balance : rs {}/-".format(accBal))
# elif int(sys.argv[1]) == 4:
#     depcheck = int(input("Enter the amount to deposit as check : "))
#     accBal += depcheck
#     print("rs {}/- deposited as check".format(depcheck))
#     print("Account Balance : rs {}/-".format(accBal))
#
# x =12
# def a():
#     print(x)
#     globals()['x'] = 2
# b = a
# b()
# print(x)
#
# iseven = lambda n:"yes" if n%2 == 0 else "no"
# print(iseven(4))
#
# lst = [1,2,3,4]
# lstf = filter(lambda x: x%2 == 0,lst)
# print(lstf)
#
# def decor(fun):
#     def inner(nm):
#         res = fun(nm)
#         res += ",how are you?"
#         return res
#     return inner
#
# @decor
# def dei(name):
#     return "Dei "+name
#
# print(dei("Vikash"))
#
# lst = [x for x in range(10, 30, 2)]
# print(lst)
# lst1 = [x for x in range(1, 21) if x % 2 == 0]
# print(lst1)
# lst2 = [lst[x]*lst1[x] for x in range(10)]
# print(lst2)
# lst3 = [x for x in lst if x in lst1]
# print(lst3)
#
# oops ==================================================================================
#
# class Patient:
#     def setId(self, id):
#         self.id = id
#     def setName(self, name):
#         self.name = name
#     def setSsn(self, ssn):
#         self.ssn = ssn
#     def getId(self):
#         return self.id
#     def getName(self):
#         return self.name
#     def getSsn(self):
#         return self.ssn
#
# patient1 = Patient()
# patient1.setId(123)
# patient1.setName("Vikash")
# patient1.setSsn(1238752794234)
# print("ID : ",patient1.getId())
# print("Name : ",patient1.getName())
# print("Ssn : ",patient1.getSsn())
#
# from abc import *
# class TouchScreenLaptop(ABC):
#     @abstractmethod
#     def scroll(self):
#         pass
#
#     @abstractmethod
#     def click(self):
#         pass
#
# class HP(TouchScreenLaptop):
#     def scroll(self):
#         print("HP - Scrolled")
#
# class DELL(TouchScreenLaptop):
#     def scroll(self):
#         print("DELL - Scrolled")
#
# class HPNoteBook(HP):
#     def click(self):
#         print("HP - clicked")
#
# class DELLNoteBook(DELL):
#     def click(self):
#         print("DELL - clicked")
#
# HPNB1 = HPNoteBook()
# HPNB1.scroll()
# HPNB1.click()
#
# DELLNB1 = DELLNoteBook()
# DELLNB1.scroll()
# DELLNB1.click()
#
# class InvalidPasswordException(BaseException):
#     def __init__(self,msg):
#         self.msg = msg
# password = input("Enter the password : ")
# try:
#     if len(password) > 8:
#         raise InvalidPasswordException("The length of the password is greater than 8 characters")
# except InvalidPasswordException as msg:
#     print("InvalidPasswordException : ", msg)
#
# import time,datetime
# epochseconds = time.time()
# print(epochseconds/3600/24/365 - 2023)
#
# import time,datetime
# class Event:
#     def __init__(self,name,startTime,endTime):
#         self.name = name
#         self.startTime = startTime
#         self.endTime = endTime
#         self.venue = None
#
#     def addVenue(self,venue):
#         self.venue = venue
#
# class Venue:
#     def __init__(self,name):
#         self.name = name
#         self.address = None
#
#     def addAddress(self,address):
#         self.address = address
#
# class Address:
#     def __init__(self,street,city,state,country,zipcode):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.country = country
#         self.zipcode = zipcode
#
# event = Event("Cricket Match",datetime.datetime(2022,8,10,19,30,0),datetime.datetime(2022,8,11,9,30,0))
# venue= Venue("Central Cricket Ground")
# address = Address("Dhoni street","Chennai","Tamil Nadu","India","641024")
# venue.addAddress(address)
# event.addVenue(venue)
#
# print("Event Name :",event.name)
# print("Venue : ",event.venue.name)
# print("Address : ",event.venue.address.street,",",event.venue.address.city,",",event.venue.address.state,",",event.venue.address.country,"-",event.venue.address.zipcode)
#
# Threads ========================================================================
#
# from threading import *
# from time import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print(i+1)
#
# t1 = MyThread()
# t1.start()
#
# class MyClass:
#     def fun(self):
#         for i in range(10):
#             print(i+1)
#
# myObj = MyClass()
# t1 = Thread(target=myObj.fun)
# t1.start()
#
# class Producer:
#     def __init__(self):
#         self.products = []
#         # self.ordersplaced = False
#         self.c = Condition()
#     def produce(self,n):
#         self.c.acquire()
#         for i in range(n):
#             sleep(1)
#             self.products.append("product-{}".format(i+1))
#             print("item-{} Added".format(i+1))
#         # self.ordersplaced = True
#         self.c.notify()
#         self.c.release()
#
# class Consumer:
#     def __init__(self,producer):
#         self.producer = producer
#     def consume(self):
#         self.producer.c.acquire()
#         # while self.producer.ordersplaced == False:
#             # print("Waiting for the orders")
#             # sleep(0.5)
#         self.producer.c.wait(timeout=0)
#         self.producer.c.release()
#         print("Order shiped {}".format(self.producer.products))
#
# producer1 = Producer()
# consumer1 = Consumer(producer1)
# n = int(input("Enter the number of products : "))
# producerThread = Thread(target=producer1.produce,args=(n,))
# consumerThread = Thread(target=consumer1.consume)
#
# producerThread.start()
# consumerThread.start()
#
# from queue import *
# from random import *
# def producer(q):
#     while True:
#         print("producing products")
#         q.put(randint(1,10))
#         print("product produced")
#         sleep(2)
#
# def consumer(q):
#     while True:
#         print("ready to consume")
#         print("consume data ",q.get())
#         sleep(2)
#
# q = Queue()
# prodThread = Thread(target=producer,args=(q,))
# consThread = Thread(target=consumer,args=(q,))
#
# consThread.start()
# prodThread.start()
#
# from threading import *
# def oddNumbers(c):
#     for i in range(1,100,2):
#         c.acquire()
#         c.wait()
#         print(i,end=' ')
#         c.notify()
#         c.release()
#
# def evenNumbers(c):
#     for i in range(2,101,2):
#         c.acquire()
#         c.wait()
#         print(i,end=' ')
#         c.notify()
#         c.release()
#
# c = Condition()
# oddThread = Thread(target=oddNumbers,args=(c,))
# evenThread = Thread(target=evenNumbers,args=(c,))
#
# oddThread.start()
# c.acquire()
# c.notify()
# c.release()
# evenThread.start()
#
# import urllib.request
# try:
#     url = urllib.request.urlopen("https://www.python.org/")
#     content = url.read()
#     url.close()
# except urllib.error.HTTPError:
#     print("web page not found")
#     exit()
# 
# file = open("index.html","wb")
# file.write(content)
# file.close()
# 
# url = "https://www.python.org/static/img/python-logo@2x.png"
# urllib.request.urlretrieve(url,"python.png")
#
# import socket
#
# host = "localhost"
# port = 4000
#
# socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket1.bind((host,port))
# socket1.listen(1)
# print("server listeing on port : ",port)
# c,addr = socket1.accept()
# print("connected to",str(addr))
# c.send("Hi from server".encode())
# c.close()
#
# host = "localhost"
# port = 4000
#
# socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket1.bind((host,port))
# socket1.listen(1)
# print("server listening on port : ",port)
# c,addr = socket1.accept()
# fileName = c.recv(1024)
# try:
#     file = open(fileName,"rb")
#     content = file.read()
#     c.send(content)
#     file.close()
# except FileNotFoundError:
#     c.send("file does not exist".encode())
# c.close()
#
# import smtplib
# from email.mime.text import MIMEText
#
# body = "this is a test email,how are you?"
# msg = MIMEText(body)
# msg['From'] = "vikycbe003@gmail.com"
# msg['To'] = "vikycbe003@gmail.com"
# msg['Subject'] = "hellof"
#
# server = smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()
# passWord = input("Enter the gmail password : ")
# server.login("vikycbe003@gmail.com",passWord)
# server.send_message(msg)
# print("Email sent")
# server.quit()
#
# mysql with python ========================================
#
# import mysql.connector
# connection = mysql.connector.connect(host="sql6.freemysqlhosting.net",database="sql6511999",user="sql6511999",password="SpaBAicutN")
# if connection.is_connected():
#     print("Mysql database is connected")
#     cursor = connection.cursor()
#     try:
#         cursor.execute("insert into emp values(3,'abhy',30000);")
#         connection.commit()
#         print("Employee added")
#     except:
#         connection.rollback()
#     cursor.execute("select * from emp;")
#     rows = cursor.fetchall()
#     print("Total number of rows : ",cursor.rowcount)
#     for row in rows:
#         print(row)
#     cursor.close()
#     connection.close()
#
# def delete(empId):
#     connection = mysql.connector.connect(host="sql6.freemysqlhosting.net", database="sql6511999", user="sql6511999",
#                                          password="SpaBAicutN")
#     if connection.is_connected():
#         print("Mysql database is connected")
#         cursor = connection.cursor()
#         string = "delete from emp where id='%d'"
#         args = empId
#         try:
#             cursor.execute(string % args)
#             connection.commit()
#             print("Employee deleted")
#
#             cursor.execute("select * from emp;")
#             rows = cursor.fetchall()
#             print("Total number of rows : ", cursor.rowcount)
#             for row in rows:
#                 print(row)
#         except mysql.connector.errors.DatabaseError:
#             connection.rollback()
#             print("database error occurred")
#         finally:
#             cursor.close()
#             connection.close()
#             print("Mysql database is disconnected")
#
#
# empId = int(input("Enter Employee id to be deleted : "))
# delete(empId)
#
# mongoDB =========================================================
#
# from pymongo import *
# client = MongoClient("mongodb+srv://vikash:6382182587@vikash.nciz1et.mongodb.net/?retryWrites=true&w=majority")
# print("MongoDb serer connected")
# database = client["products"]
# print("Database created")
# collection = database['product']
# print("Collection created")
# products = [{
#     "name":"IPhone",
#     "price":1300
#     },
#     {
#     "name":"Samsung",
#     "price":1000
#     },
#     {
#     "name":"Redmi",
#     "price":700
#     }]
# collection.delete_many({})
# result = collection.insert_many(products)
# print("Insertedt Ids : ",result.inserted_ids)
# update = collection.update_many({"name":"IPhone"},{"$set":{"price":1500}})
# print("updated count : ",update.modified_count)
# cursor = collection.find()
# for item in cursor:
#     print(">",item)
# client.close()
#
# from numpy import *
#
# a = array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [5,6],
#         [7,8]
#     ],
#     [
#         [9,10],
#         [11,12]
#     ]
#     ])
#
# print(a.shape)
#
