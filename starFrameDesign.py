number_of_lignes = int(input("\nEnter The Number of Lignes>>: "))
number_of_colomnes = int(input("\nEnter The Number of Columnes>>: "))
print("\n")
for i in range(1,number_of_lignes+1):
    for j in range(1,number_of_colomnes+1):
        if ((i == 1 or i == number_of_lignes) or (j == 1 or j == number_of_colomnes)):
            print("* ",end="")
        else:
            print("  ",end="")
    print("")
    
print("\n")
