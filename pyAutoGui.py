import pyautogui as pag

w,h=pag.size()

changeW=w/1920
changeH=h/1080

pag.moveTo(222*changeW,1059*changeH,0)
pag.click()

pag.hotkey('ctrl','t')
pag.PAUSE=1

'''
pag.keyDown('shift')
pag.keyUp('shift')
'''

pag.moveTo(312*changeW,52*changeH,0)
pag.click()
pag.write('https://www.youtube.com/')
pag.press('enter')


