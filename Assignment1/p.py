from http import server
import os

print(os.getcwd())
os.chdir("temp")
print(os.getcwd())
newfi = open("hello.txt",'w')
newfi.write("this is hwllo world")
print("done")

# # current_working_directory = os.getcwd()
# # current_working_directory = current_working_directory + "\SERVER_FOLDER"+ "\\a.txt"
# # # print(current_working_directory)
# # new_file = open(current_working_directory,'w')
# # new_file.write("hi chirag ofdklf")
# # new_file.close()
# # s = "\\"
# # print(s)

# # 0 -48 to  9-57
# # A - 65 to Z = 90
# # a - 97 to z - 122




# from cgi import print_arguments


# a = "abcdxyz()- AR_+TZ 012789-^%"

# def substituteEncription(a):
#     ans = ""

#     for i in range(len(a)):
#         asciiValue = ord(a[i]) 
#         if asciiValue >=48 and asciiValue <= 57:
#             ans = ans + chr(48 + (asciiValue - 48 + 2)%10)
#         elif asciiValue >=65 and asciiValue <= 90:
#             ans = ans + chr(65 + (asciiValue - 65 + 2)%26)
#         elif asciiValue >=97 and asciiValue <= 122:
#             ans = ans + chr(97 + (asciiValue - 97 + 2)%26)
#         else:
#             ans = ans + a[i]
#     return ans
# def substituteDecription(a):
#     ans = ""
#     for i in range(len(a)):
#         asciiValue = ord(a[i])

#         if asciiValue >=48 and asciiValue <= 57:
#             ans = ans + chr(48 + (asciiValue - 48 - 2)%10)
#         elif asciiValue >=65 and asciiValue <= 90:
#             ans = ans + chr(65 + (asciiValue - 65 - 2)%26)
#         elif asciiValue >=97 and asciiValue <= 122:
#             ans = ans + chr(97 + (asciiValue - 97 - 2)%26)
#         else:
#             ans = ans + a[i]
#     return ans

# def transposeEncryption(a):
#     tempList = a.split()
#     print(tempList)
#     for i in range(len(tempList)):
#         tempList[i] = tempList[i][::-1]
#     st = ' '.join(tempList)
#     return st
# def transposeDecryption(a):
#     tempList = a.split()
#     print(tempList)
#     for i in range(len(tempList)):
#         tempList[i] = tempList[i][::-1]
#     st = ' '.join(tempList)
#     return st



# # a = "190"
# # print(ord(a[2]))
# # # for i in range(len(a)):
# # #     asciiValue = ord(a[i]) 
# # #     if asciiValue >=48 and asciiValue <= 57:
# # #         a[i] = chr(48 + (asciiValue + 2)%10)

# # a[0] = 'a'
# # print(a)
# # print(a)
# # ans = substituteEncription(a)
# # print(ans)
# # print(substituteDecription(ans))

# # print(a)
# # ans = transposeEncryption(a)
# # print(ans)
# # print(transposeDecryption(ans))

# print('a' == 'A')