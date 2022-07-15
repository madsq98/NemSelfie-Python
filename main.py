from pynput.mouse import Listener
import SelfieLibrary

cam = SelfieLibrary.startCamera()

def on_move(x, y):
    SelfieLibrary.doSelfie(cam)

def on_click(x, y, button, pressed):
    SelfieLibrary.doSelfie(cam)

def init():
    cam.start_preview()

    SelfieLibrary.startSelfie(cam)

    with Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()