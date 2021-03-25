data = str(input())
def count_chars(data):
    dict_chars = {}
    for x in data:
        if x ==" ":
            continue
        if x not in dict_chars:
            dict_chars[x]=0
        dict_chars[x]+=1
    return dict_chars
d = count_chars(data)
for x,y in d.items():
    print(f"{x} -> {y}")