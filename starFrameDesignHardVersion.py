while True:
    number_of_lignes = int(input("\nEnter The Number of Lignes>>: "))
    if number_of_lignes % 2 != 0:
        break
    else:print("\t\n\nThe Number of Lignes Should be Odd\n\n")
print("\n")
for i in range(1,number_of_lignes+1):
     for j in range(1,number_of_lignes+1):
         if ( i == 1 or i == number_of_lignes or j == 1 or j == number_of_lignes or i == j or j == number_of_lignes - i + 1):
             print("* ",end="")
         else:
             print("  ",end="")
     print("")
print("\n\n")
             
            
        