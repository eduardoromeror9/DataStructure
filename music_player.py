from random import randint # Generar numeros aleatorios
from node_based_queue import Queue # clase Queue
from time import sleep # simular el tiempo

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 6)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"count: {self.count}")
        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.title}.")

            sleep(current_track_node.length)

track1 = Track("Salsa")
track2 = Track("Reggaeton")
track3 = Track("Merengue")
track4 = Track("Rock")
track5 = Track("Pop")

""" print(track1.length)
print(track2.length)
print(track3.length) """

media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()