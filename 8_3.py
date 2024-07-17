# Հայտարարել list և տպել list-ի էլեմենտները  հակառակ հերթականությամբ: List-ը կարող է պարունակել ցանկացած տիպի էլեմենտ:

ls = [1, 3.14, "hello", "python", (1, 2), {"key": "value"}]
start = -1
end_index = len(ls) - 1
ls2 = []
for i in range(end_index, start, -1):
    ls2.append(ls[i])
for j in ls2:
    print(j, end='    ')