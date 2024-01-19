'''This Program Draw  isosceles Triangle '''
number_of_colomnes = int(input('\n\nEnter The Number of Colomnes>>: '))
# print('\n')
# for i in range(1,number_of_colomnes+1):
#     for j in range(1,i+1):
#         print('* ',end='')
#         if j == number_of_colomnes:
#             print('')
#             for i in range(1,number_of_colomnes):
#                 for j in range(number_of_colomnes,i,-1):
#                     print('* ',end='')
#                 print('')
#     print('')
print('\n')   
p = 1
for i in range(1,2*number_of_colomnes):
    for j in range(1,p+1):
        print('* ',end='')
    if i < number_of_colomnes : p = p + 1
    else: p = p - 1
    print('')
    
print('\n') 

    
                   
   
    