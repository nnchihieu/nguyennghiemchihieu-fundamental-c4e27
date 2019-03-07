ls = ["T-shirt", "Sweater"]
while True:
    print("welcom to our shop, what do you want?")
    print("R: Our items")
    print("C: Add new item")
    print("U: Update item")
    print("D: Delete item")
    chosse = input("")
    if chosse == "R":
        print("Our items: ",(ls))
    if chosse == "C":
        new = input("Add new: ")
        ls.append(new)
        print("Our items: ",(ls))
    if chosse == "U":
        p=int(input("Update position?"))
        new = input("Add new: ")
        if p <= len(ls):
            ls[p-1] = new
        else:
            print("Your position isn't exist ")
        print("Our items: ",(ls))
    if chosse == "D":
        p=int(input("Delete position?"))
        if p <= len(ls):
            ls.remove(ls[p-1])
        else:
            print("Your position isn't exist ")
        print("Our Items: ",(ls))

