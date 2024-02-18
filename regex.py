# #regex-findall pattern
# import re

# text = "The quick brown fox"
# pattern = r"brown"

# search = re.search(pattern, text)
# if search:
#     print("Pattern found:", search.group())
# else:
#     print("pattern not found")
# ====================================================
# #regex-match pattern
# import re 
# text = "The quick brown fox"
# pattern = r"brown"

# match = re.match(text,pattern)
# if match:
#     print("Match found",match.group())
# else:
#     print("Match not found")

# ========================================================

# #regex-replace

# line= "this is my brown fox"
# word= "is"
# replacement = "your"

# replace= re.sub(pattern,replacement,word)
# print("Word",replace)

# =========================================

# # to find word in a line

# line = "Hello Python"
# word= "Python"

# result = re.search(line,word)
# if result:
#     print("Word found",search.group())
# else:
#     print("Word isn't found")
# ==============================================

# # split the line

# import re
# text = "apple,mango,orange,banana"
# pattern= r","

# split_result= re.split(pattern,text)
# print("Split",split_result)

# # =================================================