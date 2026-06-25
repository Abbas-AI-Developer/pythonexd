x=10;

print(x)

name="abbas"
age=26
is_male=True
height=5.8

print(name,age,is_male, height)

user_name="abbas"

# wrong declaration 
# user-name="ali"
# 1name
# class
# @abbas


# print(type(age))
# print(str(age))
# num ="100"
# print(int(num))
# print(type(num))

# num=int(num)

# print(type(num))


# a,b=10,5
# a,b=b,a
# print(a,b)


# x=[1,2]
# y=x
# y.append(3)

# print(x)


x=10

def value():
    x=100
    print(x)

value()    
print(x)

x=10

def value():
     global x
     x=100
     print(x)

value()    
print(x)
print(id(x))

