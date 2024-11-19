max_table = 10
i=0
#outer loop for loop
while i<=max_table :
    print(f"Table de {i}: ",end="") 

    j=0
    #inner for loop coloumn
    while j <=max_table :

        print(f"{i * j:2} ",end="")

        j+=1

    print() # newline
    i+=1
