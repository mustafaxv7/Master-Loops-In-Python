number_of_lignes = int(input("\nEnter The Number of Lignes>>: "))
print("\n\n")
for i in range(1,number_of_lignes+1):
    for j in range(1,number_of_lignes-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")
print("\n\n")