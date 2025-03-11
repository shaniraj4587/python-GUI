import tkinter as tk
from tkinter import ttk, filedialog
import pygame
import os
from mutagen.mp3 import MP3
from PIL import Image, ImageTk, ImageDraw, ImageFont
import time
from pathlib import Path

class ModernAudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Audio Player")
        self.root.geometry("500x700")
        self.root.configure(bg="#1e1e1e")
        
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Variables
        self.current_song = None
        self.paused = False
        self.songs_list = []
        self.current_song_index = 0
        
        # Load icons
        self.load_icons()
        self.setup_ui()
        self.setup_bindings()

    def load_icons(self):
        self.icons = {}
        size = (30, 30)
        
        # Create simple colored shapes for buttons
        colors = {
            "play": "#4CAF50",    # Green
            "pause": "#f44336",   # Red
            "next": "#2196F3",    # Blue
            "prev": "#2196F3",    # Blue
            "volume": "#FFC107"   # Amber
        }
        
        for name, color in colors.items():
            img = Image.new('RGBA', size, color)
            self.icons[name] = ImageTk.PhotoImage(img)

    def create_icon(self, symbol, color, size=(30, 30)):
        img = Image.new('RGBA', size, color)
        return ImageTk.PhotoImage(img)

    def setup_ui(self):
        # Style configuration
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#1e1e1e")
        style.configure("Custom.TButton", padding=10)
        style.configure("Custom.TLabel", background="#1e1e1e", foreground="#ffffff")
        style.configure("Playlist.TFrame", background="#2d2d2d")
        
        # Main container
        self.main_frame = ttk.Frame(self.root, style="Custom.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Now playing section
        self.setup_now_playing()
        
        # Progress section
        self.setup_progress()
        
        # Controls section
        self.setup_controls()
        
        # Playlist section
        self.setup_playlist()

    def setup_now_playing(self):
        now_playing_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        now_playing_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(now_playing_frame, text="NOW PLAYING", 
                 style="Custom.TLabel", font=("Segoe UI", 12)).pack()
        
        self.song_label = ttk.Label(now_playing_frame, text="No Song Selected",
                                  style="Custom.TLabel", 
                                  font=("Segoe UI", 14, "bold"),
                                  wraplength=460)
        self.song_label.pack(pady=10)

    def setup_progress(self):
        self.progress_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.progress_frame.pack(fill=tk.X, pady=10)
        
        self.current_time_label = ttk.Label(self.progress_frame, text="00:00",
                                          style="Custom.TLabel")
        self.current_time_label.pack(side=tk.LEFT)
        
        self.progress_bar = ttk.Scale(self.progress_frame, from_=0, to=100,
                                    orient=tk.HORIZONTAL, style="Custom.Horizontal.TScale")
        self.progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        
        self.total_time_label = ttk.Label(self.progress_frame, text="00:00",
                                        style="Custom.TLabel")
        self.total_time_label.pack(side=tk.LEFT)

    def setup_controls(self):
        controls_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        controls_frame.pack(pady=20)
        
        # Control buttons with icons
        ttk.Button(controls_frame, image=self.icons["prev"],
                  command=self.previous_song).pack(side=tk.LEFT, padx=10)
        
        self.play_button = ttk.Button(controls_frame, image=self.icons["play"],
                                    command=self.play_pause)
        self.play_button.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(controls_frame, image=self.icons["next"],
                  command=self.next_song).pack(side=tk.LEFT, padx=10)
        
        # Volume control
        volume_frame = ttk.Frame(controls_frame, style="Custom.TFrame")
        volume_frame.pack(side=tk.LEFT, padx=(20, 0))
        
        ttk.Label(volume_frame, image=self.icons["volume"],
                 style="Custom.TLabel").pack(side=tk.LEFT)
        
        self.volume_slider = ttk.Scale(volume_frame, from_=0, to=100,
                                     orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(70)
        self.volume_slider.pack(side=tk.LEFT, padx=(5, 0))

    def setup_playlist(self):
        playlist_frame = ttk.Frame(self.main_frame, style="Playlist.TFrame")
        playlist_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Playlist header
        header_frame = ttk.Frame(playlist_frame, style="Custom.TFrame")
        header_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(header_frame, text="PLAYLIST",
                 style="Custom.TLabel", font=("Segoe UI", 12)).pack(side=tk.LEFT)
        
        ttk.Button(header_frame, text="Add Songs",
                  command=self.add_songs).pack(side=tk.RIGHT)
        
        # Playlist with scrollbar
        playlist_container = ttk.Frame(playlist_frame, style="Custom.TFrame")
        playlist_container.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        scrollbar = ttk.Scrollbar(playlist_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.playlist = tk.Listbox(playlist_container,
                                 bg="#2d2d2d",
                                 fg="#ffffff",
                                 selectmode=tk.SINGLE,
                                 selectbackground="#4CAF50",
                                 font=("Segoe UI", 10),
                                 height=10,
                                 yscrollcommand=scrollbar.set)
        self.playlist.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.playlist.yview)

    def setup_bindings(self):
        self.playlist.bind('<Double-Button-1>', self.play_selected_song)
        self.root.bind('<space>', lambda e: self.play_pause())
        self.root.bind('<Left>', lambda e: self.previous_song())
        self.root.bind('<Right>', lambda e: self.next_song())

    def add_songs(self):
        files = filedialog.askopenfilenames(
            filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])
        for file in files:
            self.songs_list.append(file)
            self.playlist.insert(tk.END, os.path.basename(file))

    def play_selected_song(self, event=None):
        if self.playlist.curselection():
            self.current_song_index = self.playlist.curselection()[0]
            self.play_song()

    def play_song(self):
        if self.current_song:
            pygame.mixer.music.stop()
        
        song_path = self.songs_list[self.current_song_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        
        self.current_song = song_path
        self.song_label.config(text=os.path.basename(song_path))
        self.update_progress()

    def play_pause(self):
        if not self.current_song:
            if self.songs_list:
                self.play_song()
        else:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True

    def next_song(self):
        if self.songs_list:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs_list)
            self.play_song()

    def previous_song(self):
        if self.songs_list:
            self.current_song_index = (self.current_song_index - 1) % len(self.songs_list)
            self.play_song()

    def set_volume(self, val):
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)

    def seek(self, event):
        if self.current_song:
            song = MP3(self.current_song)
            total_length = song.info.length
            position = (self.progress_bar.get() / 100) * total_length
            pygame.mixer.music.play(start=position)

    def update_progress(self):
        if self.current_song and not self.paused:
            current_time = pygame.mixer.music.get_pos() / 1000
            song = MP3(self.current_song)
            total_length = song.info.length
            
            # Update progress bar
            progress = (current_time / total_length) * 100
            self.progress_bar.set(progress)
            
            # Update time labels
            self.current_time_label.config(
                text=time.strftime('%M:%S', time.gmtime(current_time)))
            self.total_time_label.config(
                text=time.strftime('%M:%S', time.gmtime(total_length)))
            
        self.root.after(1000, self.update_progress)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernAudioPlayer(root)
    root.mainloop()