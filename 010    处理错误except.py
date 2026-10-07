try:
    x = int(input("what's x?"))
    print(f"x is {x}")
except ValueError:
    print("The x you input is not a integer")
#不建议直接捕获所有错误，因为这样你会不知道错误出在哪了
