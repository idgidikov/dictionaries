
a={"shards":250}
b={"shards":255}
diffKeys = set(a.keys()) - set(b.keys())
c = dict()
for key in diffKeys:
  c[key] = a.get(key)

print(diffKeys)
print(c)

