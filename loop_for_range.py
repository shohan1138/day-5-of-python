total=0
# for number in range (1,101,3):
# for number in range (1,101):
#     total +=number
#     print(number)
# print (total)

even_total=0
for number in range (2,101,2):
    total +=number
    # print(number)
print (total)

even_total_2=0
for number in range (1,101):
    if number%2==0:
        even_total_2 +=number  
        # print(number)
print (even_total_2)
