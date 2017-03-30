import urllib2
import zlib
header={'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Cache-Control': 'max-age=0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Connection': 'keep-alive', 'Referer': 'http://www.xicidaili.com/', 'If-None-Match': 'W/"309b50a918abd09a8c87011821da01c1"', 'Cookie': 'Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1490869358;_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWJlMjdiNzRiZmE3MjY5NmQzMWEwYzRlYzQ1NDc4ZDdkBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXdydWxRcmxVZE5ZZk9NbjRuaXNSWWVodVdpMWkrM1RxQWRXS0YyOStQb009BjsARg%3D%3D--2706d0e78d27d3b39720e450882f4a955c65e3c5;Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1490869988'}

url='http://www.xicidaili.com/api'

req=urllib2.Request(url,headers=header)
page=urllib2.urlopen(req)
info=page.info()
#print info
if info["Content-Encoding"]=="gzip":
    output=zlib.decompress(page.read(),16+zlib.MAX_WBITS)
else:
    output=page.read()
fp=open("output.txt","w")
fp.write(output)
fp.close()



# bs.select('div#home > div.main')[0].select("table#ip_list")[0].select("tr.odd")[0].select("td.country")[0].next_sibling.next_sibling

