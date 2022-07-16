import sys

from picamera import PiCamera
from time import sleep
import selfieOptions as opt
from datetime import datetime
import pygame
import io
import pygame.camera

takePicture = False
brightnessTimerSet = False
brightnessCounter = opt.IDDLE_BRIGHTNESS
brightnessTimerDone = False

pictureCountdownTimerSet = False
pictureCountdownCounter = 0

startFlash = False
startFlashTimeStamp = 0

capturedImage = False
capturedImagePy = None

def newPicture():
    global capturedImage, takePicture, brightnessCounter, brightnessTimerDone, brightnessTimerSet, pictureCountdownTimerSet, pictureCountdownCounter, startFlash, startFlashTimeStamp, capturedImagePy
    takePicture = False
    brightnessTimerSet = False
    brightnessCounter = opt.IDDLE_BRIGHTNESS
    brightnessTimerDone = False

    pictureCountdownTimerSet = False
    pictureCountdownCounter = 0

    startFlash = False
    startFlashTimeStamp = 0

    capturedImage = False
    capturedImagePy = None

def pyGameTest():
    global capturedImage, takePicture, brightnessCounter, brightnessTimerDone, brightnessTimerSet, pictureCountdownTimerSet, pictureCountdownCounter, startFlash, startFlashTimeStamp, capturedImagePy
    pygame.init()
    pygame.camera.init()

    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode((opt.SCREEN_X, opt.SCREEN_Y), 0)
    cam_list = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(cam_list[0], (opt.SCREEN_X, opt.SCREEN_Y))
    cam.start()

    cam.set_controls(False, False, opt.IDDLE_BRIGHTNESS)


    while True:
        if not capturedImage:
            image1 = cam.get_image()
        else:
            image1 = capturedImagePy

        image1 = pygame.transform.scale(image1, (opt.SCREEN_X, opt.SCREEN_Y))

        screen.blit(image1, (0, 0))

        if capturedImage:
            buttonWidth = opt.SCREEN_X / 2
            buttonHeight = opt.SCREEN_Y / 6

            GRAY = (150, 150, 150)
            WHITE = (255, 255, 255)

            bottomLeft_x = 0
            bottomLeft_y = opt.SCREEN_Y - buttonHeight
            bottomLeft_x_center = bottomLeft_x + (buttonWidth / 2)
            bottomLeft_y_center = bottomLeft_y + (buttonHeight / 2)

            bottomRight_x = buttonWidth
            bottomRight_y = opt.SCREEN_Y - buttonHeight
            bottomRight_x_center = bottomRight_x + (buttonWidth / 2)
            bottomRight_y_center = bottomLeft_y + (buttonHeight / 2)

            bottomLeftButton = pygame.Rect(bottomLeft_x, bottomLeft_y, buttonWidth, buttonHeight)
            bottomRightButton = pygame.Rect(bottomRight_x, bottomRight_y, buttonWidth, buttonHeight)

            pygame.draw.rect(screen, GRAY, bottomLeftButton)
            pygame.draw.rect(screen, GRAY, bottomRightButton)
            pygame.draw.line(screen, WHITE, (opt.SCREEN_X / 2, opt.SCREEN_Y - buttonHeight), (opt.SCREEN_X / 2, opt.SCREEN_Y), 2)
            pygame.draw.line(screen, WHITE, (0, opt.SCREEN_Y - buttonHeight), (opt.SCREEN_X, opt.SCREEN_Y - buttonHeight), 2)

            font = pygame.font.Font(None, 35)
            text_left = font.render(opt.NEW_PICTURE_TEXT, True, WHITE)
            text_right = font.render(opt.KEEP_PICTURE_TEXT, True, WHITE)

            left_rect = text_left.get_rect(center=(bottomLeft_x_center, bottomLeft_y_center))
            right_rect = text_right.get_rect(center=(bottomRight_x_center, bottomRight_y_center))

            screen.blit(text_left, left_rect)
            screen.blit(text_right, right_rect)

        if not takePicture:
            font = pygame.font.Font(None, 50)
            text = font.render(opt.IDDLE_TEXT, True, (255, 255, 255))
            text_rect = text.get_rect(center=(opt.SCREEN_X / 2, opt.SCREEN_Y / 2))
            screen.blit(text, text_rect)
        else:
            if not brightnessTimerSet:
                pygame.time.set_timer(pygame.USEREVENT, 50)
                brightnessTimerSet = True

            if pictureCountdownTimerSet == False and brightnessTimerDone == True:
                pygame.time.set_timer(pygame.USEREVENT, 1000)
                pictureCountdownTimerSet = True

            font = pygame.font.Font(None, 50)

            if pictureCountdownCounter == 0:
                textToRender = opt.PICTURE_TEXT_BEFORE
            elif pictureCountdownCounter == 1:
                textToRender = opt.PICTURE_TEXT_1
            elif pictureCountdownCounter == 2:
                textToRender = opt.PICTURE_TEXT_2
            elif pictureCountdownCounter == 3:
                textToRender = opt.PICTURE_TEXT_3
            else:
                textToRender = ""
                if not startFlash:
                    cam.set_controls(False, False, opt.FLASH_BRIGHTNESS)
                    startFlash = True
                    startFlashTimeStamp = pygame.time.get_ticks()
                else:
                    if (startFlashTimeStamp + opt.FLASH_DURATION) < pygame.time.get_ticks():
                        cam.set_controls(False, False, opt.PICTURE_BRIGHTNESS)

                        if not capturedImage and (startFlashTimeStamp + opt.FLASH_DURATION + 50) < pygame.time.get_ticks():
                            capturedImagePy = cam.get_image()
                            capturedImage = True

            text = font.render(textToRender, True, (255, 255, 255))
            text_rect = text.get_rect(center=(opt.SCREEN_X / 2, opt.SCREEN_Y / 2))
            screen.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            # Functionality for fading from Iddle Brightness to Picture Brightness
            if event.type == pygame.USEREVENT and brightnessTimerDone == False:
                if brightnessCounter < opt.PICTURE_BRIGHTNESS:
                    brightnessCounter += 1
                    cam.set_controls(False, False, brightnessCounter)
                else:
                    brightnessTimerDone = True

            if event.type == pygame.USEREVENT and brightnessTimerDone == True and pictureCountdownTimerSet == True:
                if pictureCountdownCounter <= 3:
                    pictureCountdownCounter += 1

            # Detect touch screen input
            if event.type == pygame.FINGERDOWN:
                takePicture = True

            if event.type == pygame.KEYDOWN:
                cam.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                cam.stop()
                pygame.quit()
