print(*range(0,20,2))

for i in range(0,10):
    if(i==5):
        continue
    print(i)
print("\n")
for i in range(0,10):
    if(i==5):
        break
    print(i)