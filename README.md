# YouTube Downloader GUI
(c) Charlie Martínez - Quirinux Project, GPLv2

**YouTube Downloader GUI** is a simple, multilingual graphical application for downloading YouTube videos in either **MP4 (video)** or **MP3 (audio)** format.  

It is built in Python 3 using Tkinter for the graphical interface, and uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) as the backend downloader.

## Features

- Download YouTube videos as MP4
- Extract audio as MP3 using `ffmpeg`
- Real-time download progress bar
- Choose the output folder before downloading
- Multilingual interface: Spanish, English, German, French, Italian, Portuguese, Galician
- Automatically adapts to your system's configured language
- Works offline (no pip required)
- Designed to work fully on Debian-based systems

## Requirements

Install the following packages using APT:

```bash
sudo apt install python3-tk ffmpeg
```

## About yt-dlp

This program depends on an up-to-date version of yt-dlp for reliable YouTube support.

### Debian and Ubuntu: 

The yt-dlp package in official repositories is often outdated. In that case, it is recommended to install the official binary:

```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```
### Quirinux: 

yt-dlp is available and kept up to date directly in the Quirinux repositories. No manual installation is needed in this case.
You can verify the package at:

[https://repo.quirinux.org/pool/main/y/](https://repo.quirinux.org/pool/main/y/yt-dlp/)

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-downloader-gui.git
cd youtube-downloader-gui
```

Run the application:
```bash
python3 youtubedownload.py
```

## Alternative: Install from Quirinux Repository

If you're using Quirinux, you can install the app directly from the official repository as a .deb package:

```bash
su root
apt install quirinux-youtubedownloader
```

Also available from the Quirinux Software Center.

Package URL:
https://repo.quirinux.org/pool/main/q/quirinux-youtubedownloader

## License

This project is licensed under the GNU General Public License v2.
(c) Charlie Martínez - Quirinux Project
This application is part of the Quirinux ecosystem but is compatible with any modern GNU/Linux distribution.
