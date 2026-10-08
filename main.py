from playlist import myPlaylist

def main():
    playlist = myPlaylist()    

    while True:
        print("==============================")
        print("     MUSIC PLAYLIST MANAGER")
        print("==============================")
        print("1. Lihat Playlist")
        print("2. Cari Lagu")
        print("3. Urutkan Berdasarkan Durasi")
        print("4. Hitung Total Durasi")
        print("5. Tambah Lagu")
        print("6. Hapus Lagu")
        print("7. Keluar")
        print("==============================")

        pilihan = input("Pilih menu: ")

        # Menampilkan playlist
        if pilihan == "1":
            playlist.viewPlaylist()

        # Mencari lagu
        elif pilihan == "2":
            song = input("Masukkan judul lagu: ")

            hasil = playlist.searchSong(song)

            if hasil:
                print("Lagu ditemukan!")
                print(f"Judul    : {hasil['title']}")
                print(f"Artis    : {hasil['artist']}")
                print(
                    f"Durasi   : "
                    f"{playlist.convertSecondsToMinutes(hasil['duration'])}"
                )
            else:
                print("Lagu tidak ditemukan.")

        # Sorting berdasarkan durasi
        elif pilihan == "3":
            playlist.durationSorting()
            playlist.saveData()
            print("Playlist berhasil diurutkan!")
            playlist.viewPlaylist()

        # Menghitung total durasi
        elif pilihan == "4":
            total = playlist.totalDuration()

            print("\n===== TOTAL DURASI =====")
            print(
                f"Total durasi : "
                f"{playlist.convertSecondsToMinutes(total)}"
            )

        # Menambah lagu
        elif pilihan == "5":
            song = input("Judul lagu    : ")
            artist = input("Artis         : ")
            duration = int(input("Durasi (detik): "))

            playlist.addSong(song, artist, duration)
            playlist.saveData()
            print("Lagu berhasil ditambahkan!")

        # Menghapus lagu
        elif pilihan == "6":
            song = input("Masukkan judul lagu yang ingin dihapus: ")
            berhasil = playlist.removeSong(song)

            if berhasil:
                playlist.saveData()
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan.")

        # Keluar
        elif pilihan == "7":
            print("\n===== KELUAR =====")
            print("Terima kasih sudah menggunakan Music Playlist Manager!")
            break

        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()