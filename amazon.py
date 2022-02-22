from Browser import *
import traceback
obj=Browser()
try:
    with open("keywords.txt") as f:
        keywords=f.read().split("\n")
    for keyword in keywords:
        for page in range(1,2):
            print("search :",keyword)
            print("page",page)
            obj.start(keyword,page)
except:
    traceback.print_exc()
