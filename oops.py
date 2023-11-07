# class atm:
#     def sumvalue(self):
#         print(20+30)
# obj=atm()
# obj.sumvalue()        


# class demo:
#     a=10
#     def show(self):
#         print(self.a)
# obj=demo()
# obj.show()        



# class demo:
#     a=45
#     b=90
#     def sum(self):
#         self.c=self.a+self.b
#         print(self.c)
# o=demo()
# o.sum()        


# class demo:
#     def show(self,a,b):
#         print(a+b)
# obj=demo()
# obj.show(34,78)        



#                                       Constructor
# class pen:
#     def __init__(self):
#         print("i am a constructor")
# p=pen()        


#              Inheritance
# class A:
#     def display(self):
#         print("welcome")
# class B(A):
#     def display(self):
#         super().display()
#         print("home")
# o=B()
# o.display()                


#        multiple Inheritance
# class A:
#     def displaya(self):
#         print("i am a")
# class B:
#     def displayb(self):
#         print("i am b")
# class c(A,B):
#     def displayc(self):
#         print("i am c")
# o=c()
# o.displayc()
# o.displaya()
# o.displayb()                        



#                                private access modifiers
# class Geek: 
#     def __init__(self, age = 0): 
#          self._age = age 
      
#     # getter method 
#     def get_age(self): 
#         return self._age 
      
#     # setter method 
#     def set_age(self, x): 
#         self._age = x 
  
# raj = Geek() 
# raj.set_age(21) 
# print(raj.get_age()) 
  




#                       method overloading
# def product(a, b):
#     p = a * b
#     print(p)
 
# def product(a, b, c):
#     p = a * b*c
#     print(p)
 
# product(4, 5, 5)        

# print("Hello {0[0]} and {0[1]}".format(('foo', 'bin')))


# i = 0
# while i < -1:
#     print(i)
#     i += 1
# else:
#     print(0)

# print(hex(15))

# fruit="mango"
# # # print(fruit[1:])
# # print(fruit[:])

# print(fruit[-3:-1])

# a="!!aish!!"
# print(a.lstrip("!"))


# a="aishwarya is a an adventrous"
# print(a.split(" "))

# num=int(input("enter a number"))
# for i in range(1,11):
#     print(num*i)

# for k in range(5):
#     print(k)

# for k in range(1,20,3):
#     print(k)

# i=1
# while i<0:
#     print("executed")
# else:
#     print("check the value of i")  
# print("out from loop")      

# l1=[1,2,3]
# l2=[1,2,3]
# print(l1 is l2)
# print(id(l1), id(l2))

# l1=[1,2,3,4,5]
# l1.remove(4)
# l1.pop()
# print(l1)

# t=(10)
# t=(10,)
# print(type(t))

# set2={1,2,3,4}
# set2.add(7,9,6)
# print(set2)

# tuple1=(1,2,3,4)
# for i in tuple1:
#     if i%2==0:
#         print(i)
#         break
# else:
#     print("number")        


# tuple1=(1,2,3,4)
# for i in tuple1:
#     print(i)
# else:
#     print("number") 


# for i in range(1,11):
#     if i==7:
#         continue
#     else:
#         print(i)   


# count=1
# while count<=10:
#     print(count)
#     count+=1
#     if count==7:
#         pass
#     print("hi")
# print("out from loop")        


# phone={
#     "aish": 5245,
#     "pooja":4744,
#     "kirti":4555
# }
# for i in phone:
#     print(i)


# class car:
#     def __init__(self):
#         print("welcome")

# i20=car()        


# class ws:
#     def display(self):
#         print("welcome")

# class iip(ws):
#     def display(self):
#         super().display()
#         print("hello")
# o=iip()
# o.display()                


# f=open('py.txt','w')
# f.write("py is good \n it is easy")
# f.close()

# f=open('py.txt','r')
# for each in f:
#     print(each)


# a=round(4.5)
# b=round(4.576)
# print(a)
# print(b)

