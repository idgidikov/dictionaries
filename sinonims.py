synonyms= {}
n= int(input())

for _ in range(n):
    word= input()
    synonym = input()
    if word not in synonyms:
        synonyms[word]=[]
    synonyms[word].append(synonym)

[print(f"{word} - {', '.join(synonym)}") for word, synonym in synonyms.items()]