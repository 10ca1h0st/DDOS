from bs4 import BeautifulSoup
import urllib2
import zlib
import sys

header={'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Cache-Control': 'max-age=0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Connection': 'keep-alive', 'Referer': 'http://www.kuaidaili.com/', 'Cookie': '_ga=GA1.2.1001650843.1490869637; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490869637,1490941800;_ydclearance=3849e999e7a92c8fb3caf93f-460e-495e-8a5f-f205ffc93d3e-1490948994; channelid=0;sid=1490941484998609; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1490941800'}

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
    '''
    fp=open("output.txt","w")
    fp.write(output)
    fp.close()
    '''

def getIpAddr(html):
    '''
    bs=BeautifulSoup(html,'lxml')
    count=0
    for tr_odd in bs.find_all('tr',class_='odd'):
        tr_none=tr_odd.next_sibling.next_sibling
        print tr_odd.find('td',class_='country').next_sibling.next_sibling.string
        print tr_none.find('td',class_='country').next_sibling.next_sibling.string
        count+=2
    print 'ip address counts '+str(count)
    '''



def startDdos():
    pass



if __name__=='__main__':
    #getHtml(sys.argv[1])
    html=getHtml(sys.argv[1])
    #getIpAddr(html)

