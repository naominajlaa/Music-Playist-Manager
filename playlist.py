class myPlaylist:
    #Array (list): menyimpan semua data lagu dalam playlist.
    def __init__(self):
        self.songs = []
        self.loadData()

    def loadData(self):
        try:
            with open("playlist.txt", "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split("|")

                    if len(data) == 3:
                        song = {
                            "title": data[0],
                            "artist": data[1],
                            "duration": int(data[2])
                        }
                        self.songs.append(song)
        except FileNotFoundError:
            with open("playlist.txt", "w", encoding="utf-8"):
                pass

    # Simpan data ke TXT
    def saveData(self):
        with open("playlist.txt", "w", encoding="utf-8") as file:
            for song in self.songs:
                file.write(
                    song["title"] + "|" +
                    song["artist"] + "|" +
                    str(song["duration"]) + "\n"
                )

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
        for i, song_data in enumerate(self.songs, start=1):
            print(f"{i}. {song_data['title']} - {song_data['artist']} - {self.convertSecondsToMinutes(song_data['duration'])}")

    # Linear Searching: mencari lagu berdasarkan judul.
    def searchSong(self, song):
        for song_data in self.songs:
            if song_data['title'].lower() == song.lower():
                return song_data
        return None

    #Bubble Sort: membandingkan lagu bersebelahan lalu menukarnya jika perlu.
    def durationSorting(self):
        n = len(self.songs)
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