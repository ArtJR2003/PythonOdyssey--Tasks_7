# Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում:

ls = ["hello", "world", "hello", "python", "hello", "world", "chlp"]
print(f"Our original string is: {ls}")
index = 0
for i in range(len(ls)):
    count = 0
    index += 1
    for j in range(len(ls)):
        if id(ls[i]) == id(ls[j]):
            count += 1
    print(f"Our {index} word is: {ls[i]} ====== Our word's count is: {count}")
