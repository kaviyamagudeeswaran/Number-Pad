key_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in key_pad:
    for key in row:
        print(key,end="")
    print()
