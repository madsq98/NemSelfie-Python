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

    #pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode((800, 480), 0)
    cam_list = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(cam_list[0], (800, 480))
    cam.start()

    takePicture = False
    while True:
        image1 = cam.get_image()
        image1 = pygame.transform.scale(image1, (800, 480))
        if not takePicture:
            screen.blit(image1, (0, 0))
        else:
            screen.fill((0, 0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                cam.set_controls(False, False, 100)
                takePicture = True

            if event.type == pygame.QUIT:
                cam.stop()
                pygame.quit()
