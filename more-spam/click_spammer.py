from time import sleep
import pyautogui as pg 

x=pg.prompt('Clicks do you want to spam?')
y=pg.prompt('How many seconds do u want ur cursor to sleep?')
cnt=0
pg.alert('5s sleep...',title="SET YOUR CURSOR")
sleep(5)
while cnt!=int(x):
    pg.click()
    cnt+=1
    sleep(int(y))

pg.alert("Clicker done its job by clicking for  %s times!"%x)

