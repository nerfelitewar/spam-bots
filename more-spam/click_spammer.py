from time import sleep
import pyautogui as pg 

x=pg.prompt('Clicks do you want to spam?')
cnt=0
pg.alert('5s sleep...',title="SET YOUR CURSOR")
sleep(5)
while cnt!=int(x):
    pg.click()
    cnt+=1

pg.alert("Clicker done its job by clicking for  %s times!"%x)

