from bs4 import BeautifulSoup
import urllib2
import zlib
import sys
import re

base_url=''
header={}
count=0
ip_list=[]

def getHeader(filename):
    fp=open(filename,'r')
    for eachline in fp:
        if(len(eachline)>1):
            name,value=eachline[:-1].split('=',1)
            header[name]=value
    fp.close()

def getIpAddr(url):
    global count,base_url
    req=urllib2.Request(url,headers=header)
    page=urllib2.urlopen(req)
    info=page.info()
    try:
        if info["Content-Encoding"]=="gzip":
            output=zlib.decompress(page.read(),16+zlib.MAX_WBITS)
        else:
            output=page.read()
    except KeyError:
        return
    bs=BeautifulSoup(output,'lxml')
    ip_list.extend(bs.find_all(attrs={'data-title':'IP'}))
    page_now=bs.select('#listnav > ul > li > a.active')[0]
    if(type(page_now.parent.next_sibling.contents[0])!=type(bs.title.string)):
        page_next=page_now.parent.next_sibling.contents[0]['href']
        getIpAddr(base_url+page_next)
    '''
    count-=1
    if(count>0):
        page_next=page_now.parent.next_sibling.contents[0]['href']
        getIpAddr(base_url+page_next)
    '''

def getBaseUrl(arg):
    global base_url
    base_url=arg.split('//')[0]+'//'+arg.split('//')[1].split('/',1)[0]

def startDdos():
    pass



if __name__=='__main__':
    getHeader(sys.argv[1])
    getBaseUrl(sys.argv[2])
    getIpAddr(sys.argv[2])
    
    for ip in ip_list:
        print ip.string

    print len(ip_list)
   
    
