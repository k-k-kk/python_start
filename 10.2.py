def main():
    x = get_int()
    print(f"x is {x}")



def get_int():
    while True:
        try:
            return int(input("what's x?"))
        except ValueError:
            print("x is not a integer")       #这行改成pass也行


main()  