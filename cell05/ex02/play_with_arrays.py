original_array=[2, 8, 9, 48, 8, 22, -12, 2]
new_array=[]

for i in range(len(original_array)):
    x=original_array[i]+2
    if x>5 :
        new_array.append(x)

print(original_array)
print(new_array)