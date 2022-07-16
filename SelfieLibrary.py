from picamera import PiCamera
from time import sleep
import selfieOptions as opt
from datetime import datetime
import pygame
import io
import pygame.camera

def pyGameTest():
    pygame.init()
    pygame.camera.init()

    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode((opt.SCREEN_X, opt.SCREEN_Y), 0)
    cam_list = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(cam_list[0], (opt.SCREEN_X, opt.SCREEN_Y))
    cam.start()

    cam.set_controls(False, False, opt.IDDLE_BRIGHTNESS)

    takePicture = False
    timerSet = False
    counter = opt.IDDLE_BRIGHTNESS

    while True:
        image1 = cam.get_image()
        image1 = pygame.transform.scale(image1, (opt.SCREEN_X, opt.SCREEN_Y))

        screen.blit(image1, (0, 0))

        if not takePicture:
            font = pygame.font.Font(None, 50)
            text = font.render(opt.IDDLE_TEXT, True, (255, 255, 255))
            text_rect = text.get_rect(center=(opt.SCREEN_X / 2, opt.SCREEN_Y / 2))
            screen.blit(text, text_rect)
        else:
            font = pygame.font.Font(None, 50)
            text = font.render(opt.PICTURE_TEXT_BEFORE, True, (255, 255, 255))
            text_rect = text.get_rect(center=(opt.SCREEN_X / 2, opt.SCREEN_Y / 2))
            screen.blit(text, text_rect)

        if not timerSet & takePicture:
            pygame.time.set_timer(pygame.USEREVENT, 50)
            timerSet = True

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if counter < opt.PICTURE_BRIGHTNESS
                    counter += 1
                    cam.set_controls(False, False, counter)

            if event.type == pygame.FINGERDOWN:
                takePicture = True

            if event.type == pygame.QUIT:
                cam.stop()
                pygame.quit()
