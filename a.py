while(1):
    x = 900
    y = 530
    for i in range(3):
        p = snp.locateCenterOnScreen('yoyo.png', region=(x, y, 100, 85))
        if p != None:
            pyautogui.click(p[0], p[1])
           # pyautogui.moveTo(1200,580)
        x = x + 100

    x = 843
    y = 617
    for i in range(4):
        p = snp.locateCenterOnScreen('yoyo.png',  region=(x, y, 100, 85))
        if p != None:
            pyautogui.click(p[0], p[1])
           # pyautogui.moveTo(1300, 667)
        x = x + 100

    x = 900
    y = 710
    for i in range(3):
        p = snp.locateCenterOnScreen('yoyo.png',  region=(x, y, 100, 85))
        if p != None:
            pyautogui.click(p[0], p[1])
            #pyautogui.moveTo(1200, 760)
        x = x + 100
