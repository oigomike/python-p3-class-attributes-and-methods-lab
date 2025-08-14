class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        Song.count += 1

        # Track genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Track artists
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update genre_count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist_count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
