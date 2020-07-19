import time
import threading
import socket
from ping3  import ping
mutex = threading.RLock()
ip_address = '192.168.0.1-192.168.0.10'
def scan(n,check_ip):
    try:
        s = socket.socket()
        s.settimeout(0.1)
        if s.connect_ex((check_ip,n)) == 0:
            print("%s的端口%s：open" % (n,check_ip))
            #print(':open')
        else:
            print("%s的端口%s: losed" % (n,check_ip))
        s.close()
    except Exception as e:
        print(e)
def pingIP(inputIp):
    try:
        result = ping(inputIp, timeout=4)
        if result is not None:
            return True
        else:
            return False
    except Exception as ex:
        return False
if __name__ == '__main__':
    lp = [str(x) for x in ip_address.split('-')]
    #IP段的前面三段
    before=[str(x) for x in lp[0].split('.')][0]+'.'+[str(x) for x in lp[0].split('.')][1]+'.'+[str(x) for x in lp[0].split('.')][2]
    #起始IP段最后一位
    start=[int(x) for x in lp[0].split('.')][3]
    end=[int(x) for x in lp[1].split('.')][3]+1
    for i in range(start,end):
        if mutex.acquire(1):    # 加锁 
            ip=before+'.'+str(i)
            if(pingIP(ip)):
                k=ip
                print('%s:开始检查端口!' % ip)
                for j in range(70,81):#几万个端口太多不好测试，暂时用这几个端口进行测试
                    t1 = threading.Thread(target=scan, args=(j,k,))
                    t1.start()
            else:
                print('%s:无法连接!' % ip)
        mutex.release()   #解锁
   
    