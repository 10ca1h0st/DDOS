from bs4 import BeautifulSoup
import urllib2
import zlib
import sys

header={}
ip_list=[]

def getHeader(filename):
    fp=open(filename,'r')
    for eachline in fp:
        if(len(eachline)>1):
            name,value=eachline[:-1].split('=',1)
            header[name]=value
    
    fp.close()

def getHtml(url):
    req=urllib2.Request(url,headers=header)
    page=urllib2.urlopen(req)
    info=page.info()
    #print info
    if info["Content-Encoding"]=="gzip":
        output=zlib.decompress(page.read(),16+zlib.MAX_WBITS)
    else:
        output=page.read()
    return output

def getIpAddr(html):
    bs=BeautifulSoup(html,'lxml')
    #count=0
    for tr_odd in bs.find_all('tr',class_='odd'):
        tr_none=tr_odd.next_sibling.next_sibling
        ip_list.append(tr_odd.find('td',class_='country').next_sibling.next_sibling.string)
        ip_list.append(tr_none.find('td',class_='country').next_sibling.next_sibling.string)
        #count+=2
    #print 'ip address counts '+str(count)
    return ip_list



def startDdos():
    pass



if __name__=='__main__':
    getHeader(sys.argv[1])
    html=getHtml(sys.argv[2])
    getIpAddr(html)

