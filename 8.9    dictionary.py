pigs = {
    "cwj":"ncu",
    "jz":"ntu",
    "xxd":"ncu"
    }

print(pigs["jz"],pigs["xxd"],pigs["cwj"],sep="\n")
for pig in pigs:
    print(pig,pigs[pig],sep=" is from ")