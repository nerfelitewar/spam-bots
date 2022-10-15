from time import sleep
import pyautogui as pg 

x=pg.prompt('CLICK')
cnt=0
pg.alert('5s sleep')
sleep(5)
while cnt!=int(x):
    sleep(0.3)
    pg.click()
    cnt+=1

