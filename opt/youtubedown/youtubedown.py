#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Requisitos del sistema (todos disponibles vía APT o binario):
- python3
- python3-tk        (GUI tkinter)
- yt-dlp (actualizado desde github.com/yt-dlp/yt-dlp/releases)
- ffmpeg            (para extraer audio en formato MP3)

Instalación de dependencias:
sudo apt install python3-tk ffmpeg
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import os
import threading
import locale
import re

# Traducciones
translations = {
    'es': {
        'title': 'Youtube Downloader',
        'url_label': 'Dirección de YouTube:',
        'format_label': 'Formato:',
        'download_button': 'Descargar',
        'language_label': 'Idioma:',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': '¡Descarga completa!',
        'error': 'Error al descargar:',
        'choose_folder': 'Selecciona carpeta de destino',
        'downloading': 'Descargando...',
    },
    'en': {
        'title': 'Youtube Downloader',
        'url_label': 'YouTube URL:',
        'format_label': 'Format:',
        'download_button': 'Download',
        'language_label': 'Language:',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': 'Download completed!',
        'error': 'Download failed:',
        'choose_folder': 'Select destination folder',
        'downloading': 'Downloading...',
    },
    'de': {
        'title': 'Youtube-Downloader',
        'url_label': 'YouTube-Adresse:',
        'format_label': 'Format:',
        'download_button': 'Herunterladen',
        'language_label': 'Sprache:',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': 'Download abgeschlossen!',
        'error': 'Fehler beim Herunterladen:',
        'choose_folder': 'Zielordner auswählen',
        'downloading': 'Herunterladen...',
    },
    'fr': {
        'title': 'Téléchargeur YouTube',
        'url_label': 'Adresse YouTube :',
        'format_label': 'Format :',
        'download_button': 'Télécharger',
        'language_label': 'Langue :',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': 'Téléchargement terminé !',
        'error': 'Erreur lors du téléchargement :',
        'choose_folder': 'Sélectionner le dossier de destination',
        'downloading': 'Téléchargement...',
    },
    'pt': {
        'title': 'Baixador do YouTube',
        'url_label': 'Endereço do YouTube:',
        'format_label': 'Formato:',
        'download_button': 'Baixar',
        'language_label': 'Idioma:',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': 'Download concluído!',
        'error': 'Erro ao baixar:',
        'choose_folder': 'Escolher pasta de destino',
        'downloading': 'Baixando...',
    },
    'it': {
        'title': 'Downloader di YouTube',
        'url_label': 'Indirizzo YouTube:',
        'format_label': 'Formato:',
        'download_button': 'Scarica',
        'language_label': 'Lingua:',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': 'Download completato!',
        'error': 'Errore durante il download:',
        'choose_folder': 'Seleziona cartella di destinazione',
        'downloading': 'Scaricando...',
    },
    'gl': {
        'title': 'Descargador de YouTube',
        'url_label': 'Enderezo de YouTube:',
        'format_label': 'Formato:',
        'download_button': 'Descargar',
        'language_label': 'Lingua:',
        'footer': '(c) Charlie Martínez - Quirinux GPLv2',
        'select_format': ['MP4', 'MP3'],
        'success': 'Descarga completa!',
        'error': 'Erro ao descargar:',
        'choose_folder': 'Selecciona o cartafol de destino',
        'downloading': 'Descargando...',
    }
}

def get_system_language():
    lang = locale.getdefaultlocale()[0]
    if lang:
        code = lang.split('_')[0]
        return code if code in translations else 'en'
    return 'en'

class YoutubeDownloader:
    def __init__(self, root):
        self.root = root
        self.lang = get_system_language()
        self.setup_ui()

    def setup_ui(self):
        t = translations[self.lang]
        self.root.title(t['title'])
        self.root.geometry('480x320')
        self.root.resizable(False, False)

        self.mainframe = ttk.Frame(self.root, padding="12")
        self.mainframe.pack(fill='both', expand=True)

        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value='MP4')
        self.lang_var = tk.StringVar(value=self.lang)

        tk.Label(self.mainframe, text="YouTubeDown!", font=("Helvetica", 20, 'bold'), fg="#800000").pack(pady=(0, 0))
        tk.Label(self.mainframe, text="(c) Charlie Martínez - Quirinux GPLv2", font=("Arial", 8), fg="gray").pack(pady=(0, 10))

        ttk.Label(self.mainframe, text=t['url_label']).pack(anchor='w')
        ttk.Entry(self.mainframe, textvariable=self.url_var, width=52).pack(pady=2)

        ttk.Label(self.mainframe, text=t['format_label']).pack(anchor='w', pady=(10, 0))
        ttk.Combobox(self.mainframe, textvariable=self.format_var,
                     values=t['select_format'], state='readonly').pack()

        ttk.Label(self.mainframe, text=t['language_label']).pack(anchor='w', pady=(10, 0))
        lang_selector = ttk.Combobox(self.mainframe, textvariable=self.lang_var,
                                     values=list(translations.keys()), state='readonly')
        lang_selector.pack()
        lang_selector.bind("<<ComboboxSelected>>", self.change_language)

        self.progress = ttk.Progressbar(self.mainframe, length=300, mode='determinate')
        self.progress.pack(pady=10)

        ttk.Button(self.mainframe, text=t['download_button'], command=self.start_download_thread).pack(pady=5)
        self.status_label = tk.Label(self.mainframe, text="", font=("Arial", 9, "bold"), fg="green")
        self.status_label.pack()

    def change_language(self, event=None):
        self.lang = self.lang_var.get()
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        self.setup_ui()

    def start_download_thread(self):
        thread = threading.Thread(target=self.download_video)
        thread.start()

    def download_video(self):
        url = self.url_var.get().strip()
        fmt = self.format_var.get().lower()
        t = translations[self.lang]

        if not url:
            messagebox.showerror(t['title'], t['error'] + "\n(No URL)")
            return

        desktop_path = os.path.join(os.path.expanduser("~"), "Escritorio")
        if not os.path.exists(desktop_path):
            desktop_path = os.path.expanduser("~")

        folder = filedialog.askdirectory(title=t['choose_folder'], initialdir=desktop_path, mustexist=True)
        if not folder:
            return

        if os.path.basename(folder).startswith("."):
            messagebox.showerror(t['title'], t['error'] + "\n(Carpeta oculta no permitida)")
            return

        self.status_label.config(text=t['downloading'])
        self.progress['value'] = 0
        self.root.update_idletasks()

        try:
            if fmt == 'mp4':
                cmd = [
                    'yt-dlp',
                    '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                    '-o', os.path.join(folder, '%(title)s.%(ext)s'),
                    url
                ]
            elif fmt == 'mp3':
                cmd = [
                    'yt-dlp',
                    '--extract-audio',
                    '--audio-format', 'mp3',
                    '-o', os.path.join(folder, '%(title)s.%(ext)s'),
                    url
                ]

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                self.root.update_idletasks()
                match = re.search(r'\b(\d{1,3}\.\d)%', line)
                if match:
                    progress_value = float(match.group(1))
                    self.progress['value'] = progress_value
                    self.status_label.config(text=f"{t['downloading']} {progress_value:.1f}%")

            process.wait()
            if process.returncode == 0:
                self.progress['value'] = 100
                self.status_label.config(text=t['success'])
                messagebox.showinfo(t['title'], t['success'])
            else:
                raise RuntimeError("yt-dlp returned error code")

        except Exception as e:
            self.status_label.config(text=f"{t['error']} {e}")
            messagebox.showerror(t['title'], f"{t['error']}\n{e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = YoutubeDownloader(root)
    root.mainloop()
