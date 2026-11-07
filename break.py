for i in range(1, 51):
    if(i == 21):
        break
    if (i % 3 == 0):
            print(i)
print ("out of loop")

# contine it will skip the specific number 
for i in range(1, 51):
    if(i == 21):
        continue
    if (i % 3 == 0):
            print(i)
print ("out of loop")