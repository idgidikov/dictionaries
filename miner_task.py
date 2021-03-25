data = input()
resorses={}
while data !="stop":
    
    quantity= int(input())
    if data not in resorses:
        resorses[data]=quantity
    else:
        resorses[data]+=quantity
    data = input()

for x,y in resorses.items():
    print(f"{x} -> {y}")
