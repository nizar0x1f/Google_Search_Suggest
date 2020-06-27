import requests
import json
import re

try:
    header = '''
   _____  ____   ____   _____ _      ______    _____                             _   
  / ____|/ __ \ / __ \ / ____| |    |  ____|  / ____|                           | |  
 | |  __| |  | | |  | | |  __| |    | |__    | (___  _   _  __ _  __ _  ___  ___| |_ 
 | | |_ | |  | | |  | | | |_ | |    |  __|    \___ \| | | |/ _` |/ _` |/ _ \/ __| __|
 | |__| | |__| | |__| | |__| | |____| |____   ____) | |_| | (_| | (_| |  __/\__ \ |_ 
  \_____|\____/ \____/ \_____|______|______| |_____/ \__,_|\__, |\__, |\___||___/\__|
     By NIZAR BAMIDA                 SEOAGENCYHQ.COM        __/ | __/ |              
                                                           |___/ |___/               
    
    '''
    print(header)
    elems =[]
    word1=input('Enter you search query  : ')
    #
    #+"%20"+word2+"%20"+word3+
    req_dep0_url = "https://www.google.com:443/complete/search?q="+word1+"&cp=22&client=psy-ab&xssi=t&gs_ri=gws-wiz&hl=en&authuser=0&psi=foz2XtbsHcXggwepoK3IAw.1593216130927"
    req_dep0_cookies = {"CGIC": "CgtmaXJlZm94LWItZCJKdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCwqLyo7cT0wLjg", "1P_JAR": "2020-6-27-0", "NID": "204=i-qOwQDD-69-nNrGyX-G95jluSygvF-LFgSsi8-rlStFlOIOPfJBV2Nht9-oQPyO0-Sy2tDHv0EB-Pg34ajYlwYbVqoOXaF_XyGjRdiq74wIHXbIbH5PxVn-d4iTj_wxuexZbWy6wSzcuw-H7mhx3Mjjev0pHsYTn2EIG28Uwqg", "ANID": "AHWqTUlYw67IBAY73RmHFUgbu1OQzYMnMif1SJqGnfX5o9q2Jh3Z9h-KAnncsBhG"}
    req_dep0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "*/*", "Accept-Language": "en-GB,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.google.com/", "Connection": "close"}
    bb = requests.get(req_dep0_url, headers=req_dep0_headers, cookies=req_dep0_cookies).text
    cc =(bb.encode().decode("unicode-escape").encode().decode("unicode-escape")) 
    ff = cc.replace("<b>","")
    gg = ff.replace('<\\/b>', '')

    hh = gg.split('",0],["')   
    for h in hh:
         cc = [x.strip() for x in re.split(r'(?:(?!")(?:.|\n))*"', h)]
         elems.append(cc)
        
    elems = elems[:-1]   
    for elem in elems:
        print(elem)
except:
    pass
