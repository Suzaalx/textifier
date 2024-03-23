
import yt_dlp

# Define the URLs to download


# Define the options for 
def download(URLS):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': './mp3/%(title)s',  # Specify the output location
        'ffmpeg-location': './mp3/',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            
        }]
    }

    # Download the video/audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

