import re

with open("C:\LULU\KEGG\KEGG_anno.txt") as f:
    str = f.read()
res1= r'<b>(.*?)</b>'
level1 = re.findall(res1,str)
# with open('C:\LULU\KEGG\level1.txt','w') as class1:
#     for item in level1:
#         class1.write(item)
#         class1.write('\n')
#         print(item,'')
print(level1)