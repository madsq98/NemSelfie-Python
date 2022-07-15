from picamera import PiCamera
from time import sleep
import selfieOptions as opt
from datetime import datetime
import pygame
import io

def pyGameTest():
    cam = PiCamera()

    pygame.init()
    screen = pygame.display.set_mode((opt.SCREEN_X, opt.SCREEN_Y))

    rgb = bytearray(cam.resolution[0] * cam.resolution[1] * 3)

    exitFlag = True
    while(exitFlag):
        for event in pygame.event.get():
            if(event.type is pygame.QUIT):
                exitFlag = False

        stream = io.BytesIO
        camera.capture(stream, use_Video_port=True, format='rgb')
        stream.seek(0)
        stream.readinto(rgb)
        stream.close()

        img = pygame.image.frombuffer(rgb[0:(camera.resolution[0] * camera.resolution[1] * 3)], camera.resolution, 'RGB')

        screen.fill(0)
        if img:
            screen.blit(img, (opt.SCREEN_X, opt.SCREEN_Y))

        pygame.display.update()

    cam.close()
    pygame.display.quit()

def showPicture(picture):
    pygame.init()
    white = (255, 255, 255)

    display_surface = pygame.display.set_mode((opt.SCREEN_X, opt.SCREEN_Y))

    pygame.display.set_caption('Image')

    img = pygame.image.load(picture)

    while True:
        display_surface.fill(white)

        display_surface.blit(img, (0, 0))

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()

            pygame.display.update()

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

    dt = datetime.now()
    ts = datetime.timestamp(dt)
    saveLocation = opt.PICTURES_LOCATION + "selfie-" + str(ts) + ".jpg"

    camera.capture(saveLocation)

    camera.annotate_text = opt.PICTURE_TEXT_AFTER

    camera.stop_preview()
    showPicture(saveLocation)
    sleep(3)

    camera.annotate_text = ""

    for i in range(opt.PICTURE_BRIGHTNESS)[::-1]:
        camera.brightness = i
        sleep(0.03)

    startSelfie(camera)