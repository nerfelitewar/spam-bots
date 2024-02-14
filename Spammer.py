"""
REQUIREMENTS ||
--------------
Python 3 or higher
Install- pip install pg
         pip install time        

"""

import pyautogui as pg
import time


spamNum=pg.prompt('How many messages you want to send?', title='HOW MUCH SPAM NUMBER')
spamNum=int(spamNum)
text=pg.prompt('What you want to send? Type below', title='MESSAGE')

relaxTime=pg.prompt('How much relaxation time you want to set?',title='TIME FREEZE',default=0)
relaxTime=int(relaxTime)
showNo=pg.confirm('Do you want to show number?',title='SHOW NUMBER OF SPAM', buttons=['YES','NO'])


a=pg.confirm(text='Want to start the spam!', title='SPAM DISCORD!', buttons=['OK', 'Cancel'])
if a=='Cancel':
    pg.alert('Code execution stopped')
    exit()
else:
    pass

pg.alert(text='SET UR CURSOR! FOR SPAM IN 5 SECONDS!', title='WARNING')
time.sleep(5)
count=0
pg.click()
for i in range(spamNum):
    if showNo=='YES':
        i+=1
        x=str(i) 
        pg.typewrite(x+'. '+text)
        
        pg.typewrite('\n')

    else:
        pg.typewrite(text)
        pg.typewrite('\n')
    time.sleep(relaxTime)
    if count==spamNum//2:
        pg.alert('Relaxing for 3 sec to avoid timeout.',title='RELAXING')
        time.sleep(3)
    else:
        pass
    count=count+1
    pg.press('Enter')

pg.alert('SPAM DONE!')
exit()

