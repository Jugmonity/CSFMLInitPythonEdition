import ctypes
import os
def Init():
    return ctypes.cdll.LoadLibrary("{}".format(os.getcwd() + "\\DLLCSFML\\csfml-audio-2.dll"))

def CreateFromFile(filename : str) -> ctypes.c_int32:
    return Init().sfMusic_createFromFile(filename)

def PlayMusic(music : ctypes.c_int32):
    return Init().sfMusic_play(music)

def SetLoop(music: ctypes.c_int32, isLoop : bool):
    return Init().sfMusic_setLoop(music, isLoop)