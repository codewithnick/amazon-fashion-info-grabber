from ast import keyword
from Browser import *
import traceback
obj=Browser()
try:
    with open("keywords.txt") as f:
        keywords=f.read().split("\n")
    for i  in range(len(keywords)):
        if i%5==1:
            
            keyword=keywords[i]
            #making keyword to save
            keywordtosave=keyword
            try:
                keywordtosave+= ','+ keywords[i+1]
                keywordtosave+= ','+ keywords[i+2]
                keywordtosave+= ','+ keywords[i+3]
                keywordtosave+= ','+ keywords[i+4]
            except:
                pass
            for page in range(1,2):
                print("search :",keyword)
                print("page",page)
                obj.start(keyword,keywordtosave,page)
except:
    traceback.print_exc()
