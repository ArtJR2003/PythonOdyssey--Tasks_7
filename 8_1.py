# Հայտարարել list,  որը բաղկացած է string-ներից:
# Տպել list-ում եղած ամենաերկար string-ը  և համապատասխան index-ը:

ls = ['hello', 'world', 'continue', 'spam', 'ham', 'eggs', 'expression']
maximum = ls[0]
index = 0
for i in range(len(ls)):
    if len(maximum) < len(ls[i]):
        maximum = ls[i]
        index = i
print(f"The longest string is: {maximum} and it's index is: {index}.")
