#Matt Andrew F. Solatan
#duplicates

def duplicate ():
    Matt = input ("ENTER NUMBERS:")
    Matt = list (Matt)
    matty = []

    for i in Matt:
        if i not in matty:
            matty.append(i)

    print matty
duplicate()
