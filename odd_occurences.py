words = input().split()
def dictionary(data):
    dictionary = {}

    for word in words:
        word_lower = word.lower()
        if word_lower  in dictionary:
            dictionary[word_lower]+=1
            continue
        dictionary[word_lower]=1
    return dictionary
dictionary=dictionary(words)
for key,value in dictionary.items():
    if value % 2 != 0:
        print(key,end=" ")