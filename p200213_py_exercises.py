"""
scratch for
https://w3resource.com/python-exercises/
Basic Part 1 (previously completed: 3-6)

"""

# =============================================================================
# # 7
# # print the extension of a filename input from user. eg: 'myfile.txt' => 'txt'
# print(str(input("Enter filename: ")).rpartition('.')[2])
# =============================================================================

# =============================================================================
# # 8
# # print the first and last colors from the given list
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])
# =============================================================================

# =============================================================================
# # 9
# #print the examination schedule. (extract the date from exam_st_date).
# # given: exam_st_date = (11, 12, 2014)
# # print: The examination will start from : 11 / 12 / 2014
# exam_st_date = (11, 12, 2014)
# # a
# msg_form1 = 'Examination Date: {} / {} / {}'
# print(msg_form1.format(exam_st_date[0], exam_st_date[1], exam_st_date[2]))
# # b
# msg_form2 = 'Examination Date: {m} / {d} / {y}'
# dat_form = dict(zip(['m', 'd', 'y'], exam_st_date))
# print(msg_form2.format(**dat_form))
# =============================================================================

# =============================================================================
# # 10
# # accept an integer (n) and compute the value of n+nn+nnn.
# # Sample value of n is 5
# # Expected Result : 615
# try:
#     n = str(input("Enter integer: "))
#     nn = str(n+n)
#     nnn = str(n+n+n)
#     c = int(n) + int(nn) + int(nnn)
#     print(c)
# except ValueError as err:
#     print("TypeError", err.args)
# =============================================================================
