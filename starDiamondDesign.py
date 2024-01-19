""" This Program to Design a Diamond on the secreen using stars"""
number_of_lignes = int(input("\nEnter The Number of Lignes>>: "))
print("\n")
for i in range(1,number_of_lignes+1):
    for j in range(i,number_of_lignes):
        print("  ",end="")
    for j in range(1,number_of_lignes+1):
        print("* ",end="")
    print("")
print("\n")
