txt = "Hi Sam!"

x = "Sam"
y = "Utk"

mytable = txt.maketrans(x, y)

print(txt.translate(mytable))
