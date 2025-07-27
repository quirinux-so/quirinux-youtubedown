# YouTubeDown!

**Autor / Author:** Charlie Martínez – Quirinux GNU/Linux®  
**Licencia / License:** GPLv2.0

![YouTubeDown Screenshot](https://github.com/user-attachments/assets/1c439f84-0f21-4928-9858-a51e80bfd535)

---

## 🧭 Descripción general / Overview

**ES:**  
`YouTubeDown!` es una aplicación gráfica, multilingüe y sin conexión, diseñada para descargar videos de YouTube en formato **MP4 (video)** o **MP3 (audio)**.  

Desarrollada en **Python 3** con **Tkinter**, utiliza **yt-dlp** como motor de descarga y está especialmente adaptada para sistemas basados en Debian.

**EN:**  
`YouTubeDown!` is a graphical, multilingual, and offline application for downloading YouTube videos as **MP4 (video)** or **MP3 (audio)**.  

Built with **Python 3** and **Tkinter**, it uses **yt-dlp** as its download backend and is specially tailored for Debian-based systems.

---

## ✔️ Características / Features

**ES:**
- Descargar vídeos como MP4  
- Extraer audio como MP3 (requiere `ffmpeg`)  
- Barra de progreso en tiempo real  
- Selección de carpeta de destino antes de descargar  
- Interfaz en: Español, Inglés, Alemán, Francés, Italiano, Portugués y Gallego  
- Adaptación automática al idioma del sistema  
- Uso completamente offline (no requiere conexión ni dependencias por pip)  
- Diseñada para sistemas basados en Debian

**EN:**
- Download videos as MP4  
- Extract audio as MP3 (requires `ffmpeg`)  
- Real-time progress bar  
- Choose output folder before download  
- Interface available in: Spanish, English, German, French, Italian, Portuguese, and Galician  
- Automatically adapts to your system language  
- Fully offline (no internet or pip dependencies required)  
- Designed for Debian-based systems

---

## 📋 Requisitos / Requirements

**ES**  
Instalar las siguientes dependencias antes de ejecutar:  

**EN:**  
Install the following dependencies before running:

```bash
sudo apt install python3-tk ffmpeg
```

**ES**  
Instalar `yt-dlp` actualizado manualmente (en Debian/Ubuntu):  

**EN:**  
Manually install latest `yt-dlp` (on Debian/Ubuntu):

```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

**🌀 En Quirinux / On Quirinux:**  
`yt-dlp` ya está actualizado en los repositorios oficiales:  
[https://repo.quirinux.org/pool/main/y/yt-dlp/](https://repo.quirinux.org/pool/main/y/yt-dlp/)

---

## ▶️ Ejecución / How to Run

**ES:**  
Clonar y ejecutar la aplicación:  

**EN:**  
Clone and run the application:

```bash
git clone https://github.com/quirinux-so/quirinux-youtubedown.git
cd quirinux-youtubedown/opt/youtubedown
python3 youtubedown.py
```

---

## 📦 Instalación alternativa / Optional Installation (Quirinux)

**ES:**  
Disponible como paquete oficial `.deb` desde el repositorio de Quirinux o desde el Centro de Software.

**EN:**  
Available as an official `.deb` package via the Quirinux repository or Software Center.

**Comando / Command:**

    su root
    apt install quirinux-youtubedown

**Repositorio / Repository:**  
[https://repo.quirinux.org/pool/main/q/quirinux-youtubedown](https://repo.quirinux.org/pool/main/q/quirinux-youtubedown)

---

## ⚖️ Aviso legal / Legal Notice

**ES:**  
Este proyecto forma parte del ecosistema **Quirinux**, pero es compatible con cualquier distribución moderna de GNU/Linux.  
Distribuido bajo los términos de la licencia **GPLv2**.

**EN:**  
This project is part of the **Quirinux** ecosystem but remains compatible with any modern GNU/Linux distribution.  
Released under the terms of the **GPLv2 license**.

**Autor / Author:** Charlie Martínez  
📧 <cmartinez@quirinux.org>

**Más información / More information:**  
[https://www.quirinux.org/aviso-legal](https://www.quirinux.org/aviso-legal)
