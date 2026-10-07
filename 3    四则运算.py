x=166
y=4
z=x+y
#引号""会使其中的变量，函数之类的变成字符串，失去原来的效果
print("z")
print(z)
x=input("what's x?")
y=input("what's y?")
z=x+y
print(z)
print("何意味？")
#键盘输入的是字符串，若想要数字还是数字，需要另一个函数,that is INT
z=int(x)+int(y)
print(z)
#不用z也行，并使用嵌套函数
x=int(input("what's x?"))
y=int(input("what's y?"))
print(x+y)
#超级大勾使
print(int(input("what's x?"))+int(input("what's y?")))
#因此，注意简洁性