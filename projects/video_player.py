import tkinter as tk
from tkinter import ttk, filedialog, Menu
import vlc
import time
import os

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Video Player")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        
        # Initialize VLC instance
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        
        # Variables
        self.is_playing = False
        self.current_time = 0
        self.duration = 0
        
        self.setup_ui()
        self.create_menu()
        self.setup_bindings()

    def setup_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Video frame
        self.video_frame = ttk.Frame(self.main_frame)
        self.video_frame.pack(fill=tk.BOTH, expand=True)
        
        # Controls frame
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(fill=tk.X, pady=10)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Scale(
            self.controls_frame,
            from_=0, to=100,
            orient=tk.HORIZONTAL,
            variable=self.progress_var,
            command=self.seek
        )
        self.progress_bar.pack(fill=tk.X, padx=10)
        
        # Time labels
        self.time_frame = ttk.Frame(self.controls_frame)
        self.time_frame.pack(fill=tk.X, padx=10)
        
        self.current_time_label = ttk.Label(self.time_frame, text="00:00:00")
        self.current_time_label.pack(side=tk.LEFT)
        
        self.duration_label = ttk.Label(self.time_frame, text="00:00:00")
        self.duration_label.pack(side=tk.RIGHT)
        
        # Control buttons
        self.buttons_frame = ttk.Frame(self.controls_frame)
        self.buttons_frame.pack(pady=10)
        
        ttk.Button(self.buttons_frame, text="⏮", command=self.prev_10s).pack(side=tk.LEFT, padx=5)
        self.play_button = ttk.Button(self.buttons_frame, text="▶", command=self.play_pause)
        self.play_button.pack(side=tk.LEFT, padx=5)
        ttk.Button(self.buttons_frame, text="⏭", command=self.next_10s).pack(side=tk.LEFT, padx=5)
        
        # Volume control
        self.volume_frame = ttk.Frame(self.controls_frame)
        self.volume_frame.pack(pady=5)
        
        ttk.Label(self.volume_frame, text="🔊").pack(side=tk.LEFT, padx=5)
        self.volume_scale = ttk.Scale(
            self.volume_frame,
            from_=0, to=100,
            orient=tk.HORIZONTAL,
            command=self.set_volume
        )
        self.volume_scale.set(50)
        self.volume_scale.pack(side=tk.LEFT, padx=5)

    def create_menu(self):
        menubar = Menu(self.root)
        
        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Playback menu
        playback_menu = Menu(menubar, tearoff=0)
        playback_menu.add_command(label="Play/Pause", command=self.play_pause)
        playback_menu.add_command(label="Stop", command=self.stop)
        playback_menu.add_separator()
        playback_menu.add_command(label="Previous 10s", command=self.prev_10s)
        playback_menu.add_command(label="Next 10s", command=self.next_10s)
        menubar.add_cascade(label="Playback", menu=playback_menu)
        
        self.root.config(menu=menubar)

    def setup_bindings(self):
        self.root.bind("<space>", lambda e: self.play_pause())
        self.root.bind("<Left>", lambda e: self.prev_10s())
        self.root.bind("<Right>", lambda e: self.next_10s())
        self.root.bind("<Control-o>", lambda e: self.open_file())

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mkv *.mov"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.play_video(file_path)

    def play_video(self, file_path):
        # Create a media instance
        media = self.instance.media_new(file_path)
        self.player.set_media(media)
        
        # Set the window ID where to render VLC's video output
        if os.name == "nt":  # Windows
            self.player.set_hwnd(self.video_frame.winfo_id())
        else:  # Linux/Mac
            self.player.set_xwindow(self.video_frame.winfo_id())
        
        self.player.play()
        self.is_playing = True
        self.play_button.configure(text="⏸")
        self.update_progress()

    def play_pause(self):
        if self.player.get_media():
            if self.is_playing:
                self.player.pause()
                self.play_button.configure(text="▶")
            else:
                self.player.play()
                self.play_button.configure(text="⏸")
            self.is_playing = not self.is_playing

    def stop(self):
        if self.player.get_media():
            self.player.stop()
            self.is_playing = False
            self.play_button.configure(text="▶")

    def seek(self, value):
        if self.player.get_media():
            value = float(value)
            duration = self.player.get_length()
            position = duration * (value / 100.0)
            self.player.set_time(int(position))

    def set_volume(self, value):
        volume = int(float(value))
        self.player.audio_set_volume(volume)

    def prev_10s(self):
        if self.player.get_media():
            current_time = self.player.get_time()
            new_time = max(0, current_time - 10000)  # 10 seconds in milliseconds
            self.player.set_time(new_time)

    def next_10s(self):
        if self.player.get_media():
            current_time = self.player.get_time()
            self.player.set_time(current_time + 10000)  # 10 seconds in milliseconds

    def update_progress(self):
        if self.player.get_media():
            current_time = self.player.get_time()
            duration = self.player.get_length()
            
            if duration > 0:
                self.progress_var.set((current_time / duration) * 100)
            
            # Update time labels
            current = time.strftime('%H:%M:%S', time.gmtime(current_time/1000))
            total = time.strftime('%H:%M:%S', time.gmtime(duration/1000))
            self.current_time_label.configure(text=current)
            self.duration_label.configure(text=total)
        
        self.root.after(1000, self.update_progress)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()