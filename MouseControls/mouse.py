from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()

# current posistion of mouse GET
# mouse.posistion

#Move mouse to a spcific location instantly
# mouse.position = (200,200)
def cont_print():
    while(1):
        print(mouse.position)
        sleep(0.1)

def mouse_scroll(RL,UD):
    mouse.scroll(RL, UD)

def mouse_press(button):
    if(button=='LEFT'):
        mouse.press(Button.left)
    elif(button=='RIGHT'):
        mouse.press(Button.right)

def mouse_release(button):
    if(button=='LEFT'):
        mouse.release(Button.left)
    elif(button=='RIGHT'):
        mouse.release(Button.right)

def mouse_move(x_pos,y_pos):
    mouse.position = (x_pos,y_pos)

def mouse_click(button, times):
    if(button=='LEFT'):
        mouse.click(Button.left, times)
    elif(button=='RIGHT'):
        mouse.click(Button.right, times)




if __name__ == '__main__':
    print('Running as Main')

    # mouse_move(767,431)
    # cont_print()

    # mouse_move(961,845)
    # mouse_click('LEFT', 1)
    # sleep(2)
    # mouse_move(888, 257)
    # mouse_click('LEFT', 1)
    # sleep(2)
    #
    # mouse_scroll(0, 100)
