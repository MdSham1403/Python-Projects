from pytube import YouTube

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path)
        print("Download successful!")

    except Exception as e:
        print(f"Download failed: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_folder = input("Enter the output folder path: ")
    download_video(video_url, output_folder)
