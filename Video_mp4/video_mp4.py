
import re
import requests
import yt_dlp
from bs4 import BeautifulSoup

def get_video_links(channel_url):
    """Scrapes video links from a YouTube channel's Videos page."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(channel_url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to retrieve page.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract video URLs
    video_links = set(re.findall(r'"/watch\?v=(.{11})"', response.text))

    return [f"https://www.youtube.com/watch?v={vid}" for vid in video_links]

def download_video(url, save_path, download_type):
    """Downloads a YouTube video using yt-dlp."""
    if download_type == 'mp4':
        try:
            ydl_opts = {
                "format": "bestvideo+bestaudio/best",  # Highest quality
                "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save location
                "noplaylist": True,  # Ensure we download only one video at a time
                "postprocessors": [{  # Merge audio and video
                    "key": "FFmpegVideoConvertor",
                    "preferredformat": "mp4",  # Format as mp4
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
                "format": "bestaudio/best",  # Highest quality audio
                "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save location
                "noplaylist": True,  # Ensure we download only one video at a time
                "postprocessors": [{  # Convert to MP3
                    "key": "FFmpegAudioConvertor",  # Correct postprocessor for audio
                    "preferredformat": "mp3",  # Format as mp3
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
    choice = input('''🎬 YouTube Video Downloader, choose a number to start:
    (1) Download a single video
    (2) Download all uploads from a channel
    (3) Exit
''').strip()
    if choice != "3":
        save_path = input('''What is the path for your downloads folder? (C:\\Users\\**<username>**\\Downloads)
''').strip().replace('/', '\\')

    if choice == "1":
        video_url = input("Enter the YouTube video URL:\n").strip()
        download_type = input('''Choose what type of download you want:
    (1) MP4, video + audio
    (2) MP3, audio only
''').strip()
        
        if download_type == '1':
            download_type = 'mp4'
        elif download_type == '2':
            download_type = 'mp3'
        else:
            print('❌ Invalid option, please choose 1 for MP4 or 2 for MP3.')
            return

        download_video(video_url, save_path, download_type)

    elif choice == "2":
        channel_url = input("Enter the YouTube channel's 'Videos' page URL:\n").strip()
        video_urls = get_video_links(channel_url)

        if video_urls:
            print(f"🔍 Found {len(video_urls)} videos. Downloading all...")
            for link in video_urls:
                download_type = input('''Choose what type of download you want:
    (1) MP4, video + audio
    (2) MP3, audio only
''').strip()
                
                if download_type == '1':
                    download_type = 'mp4'
                elif download_type == '2':
                    download_type = 'mp3'
                else:
                    print('❌ Invalid option, please choose 1 for MP4 or 2 for MP3.')
                    continue

                download_video(link, save_path, download_type)
        else:
            print("❌ No videos found.")
    elif choice == "3":
        repeat = 0
        return repeat
    else:
        print("❌ Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    repeat = 1
    while repeat > 0:
        repeat = main(repeat)
    print('Goodbye!!!')
