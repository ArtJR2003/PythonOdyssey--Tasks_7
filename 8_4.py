# Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list:
# Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։

ls = list(range(1, 100 + 1))
print(f"Your list is: {ls}")
number = int(input("Enter your number: "))
for i in ls:
    if number in ls:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
