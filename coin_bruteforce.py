string = '52138387125317'
mylist = "abcdefghijklmnopqrstuvwxyz"
combos = []
keyword = "prize"

for x in range(len(mylist)):
    astring = string.replace("1", mylist[x])
    for y in range(len(mylist)):
        bstring = astring.replace("2", mylist[y])
        for z in range(len(mylist)):
            cstring = bstring.replace("3", mylist[z])
            for a in range(len(mylist)):
                dstring = cstring.replace("5", mylist[a])
                for b in range(len(mylist)):
                    estring = dstring.replace("7", mylist[b])
                    for c in range(len(mylist)):
                        fstring = estring.replace("8", mylist[c])
                        if keyword in fstring:
                            combos.append(fstring)


f = open("sot.txt", 'w')
for x in combos:
    f.write(x + '\n')
f.close()
