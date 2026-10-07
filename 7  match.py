name = input("what's youe name?")

match name:
    case "kk" | "xky":
        print("武大")
    case "llp":
        print("华科")
    case _:    #在此处，_用于表示其他一切未被考虑的case
        print("who?")