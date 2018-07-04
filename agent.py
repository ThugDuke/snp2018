import snp
import pyautogui

def get_position_of_bases():
    print("Please put the mouse at the upper left of game.") 
    input("Press Enter to continue...")   
    x,y = pyautogui.position()
    
    print("Please put the mouse at the lower right of game.")
    input("Press Enter to continue...")
    x1,y1 = pyautogui.position()
    coordinates = []

    for a in snp.locateAllOnScreen("base.png",threshold=0.9 ,region=(x,y,x1-x,y1-y)):
        same_base = 0
        for b in coordinates:
            if abs(b[0]-a[0]) <=6 and abs(b[1]-a[1]) <=6:
                same_base = 1
        if same_base == 0:
            coordinates.append((a[0], a[1]))
        
    return coordinates
    #return list coord
    

def locate_and_hit(x):
    pass
    #use list coord

def main():    
    get_position_of_bases()

if __name__ == "__main__":
    main()
