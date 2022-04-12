from calendar import c
import pygame, sys, os

"""

--- Senex Module for Pygame ---

"""


"""DELAY IN PYGAME"""

FPS = 30
clock = pygame.time.Clock()

class Delay():
    def __init__(self, sec, event):
        self.__FPS = sec[1]
        self.__min = 0 
        self.__max = sec[0] * self.__FPS
        self.__increment = 1
        self.__function = event
        self.__flag = True

    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                self.__function()
                self.__flag = False

    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

        #print(int(self.__min))

    def Infinite(self):
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/self.__FPS[1], self.__max/self.__FPS, self.__function))


class Delay_noEvent():
    def __init__(self, sec):
        self.__FPS = sec[1]
        self.__min = 0 
        self.__max = sec[0] * self.__FPS
        self.__increment = 1
        self.__flag = True

    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                self.__flag = False
                return True

        return False

    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    def Infinite(self):
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/self.__FPS, self.__max/self.__FPS, self.__function))


class DO():
    def __init__(self):
        self.__flagOnce = True

    def Once(self, event):
        if self.__flagOnce:
            self.__flagOnce = False
            event()
            


def MiaFunzione():
    print("Ciao")

def testa():
    Do = DO()
    while True:


        #delay.ActualState()
        Do.Once(MiaFunzione)

        clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    testa()