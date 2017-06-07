from bs4 import BeautifulSoup as bs
import urllib3,requests,re

while True :
    url = "https://felicity.iiit.ac.in/contest/extra/fastandfurious/#"
    resp = requests.get(url)

    bsobj = bs(resp.content,"lxml")

    paras = bsobj.find_all("p")

    nums = re.findall('\((.*?)\)', str(paras[1]))

    ans = eval(nums[0])
    
    payload = {"ques_ans":ans}
    
    presp = requests.post(url,payload)
    print(presp.content)
    print(nums,ans,presp.status_code,paras)
    if presp.status_code != 200 :
        break;
