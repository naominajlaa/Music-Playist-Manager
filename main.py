from playlist import myPlaylist

def main():
    playlist = myPlaylist()

    # Data awal
    playlist.add_song("Ditto", "NewJeans", 185)
    playlist.add_song("Jellyous", "ILLIT", 163)
    playlist.add_song("Spicy", "aespa", 197)
    playlist.add_song("What You Want", "CORTIS", 180)
    playlist.add_song("Rebel Heart", "IVE", 188)

    while True:
        print("\n==============================")
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
            playlist.view_playlist()

        # Mencari lagu
        elif pilihan == "2":
            song = input("Masukkan judul lagu: ")

            hasil = playlist.search_song(song)

            if hasil:
                print("Lagu ditemukan!")
                print(f"Judul    : {hasil['title']}")
                print(f"Artis    : {hasil['artist']}")
                print(f"Durasi   : {hasil['duration']} detik")
            else:
                print("Lagu tidak ditemukan.")

        # Sorting berdasarkan durasi
        elif pilihan == "3":
            playlist.duration_sorting()

            print("Playlist berhasil diurutkan!")
            playlist.view_playlist()

        # Menghitung total durasi
        elif pilihan == "4":
            total = playlist.total_duration()

            menit = total // 60
            detik = total % 60

            print("\n===== TOTAL DURASI =====")
            print(f"Total durasi : {menit} menit {detik} detik")

        # Menambah lagu
        elif pilihan == "5":
            song = input("Judul lagu    : ")
            artist = input("Artis         : ")
            duration = int(input("Durasi (detik): "))

            playlist.add_song(song, artist, duration)

            print("Lagu berhasil ditambahkan!")

        # Menghapus lagu
        elif pilihan == "6":
            song = input("Masukkan judul lagu yang ingin dihapus: ")

            berhasil = playlist.remove_song(song)

            if berhasil:
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan.")

        # Keluar
        elif pilihan == "7":
            print("Terima kasih sudah menggunakan Music Playlist Manager!")
            break

        else:
            print("Pilihan tidak tersedia.")


main()