class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    genre_check = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(artist)
        Song.genres.append(genre)
        Song.genre_checker(genre)
        Song.genre_counter(genre)

    @classmethod
    def genre_checker(cls, genre):
        Song.genre_check.add(genre)

    @classmethod
    def genre_counter(cls, genre):
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
        return Song.genre_count

print(Song.count)

cloud9 = Song("cloud9", "beach bunny", "pop")
print(Song.genre_counter("pop"))
