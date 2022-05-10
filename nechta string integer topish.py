# son = '0123456789'
# count = 0
# harflar = 0
# email = input('kiriting')
# if email[0] == '@':
#     print(False)
# elif email[1] == '@':
#     print(False)
# elif email[0] == '.':
#     print(False)
# elif email[1] == '.':
#     print(False)
# else:
#     for i in email:
#         if '@' and '.' == i:
#             if i == son[0]:
#                 count+=1
#             elif i == son[1]:
#                 count+=1
#             elif i == son[2]:
#                 count += 1
#             elif i == son[3]:
#                 count += 1
#             elif i == son[4]:
#                 count += 1
#             elif i == son[5]:
#                 count += 1
#             elif i == son[6]:
#                 count += 1
#             elif i == son[7]:
#                 count += 1
#             elif i == son[8]:
#                 count += 1
#             elif i == son[9]:
#                 count += 1
#             elif i == '@':
#                 print('')
#             elif i == '.':
#                 print('')
#             elif i != son:
#                 harflar+=1
#             else:
#                 print(False)
# print(f'bu emailda {count} son va {harflar} harf mavjud mavjud')


#
son = '0123456789'
count = 0
harflar = 0
email = input('kiriting')
if email[0] == '@' or email[1] == '@':
    print(False)
elif email[0] == '.' or email[1] == '.':
    print(False)
else:
    for i in email:
        if '@' and '.' in email:
                if i == son[0] or i == son[1] or i == son[2] or i == son[3] or i == son[4] or i == son[5] or i == son[6] or i == son[7] or i == son[8] or i == son[9]:
                    count += 1
                elif i == '@' or i == '.':
                    print('')
                elif i != son:
                    harflar+=1
    else:
        print(False)
print(f'bu emailda {count} son va {harflar} harf mavjud mavjud')
