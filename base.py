import urllib.request
import re

resultList = []

with urllib.request.urlopen('https://time.com') as response:
    html = response.read().decode('utf-8')

section = re.findall('<section class="homepage-module latest"(.*)\n((.+\n)+(.*)<\/section>)',html)

if(section != None):
    
    for i in section:
        hrefdata = re.findall('(<[Aa]\s(.*)<\/[Aa]>)',i[1])

    for j in hrefdata:
        resultList.append(j[0])
            
finale_result=[]
for x in range(len(resultList)):
    res=resultList[x].replace("<a href=/", "").split('/>')
    dic = {'url': res[0], 'title': res[1].replace('</a>','') }
    finale_result.append(dic)