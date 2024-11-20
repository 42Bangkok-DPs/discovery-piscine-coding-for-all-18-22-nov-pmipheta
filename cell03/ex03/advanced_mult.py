max_table = 10
i=0

while i<=max_table :
    print(f"Table de {i}: ",end="") 

    j=0

    while j <=max_table :

        print(f"{i * j:2} ",end="")

        j+=1

    print()
    i+=1
