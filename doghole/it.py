from socketserver import BaseRequestHandler, UDPServer
import time,os,re

def check_legal(ipAddr):
    flag = ipAddr[0]
    if(flag == ' '):
        return True
    else:
        return False

def check_ip(ipAddr):
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        c_msg = msg.decode('utf-8').strip('\r\n')
        is_legal = check_legal(c_msg)
        if(is_legal):
            c_msg = c_msg[1:]
            is_ip = check_ip(c_msg)
            if(is_ip):
                cmd = "iptables -D INPUT 1"
                os.system(cmd)
                cmd = "iptables -I INPUT -s " + c_msg + " -p tcp --dport 49155 -j ACCEPT"
                print(cmd)
                os.system(cmd)
        sock.sendto(b'fail', self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 55555), TimeHandler)
    serv.serve_forever()
