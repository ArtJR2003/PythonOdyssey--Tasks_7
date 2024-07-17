# Գրեք ծրագիր, որը ամբողջ թվային զանգվածի բոլոր զույգ էլեմենտները կտեղավորի նույն զանգվածի մեջ սկզբից, իսկ կենտերը՝ վերջից:

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls2 = []

for i in ls:
    if i % 2 == 0:
        ls2.append(i)

for i in ls:
    if i % 2 != 0:
        ls2.append(i)
        
print(f"Our original list is: {ls}\nOur updated list is: {ls2}")