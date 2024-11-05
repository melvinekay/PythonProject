#Break Statement
num = 20
while num <= 25:
    print(num)
    #num += 1
    if num == 23:
        break
    num += 1

#Continue Statement
devices = ["Laptop", "Phone", "Tablet", "iPad"]
for x in devices:
    if x == "Phone":
        continue
    print(x)