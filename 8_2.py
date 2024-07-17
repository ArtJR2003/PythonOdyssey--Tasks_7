# Հայտարարել list,  որը բաղկացած է string-ներից:
# List-ում եղած բոլոր string-ների առաջին տառը դարձնել մեծատառ:
# Տպել յուրաքանչյուրի առաջին տառը

ls = ['hello', 'world', 'continue', 'spam', 'ham', 'eggs', 'expression']
ls2 = []
for i in range(len(ls)):
    upper = ord(ls[i][0]) - 32
    ls2.append(chr(upper))
print(ls2)
