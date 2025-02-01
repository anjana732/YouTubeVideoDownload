# import os

# video_url = input("Enter YouTube video URL: ")

# # Use yt-dlp with Python
# command = f'python3 -m yt_dlp -f bestvideo+bestaudio --merge-output-format mp4 "{video_url}"'

# os.system(command)

# print("Download complete!")

import os

video_url = input("Enter YouTube video URL: ")

# Use yt-dlp with Python
command = f'python3 -m yt_dlp -f bestvideo+bestaudio --merge-output-format mp4 --audio-quality 0 "{video_url}"'

os.system(command)

print("Download complete!")
