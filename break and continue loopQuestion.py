# write that code which accept only above 100 no

while(True):
    no = int(input("Enter Number\n"))
    if no > 100:
        print("Congrate you have entered no which is greater than 100\n")
        break

    else:
        print("Enter Again\n")
        continue