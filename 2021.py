import time
import itertools
import threading
import sys,time,os
import datetime as dt
os.system('clear')
d = dt.date.today()
print(f"{d}")
print(f"day\t{d:%A}")
def tool(k):
    for c in k + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
def fore():
    tool('This is program by:SAMSUL HADI')
os.system('bash T.sh')

class gua:
    def __init__(self,inputnama,inputhelt,inputpower,inputdmg):
        self.nama = inputnama
        self.power = inputpower
        self.helt = inputhelt
        self.dmg = inputdmg
        # ini contoh
guaa = gua("anonim",10000,"9"*10,10000)
print(guaa.__dict__)

var = "SYSTEM FOUND"
for c in var :
    print(c)
h = 0
while h < 10:
    h += 1
    print(f'system local actif{h}')

done = False

def animate():
    for c in itertools.cycle(['\033[1;91mお\033[1;97m', '\033[1;92mま\033[1;97m', '\033[1;93mえ\033[1;97m', '\033[1;94mら\033[1;97m', '\033[1;94mば\033[1;97m', '\033[1;95mか\033[1;97m', '\033[1;96mや\033[1;97m', '\033[1;97mろ\033[1;97m', '\033[1;98mく\033[1;97m', 'う', 'ず']):
        if done:
            break
        sys.stdout.write('\rkotoba for you. ' + c)
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('')

t = threading.Thread(target=animate)
t.start()

 
time.sleep(10.9)
done = True
print("")
if __name__=='__main__':
    fore()
