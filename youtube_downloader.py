
import os

video_url = input("Enter YouTube video URL: ")
command = f'yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 "{video_url}"'
os.system(command)

print("Download complete!")
