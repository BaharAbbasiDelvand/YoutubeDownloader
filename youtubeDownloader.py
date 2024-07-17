import subprocess

def download_video(url, save_path):
    try:
        print(f"Downloading video from: {url}")
        result = subprocess.run(['yt-dlp', '-o', f'{save_path}/%(title)s.%(ext)s', url], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("Video downloaded")
        else:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"Error: {e}")

url = "https://www.youtube.com/watch?v=K-a8s8OLBSE"
save_path = '/Users/baharabbasidelvand/Desktop'
download_video(url, save_path)
