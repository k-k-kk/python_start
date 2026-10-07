#float带小数点的数字，正式称为浮点数值，使用后可以算小数
x=float(input("what's x?"))
y=float(input("what's y?"))
print(x+y)
#round,四舍五入函数
x=float(input("what's x?"))
y=float(input("what's y?"))
z=round(x+y)
print(z)
#格式化数字，比如在每3位数后加一个逗号
print(f"{z:,}")
#或者
print(format(z,","))
#除法省略2位小数
z=(x/y)
print(z)
print(f"{z:.2f}")
