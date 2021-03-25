elements=str(input()).lower().split()
legendety_fragments= ["shards","motes","fragments"]
legendary_item=False
materials_items={}
materials_junk={} 
while True:
    for index in range(0,len(elements),2):
        quantity=int(elements[index])
        element=elements[index+1]

        if element in legendety_fragments:
            if element not in materials_items:
                materials_items[element]=quantity
            else:
                materials_items[element]+=quantity
            
        else:
            if element not in materials_junk :
                materials_junk[element]=quantity
            else:
                materials_junk[element]+=quantity
        if "shards" not in materials_items:
            materials_items["shards"]=0
        if "motes" not in materials_items:
            materials_items["motes"]=0
        if "fragments" not in materials_items:
            materials_items["fragments"]=0
        if "shards" in materials_items:
            if materials_items["shards"]>=250:
                materials_items["shards"]-=250
                sorted_items=dict(sorted(materials_items.items(),key=lambda x: (-x[1],x[0])))
                sorted_junks=dict(sorted(materials_junk.items()))
                print(f"Shadowmourne obtained!")
                for x,y in sorted_items.items():
                    print(f"{x}: {y}")
                for x,y in sorted_junks.items():
                        print(f"{x}: {y}")
                legendary_item=True
                break
        if "fragments" in materials_items: 
            if materials_items["fragments"]>=250:
                materials_items["fragments"]-=250
                sorted_items=dict(sorted(materials_items.items(),key=lambda x: (-x[1],x[0])))
                sorted_junks=dict(sorted(materials_junk.items()))
                print(f"Valanyr obtained!")
                for x,y in sorted_items.items():
                    print(f"{x}: {y}")
                for x,y in sorted_junks.items():
                    print(f"{x}: {y}")
                legendary_item=True
                break
        if "motes" in materials_items: 
            if materials_items["motes"]>=250:
                materials_items["motes"]-=250
                sorted_items=dict(sorted(materials_items.items(),key=lambda x: (-x[1],x[0])))
                sorted_junks=dict(sorted(materials_junk.items()))
                print(f"Dragonwrath obtained!")
                
                for x,y in sorted_items.items():
                    print(f"{x}: {y}")
                for x,y in sorted_junks.items():
                        print(f"{x}: {y}")
                legendary_item=True
                break  
    if legendary_item == True:
        break
    elements=str(input()).lower().split()
    


    

    

    
    
    

    


       