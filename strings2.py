msg= "Hi %s. How are you?"
name= "mary"
print (msg%name)

msg="Hi %s"
jms = input("enter your name")
print (msg%jms)

msg= "the middle names are %s"
name= input("write the first name")
name1= input ("write the second name")
a= name [4:7]
b= name1 [2:5]
print(msg%a)
print(msg%b)

msg= "the name is %s"
s1= "Aunt"
s2= "Kelly"
a= s1 [:3]
b= s1 [2:4]
name= a+s2+b
print(msg%name)

msg= "the combine of the countries are %s"
s1= "america"
s2= "japan"
a= s1 [:1]
b= s1 [3:4]
c= s1 [6:7]
a1= s2 [:1]
b1= s2 [2:3]
c1= s2 [4:5]
country= a+a1+b+b1+c+c1
print(msg%country)