from pytube import YouTube
import os


def download_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()

        if audio is not None:
            out_file = audio.download(output_path="downloads")

            base, _ = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)

            print(f"Downloaded: {new_file}")
            return new_file
        else:
            print("Failed to download audio.")
            return None
    except Exception as e:
        print("Error:", e)
        return None
