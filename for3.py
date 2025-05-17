for a in range(1,11):
    #if a>5 : break
    if a % 2 == 0 : continue
    for b in range(1,11):
        if b%2==1 : continue
        print(f"{a} x {b} = {a*b}")
    print()