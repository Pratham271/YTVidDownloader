import tkinter
import customtkinter
from pytube import YouTube
import certifi
import ssl

# Configure the global SSL context
ssl_context = ssl.create_default_context(cafile=certifi.where())

def startDownload():
    try:
        ytLink = link.get()
        print("YouTube Link:", ytLink)

        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except Exception as e:
        print("Error:", e)
        print("YouTube Link is invalid")
    print("Download Complete!")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20, pady=20)

# Run app
app.mainloop()
