def sixsix(n):
    for _ in range(n):
        print("66")

def get_number():
    while True:
        n = int(input("what's n?"))
        if n <= 0:
            continue
        else:
            break
    return n


n = get_number()
sixsix(n)
