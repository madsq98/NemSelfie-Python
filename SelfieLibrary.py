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

    screen = pygame.display.set_mode((640, 480), 0)
    cam_list = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(cam_list[0], (32, 24))
    cam.start()

    while True:
        image1 = cam.get_image()
        image1 = pygame.transform.scale(image1, (640, 480))
        screen.blit(image1, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cam.stop()
            pygame.quit()
