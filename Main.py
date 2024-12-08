import CSFMLInit as csfml
import ctypes as cx
from time import sleep
def Main():
    music_play = csfml.CreateFromFile(bytes("ExampleMus.mp3", "utf-8"))
    csfml.SetLoop(music=music_play, isLoop=True)
    csfml.PlayMusic(music=music_play)
    while True:
        sleep(3400)

if __name__ == "__main__":
    Main()