import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}

# 获取soup的通用函数.
def get_soup(part,params={},data={}):
	req=requests.session()
	r=req.post(domain+part,params=params,data=data,headers=headers)
    return BeautifulSoup(r.text,features='html5lib')
