from pynput.mouse import Listener
import SelfieLibrary

cam = SelfieLibrary.startCamera()

def on_move(x, y):
    SelfieLibrary.startSelfie(cam)

def on_click(x, y, button, pressed):
    SelfieLibrary.startSelfie(cam)

cam.start_preview()

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()