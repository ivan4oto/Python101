import time


class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration


    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.duration)

    def __eq__(self, other):
        return self.title, self.artist == other.title, other.artist

    def __hash__(self):
        return hash(self.title, self.artist, self.album, self.duration)

    def length(self, seconds=False, minutes=False, hours=False):
        splitduration = (self.duration).split(':')

        minutes = 0
        seconds = 0
        hours = 0

        if len(splitduration) == 2:
            minutes = int(splitduration[0])
            seconds = int(splitduration[1])
        

        if seconds:
            seconds = seconds + (minutes*60) + (hours*3600)
            return seconds


class Playlist:

    def __init__(self, name = '', repeat = False, shuffle = False):
        self.name = name
        self.data = []
        

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __iter__(self):
        return(x for x in self.data)

    def add_song(self, asong):
        self.data.append(asong)

    def remove_song(self, asong):
        if asong in self.data:
            self.data.remove(asong)
        else:
            raise IndexError('Song not in playlist !')

    def add_songs(self, songslist):
        for i in songslist:
            self.data.append(i)
    





def main():
    s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", duration="3:44")
    s2 = Song(title="Doko-Doko", artist="Kondio", album="The Best", duration="3:34")
    s3 = Song(title="Smukacha", artist="Ivana", album="Neznam", duration="3:51")
    p = Playlist('testname')

    p.add_song(s3)
    p.add_songs([s1, s2])

    


if __name__ == "__main__":
    main()  