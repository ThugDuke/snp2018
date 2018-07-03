import snp
import pyautogui

def get_position_of_bases():
    print("Please put the mouse at the upper left of game.") 
    input("Press Enter to continue...")   
    x,y = pyautogui.position()
    
    print("Please put the mouse at the lower right of game.")
    input("Press Enter to continue...")
    x1,y1 = pyautogui.position()

    for p in snp.locateAllOnScreen("base.png",threshold=0.95 ,region=(x,y,x1-x,y1-y)):
        print(p[0],p[1])

    
    #return list x

def locate_and_hit(x):
    pass
    #use list x

def main():    
    get_position_of_bases()

if __name__ == "__main__":
    main()
