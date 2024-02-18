#regex-findall pattern
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())

else:
    print("pattern not found")
# ====================================================

#regex-match pattern

#import re 
