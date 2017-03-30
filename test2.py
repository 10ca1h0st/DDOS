from bs4 import BeautifulSoup
import struct
fp=open("xicidaili.htm",'r')
html=fp.read()
fp.close()
bs=BeautifulSoup(html,'lxml')
count=0
#for ip in bs.find_all('tr',class_='odd')[0].find('td',class_='country').next_sibling

for tr_odd in bs.find_all('tr',class_='odd'):
    tr_none=tr_odd.next_sibling.next_sibling
    print tr_odd.find('td',class_='country').next_sibling.next_sibling.string
    print tr_none.find('td',class_='country').next_sibling.next_sibling.string
    count+=2
print 'ip address counts '+str(count)