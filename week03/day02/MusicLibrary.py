from random import shuffle
import json


class Song:
    def __init__(self, title = "", artist = "", album = "", length = ""):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return f"{self.artist} - {self.title} from {self.album} - {self.length}"

    def __eq__(self, other):
        return (self.title, self.artist, self.album, self.length) == (other.title, other.artist, other.album, other.length)

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.length))

    def song_length(self, seconds = False, minutes = False, hours = False):
        if not (seconds, minutes, hours):
            return self.length

        splittime = self.length.split(':')
        s, m, h = 0, 0, 0

        if len(splittime) == 2:
            s, m = int(splittime[1]), int(splittime[0])
        elif len(splittime) == 3:
            s, m, h = int(splittime[2]), int(splittime[1]), int(splittime[0])
            
        if seconds:
            result = s + m*60 + h*3600
            return str(round(result, 2))

        if minutes:
            result = s*0.0166666667 + m + h*60
            result = round(result, 2)
            results = round(round(result - int(result), 2)*60)
            return f'{int(result)}:{results}'
            
        if hours:
            result = s*0.000277777778 + m*0.0166666667 + h
            return str(round(result, 2))
            
class Playlist:
    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.songslist = []
        self.artists = dict()
        self.repeat = repeat
        self.shuffle = shuffle
        self.n = 0

    def __next__(self):
        if not self.repeat:
            if self.n == len(self.songslist):
                raise StopIteration
            return_value = self.songslist[self.n]
            self.n += 1
            return return_value
        elif self.repeat:
            if self.n == len(self.songslist):
                self.n = 0
            return_value = self.songslist[self.n]
            self.n += 1
            return return_value

    def __iter__(self):
        return self

    def add_song(self, song):
        self.songslist.append(song)
        
        if song.artist in self.artists:
            self.artists[song.artist] += 1
        else:
            self.artists[song.artist] = 1

    def add_songs(self, songs):
        for s in songs:
            self.add_song(s)

    def total_length(self):
        mins, secs = 0, 0
        for s in self.songslist:
            splitlen = s.song_length(minutes = True).split(':')
            mins += int(splitlen[0])
            secs += int(splitlen[1])

        return f'{mins}:{secs}'

    def show_artists(self):
        return self.artists

    def next_song(self):
        if self.n == 0 and self.shuffle:
            shuffle(self.songslist)

        return next(self)

    def save(self):
        tojson = [s.__dict__ for s in self.songslist]
        filename = self.name.replace(' ','-')
        with open(f'{filename}.json', 'w') as f:
            json.dump(tojson, f)

    def load(self, path):
        with open(path, 'r') as f:
            jsonfile = json.load(f)
            jsonfile = [j for j in jsonfile]
        newlist = []
        for i in jsonfile:
            newlist.append(Song(title = i['title'] , artist = i['artist'], album = i['album'], length = i['length']))
    
        return newlist

