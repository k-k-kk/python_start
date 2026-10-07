print("hello,'friend'")
print("hello,\"friend\"")
#最好方法？？
name=input("What's your name?")
print("hello,name")
print(f"hello,{name}")
#remove whitespace from str
name=name.strip()
print(f"hello,{name}")
#Capitalize the user's name
name=name.capitalize()
print("hello,"+name)
#进行标题式的大写
name=name.title()
print("hello",name)