genre = input("Masukkan genre favorit Anda (aksi, drama, komedi): ").lower()

if genre == "aksi":
    print("Rekomendasi film: Fast & Furious, Avengers")
elif genre == "drama":
    print("Rekomendasi film: The Pursuit of Happyness, The Fault in Our Stars")
elif genre == "komedi":
    print("Rekomendasi film: Home Alone, Deadpool")
else:
    print("Genre tidak tersedia, coba genre lain.")
