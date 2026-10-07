class myPlaylist:
    #Array (list): menyimpan semua data lagu dalam playlist.
    def __init__(self):
        self.songs = []
        self.current_song_index = 0

    def convertSecondsToMinutes(self, seconds):
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            return f"{minutes:02d}:{remaining_seconds:02d}"

    def addSong(self, song, artist, duration):
        song_data = {
            'title': song,
            'artist': artist,
            'duration': duration
        }
        # Menambahkan data lagu ke array/list.
        self.songs.append(song_data)

    def removeSong(self, song):
        for i, song_data in enumerate(self.songs):
            if song_data['title'].lower() == song.lower():
                del self.songs[i]
                return True
        return False

    def viewPlaylist(self):
        print("\n===== MY PLAYLIST =====")

        # Traversal: mengunjungi dan menampilkan setiap lagu di array.
        for i, song_data in enumerate(self.songs, start=1):
            print(f"{i}. {song_data['title']} - {song_data['artist']} - {self.convertSecondsToMinutes(song_data['duration'])}")

    # Linear Searching: mencari lagu berdasarkan judul.
    def searchSong(self, song):
        for song_data in self.songs:
            if song_data['title'].lower() == song.lower():
                return song_data
        return None

    def durationSorting(self):
        n = len(self.songs)

        #Bubble Sort: membandingkan lagu bersebelahan lalu menukarnya jika perlu.
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.songs[j]["duration"] > self.songs[j + 1]["duration"]:
                    self.songs[j], self.songs[j + 1] = (
                        self.songs[j + 1],
                        self.songs[j])

    #Rekursif: menghitung total durasi lagu dalam playlist.
    def totalDuration(self, index=0):
        if index == len(self.songs):
            return 0
        return self.songs[index]["duration"] + self.totalDuration(index + 1)