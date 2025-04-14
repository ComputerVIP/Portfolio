import os
import yt_dlp

repeat = 1

def download_video(url, download_type, save_path):
    if download_type == 'mp4':
        try:
            ydl_opts = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
                "noplaylist": True,
                "postprocessors": [{
                    "key": "FFmpegVideoMerger",
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"✅ Downloaded (MP4): {url}")
        except Exception as e:
            print(f"❌ Error downloading (MP4) {url}: {e}")
    elif download_type == 'mp3':
        try:
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
                "noplaylist": True,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"✅ Downloaded (MP3): {url}")
        except Exception as e:
            print(f"❌ Error downloading (MP3) {url}: {e}")
    else:
        print("❌ Invalid download type.")

def main(repeat):
    while True:
        choice = input('''🎬 YouTube Video Downloader, choose a number to start:
    (1) Download a single video
    (2) Download all uploads from a channel
    (3) Exit
''').strip()
        if choice == "3":
            print("Exiting...")
            repeat = 0
            break

        save_path = input('''What is the path for your downloads folder? (C:\\Users\\<username>\\Downloads)
''').strip()
        if not os.path.exists(save_path):
            print("❌ Invalid path. Please try again.")
            continue

        if choice == "1":
            video_url = input("Enter the YouTube video URL:\n").strip()
            download_type = input('''Choose what type of download you want:
    (1) MP4, video + audio
    (2) MP3, audio only
''').strip()
            if download_type == "1":
                download_video(video_url, "mp4", save_path)
            elif download_type == "2":
                download_video(video_url, "mp3", save_path)
            else:
                print("❌ Invalid download type.")
        elif choice == "2":
            print("Feature not implemented yet.")
        else:
            print("❌ Invalid choice.")
    return repeat

if __name__ == "__main__":
    while repeat > 0:
        main(1)