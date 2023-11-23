import logging
from pydub import AudioSegment


def split_file(file_path: str, duration_millis=6000) -> list[str]:
    try:
        audio = AudioSegment.from_file(file_path)
        parts = []

        for i in range(0, len(audio), duration_millis):
            part = audio[i : i + duration_millis]
            part_file_path = f"{file_path}_part{i}.mp3"
            part.export(part_file_path, format="mp3")
            parts.append(part_file_path)

        return parts
    except Exception as e:
        logging.error(f"Error al dividir el archivo: {e}")
        return []