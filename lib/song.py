class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_artist_list(artist)
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artist_list(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        else:
            pass

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        else:
            pass

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1



    # @classmethod
    # def show_artist_names(cls):
    # print([cls.artist for artist in cls.artists]) # can i use __repr__?