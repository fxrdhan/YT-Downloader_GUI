# Mengimpor modul yang dibutuhkan
from pytube import YouTube  # untuk mengunduh video dari YouTube
from moviepy.editor import AudioFileClip  # untuk mengambil audio dari video
import os  # untuk menghapus file sementara
import tkinter as tk  # untuk membuat antarmuka GUI
from tkinter import filedialog  # untuk memilih direktori download
from tkinter import messagebox  # untuk menampilkan pesan setelah berhasil mengunduh

# Fungsi untuk memilih direktori download
def browse_directory():
    download_directory = filedialog.askdirectory()  # tampilan dialog untuk memilih direktori
    directory_entry.delete(0, tk.END)  # menghapus teks yang ada di dalam Entry widget
    directory_entry.insert(0, download_directory)  # menambahkan direktori yang dipilih ke dalam Entry widget

# Fungsi untuk menghapus teks yang ada pada kolom Link
def reset_link():
    link_entry.delete(0, tk.END)  # menghapus teks yang ada di dalam Entry widget

# Fungsi untuk mengunduh video atau audio dari YouTube
def download():
    link = link_entry.get()  # mengambil teks yang ada pada Entry widget untuk mendapatkan link video
    download_directory = directory_entry.get()  # mengambil direktori download yang dipilih oleh pengguna
    yt = YouTube(link)  # membuat objek YouTube dengan menggunakan link yang diberikan
    if var.get() == 1:  # Jika button video dipilih
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res="720p").first()  # memilih stream video dengan kualitas 720p
        stream.download(download_directory)  # mengunduh video dan menyimpannya di direktori yang dipilih
    else:  # Jika button audio dipilih
        stream = yt.streams.filter(only_audio=True).first()  # memilih stream audio
        mp4_file = stream.download(download_directory)  # mengunduh video dalam format mp4
        mp3_file = mp4_file.replace(".mp4", "_audio.mp3")  # membuat nama file baru untuk audio
        audioclip = AudioFileClip(mp4_file)  # membuat objek AudioFileClip dari video mp4 yang telah diunduh
        audioclip.write_audiofile(mp3_file)  # mengambil audio dari video dan menyimpannya dalam format mp3
        audioclip.close()  # menutup objek AudioFileClip
        os.remove(mp4_file)  # menghapus file video sementara yang telah diunduh
        messagebox.showinfo("Done", "SUCCEEDED!")  # menampilkan pesan jika unduhan berhasil

# Membuat antarmuka GUI
window_root = tk.Tk()  # membuat objek Tk
window_root.title("YT Downloader GUI by @fxrdhan_")  # memberi judul pada window
window_root.configure(bg='black')  # memberi warna latar belakang pada window
window_root.resizable(False,False)  # tolak perubahan ukuran pada interface

# Frame untuk menampung kolom input dan tombol reset
input_frame = tk.Frame(window_root, bg='black')  # membuat objek Frame untuk menampung widget
input_frame.pack(fill='x', padx=10, pady=5)  # menempatkan Frame pada window utama

link_label = tk.Label(input_frame, text="Link YouTube:", fg='white', bg='black', width=15)  # membuat Label widget untuk teks
link_label.pack(side='left')

link_entry = tk.Entry(input_frame, width=35, bg='black', fg='magenta')  # membuat entry box untuk memasukkan link video
link_entry.pack(side='left', padx=5)  # menempatkan entry box pada posisi sebelah kiri dari frame input_frame

reset_button = tk.Button(input_frame, text="Reset link", command=reset_link, bg='black', fg='red', width=10, font=('arial italic','9'))  # membuat tombol "Reset link" yang ketika ditekan akan menjalankan fungsi reset_link
reset_button.pack(side='right')  # menempatkan tombol "Reset link" pada posisi sebelah kanan dari frame input_frame

# Frame untuk menampung kolom input dan tombol browse
browse_frame = tk.Frame(window_root, bg='black')
browse_frame.pack(fill='x', padx=10, pady=5)  # menempatkan frame browse_frame di window root, mengisi sepanjang sumbu x, dengan jarak padding pada x=10 dan y=5

directory_label = tk.Label(browse_frame, text="Direktori Download:", fg='white', bg='black', width=15)  # mMembuat label "Direktori Download" dengan warna teks putih dan latar belakang hitam pada frame browse_frame, dengan lebar label 15
directory_label.pack(side='left')  # menempatkan label "Direktori Download" pada posisi sebelah kiri dari frame browse_frame

directory_entry = tk.Entry(browse_frame, width=35, bg='black', fg='magenta')  # membuat entry box untuk memasukkan direktori download
directory_entry.pack(side='left', padx=5)  # menempatkan entry box pada posisi sebelah kiri dari frame browse_frame, dengan jarak padding pada x=5

browse_button = tk.Button(browse_frame, text="Browse", command=browse_directory, bg='black', fg='orange', width=10, font=('arial italic','9'))  # membuat tombol "Browse" yang ketika ditekan akan menjalankan fungsi browse_directory
browse_button.pack(side='right')  # menempatkan tombol "Browse" pada posisi sebelah kanan dari frame browse_frame

# Kolom input untuk memilih tipe download
directory_label = tk.Label(window_root, text="Pilih Tipe Unduhan:", fg='white', bg='black')  # membuat label "Pilih Tipe Unduhan" dengan warna teks putih dan latar belakang hitam di window root
directory_label.pack(padx=5, pady=5, side='left')  # menempatkan label "Pilih Tipe Unduhan" pada window root dengan jarak padding pada x=5 dan y=5, dan posisi sebelah kiri

var = tk.IntVar(value=1)  # membuat variable int dengan nilai awal 1
audio_button = tk.Radiobutton(window_root, text="Audio Only [mp3]", variable=var, value=2, fg='#4f83db', bg='black', font=('consolas light', '9'))  # membuat button "Audio Only"
audio_button.pack(side='left')

video_button = tk.Radiobutton(window_root, text="Video [HD mp4]", variable=var, value=1, fg='#4f83db', bg='black', font=('consolas light', '9'))  # membuat button "Video Only"
video_button.pack(side='left')

download_button = tk.Button(window_root, text="DOWNLOAD", command=download, bg='black', fg='green', font=('arial bold', '9'))  # membuat tombol aksi untuk mendulai unduhan
download_button.pack(side='left', fill='y', padx=10, pady=10)

window_root.mainloop()  # menjalankan program GUI dengan memanggil method mainloop() dari object window root.