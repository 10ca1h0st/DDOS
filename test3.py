from bs4 import BeautifulSoup
import urllib2
import zlib
import sys
import re

header={'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Cache-Control': 'max-age=0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Connection': 'keep-alive', 'Referer': 'http://www.kuaidaili.com/', 'Cookie': '_ga=GA1.2.1001650843.1490869637; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490869637,1490941800; _ydclearance=fabca997b180225da017a776-f5af-4b8b-96cd-5a4baff34ec6-1490961984; channelid=0; sid=1490954499688142; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490946679; _gat=1'}

patt=re.compile('/proxylist/\d/')

count=0

page_now=0

ip_list=[]

def getIpAddr(url):
    req=urllib2.Request(url,headers=header)
    page=urllib2.urlopen(req)
    info=page.info()
    if info["Content-Encoding"]=="gzip":
        output=zlib.decompress(page.read(),16+zlib.MAX_WBITS)
    else:
        output=page.read()
    bs=BeautifulSoup(output,'lxml')
    ip_list=bs.select('#listnav > ul > li > a')
    for i in ip_list:
        print i['href']

getIpAddr(sys.argv[1])
