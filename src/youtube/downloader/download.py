from pytube import YouTube
import os


def download_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        out_file = audio.download(output_path="downloads")

        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

        print(f"Descargado: {new_file}")
        return new_file
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    video_url = input("Ingresa la URL del video de YouTube: ")
    download_audio(video_url)
