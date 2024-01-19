# program that draw triangle using stars
number_of_lines = int(input("\n\nNumber of Lines >>: "))
# print("\n")
# for i in range(1,number_of_lines+1):
#     print(" *" * i)
print("\n")

# This a second possible solution might be also right

for i in range(1,number_of_lines + 1):
    for j in range(i):
        print("* ",end="")
    print("")
print("\n")
   

