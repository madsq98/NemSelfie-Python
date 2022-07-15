from picamera import PiCamera
from time import sleep
import selfieOptions as opt

def startCamera():
    camera = PiCamera()

    return camera

def startSelfie(camera):
    for i in range(opt.IDDLE_BRIGHTNESS):
        camera.brightness = i
        sleep(0.03)

    camera.annotate_text = opt.IDDLE_TEXT

def takeSelfie(camera):
    camera.annotate_text = opt.PICTURE_TEXT_BEFORE

    for i in range(opt.PICTURE_BRIGHTNESS):
        camera.brightness = i
        sleep(0.03)

    camera.annotate_text = opt.PICTURE_TEXT_1
    sleep(1)

    camera.annotate_text = opt.PICTURE_TEXT_2
    sleep(1)

    camera.annotate_text = opt.PICTURE_TEXT_3
    sleep(1)

    camera.brightness = opt.FLASH_BRIGHTNESS
    sleep(0.2)

    camera.brightness = opt.PICTURE_BRIGHTNESS
    camera.annotate_text = ""
    camera.capture('test-selfie.jpg')

    camera.annotate_text = opt.PICTURE_TEXT_AFTER
    sleep(3)

    camera.annotate_text = ""

    for i in range(opt.PICTURE_BRIGHTNESS)[::-1]:
        camera.brightness = i
        sleep(0.03)

    startSelfie(camera)