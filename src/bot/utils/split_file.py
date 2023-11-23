import logging
from pydub import AudioSegment

MAX_AUDIO_DURATION = 45 * 60 * 1000  # 45 minutes


def split_file(file_path: str, duration_millis=MAX_AUDIO_DURATION) -> list[str]:
    try:
        audio = AudioSegment.from_file(file_path)
        parts = []
        part_index = 1

        for i in range(0, len(audio), duration_millis):
            part = audio[i : i + duration_millis]
            part_file_path = f"{file_path}_part{part_index}.mp3"
            part.export(part_file_path, format="mp3")
            parts.append(part_file_path)
            part_index += 1

        return parts
    except Exception as e:
        logging.error(f"Error al dividir el archivo: {e}")
        return []
