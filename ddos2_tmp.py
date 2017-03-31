from bs4 import BeautifulSoup
import urllib2
import zlib
import sys
import re

header={}

def getHeader():
    fp=open('header_kuaidaili.txt','r')
    for eachline in fp:
        if(len(eachline)>1):
            name,value=eachline[:-1].split('=',1)
            header[name]=value
    
    fp.close()

def getIpAddr(url):
    req=urllib2.Request(url,headers=header)
    page=urllib2.urlopen(req)
    info=page.info()
    if info["Content-Encoding"]=="gzip":
        output=zlib.decompress(page.read(),16+zlib.MAX_WBITS)
    else:
        output=page.read()
    '''
    bs=BeautifulSoup(output,'lxml')
    ip_list.extend(bs.find_all(attrs={'data-title':'IP'}))
    for ip in ip_list:
        count+=1
    '''
    fp=open('output.txt','w')
    fp.write(output)
    fp.close()



def loop(url):
    getIpAddr(url)





if __name__=='__main__':
    getHeader()
    loop(sys.argv[1])
