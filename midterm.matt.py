#Matt Andrew F. Solatan
def remove_duplicate(value):
    output = []
    seen = set()
    for value in a:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
a = input("1st Input: ")
b = input("2nd Input: ")
c = input("3rd Input: ")
result = remove_duplicate(a)
print result
