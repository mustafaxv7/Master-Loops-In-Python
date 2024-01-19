""" This program To Desgin an isosceles Triangle using Stars"""
number_of_lignes = int(input("\nEnter The Number of lignes>>: "))
print("\n")
for i in range(1,number_of_lignes+1):
    for j in range(i,number_of_lignes):
        print("  ",end="")
    for j in range(1,2*i):
        print("* ",end="")
    print("")
print("\n")
