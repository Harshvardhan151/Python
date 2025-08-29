for i in range(1,17) :
    print("5 * ",i," = ",5*i)
    if(i == 11):
        break
    else:
        continue

# continue to skip an iteration
print("\ntable of 12\n")
for i in range(1,17):
    if(i == 6) :
        break
    else:
        if(i==3):
            print("skipped the iteration")
            continue
        else:
            print("12 * ",i," = ",12*i)

