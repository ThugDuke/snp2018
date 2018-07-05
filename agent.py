import snp
import pyautogui

def get_position_of_game():
    print("Please put the mouse at the upper left of game.")
    input("Press Enter to continue...")
    x, y = pyautogui.position()

    print("Please put the mouse at the lower right of game.")
    input("Press Enter to continue...")
    x1, y1 = pyautogui.position()
    w, h = x1-x, y1-y

    return x,y,w,h

def get_position_of_bases(left,top,w,h):    
    coordinates = []

    for a in snp.locateAllOnScreen("base.png",threshold=0.9 ,region=(left,top,w,h)):
        same_base = 0
        for b in coordinates:
            if abs(b[0]-a[0]) <=6 and abs(b[1]-a[1]) <=6:
                same_base = 1
        if same_base == 0:
            coordinates.append((a[0], a[1], a[2], a[3]))
            #(left,top,w,h)
        
    return coordinates
    

def locate_moles_and_hit(coord_of_bases):
    for i in coord_of_bases:
        p = snp.locateCenterOnScreen('mole.png',  threshold=0.87 ,region=(i[0]-10, i[1]+i[3]-120, 150, 130))
        # i,region = (left,top,w,h)
        # mole.png = 133*113
        if p != None:
            pyautogui.click(p[0], p[1])    
    

def main():    
    x,y,w,h = get_position_of_game()
    bases = get_position_of_bases(x,y,w,h)
 
    if len(bases) != 10:
        print("Can't find all 10 bases, please try again.")
        main()
    else:
        while(1):
            locate_moles_and_hit(bases)    

if __name__ == "__main__":
    main()
