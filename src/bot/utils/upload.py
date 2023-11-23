import os
import logging
from telegram.ext import ContextTypes
from telegram.error import TelegramError
from telegram.constants import ChatAction
from bot.utils.split_file import split_file
from bot.utils.remove_file import remove_file
from .tg_logger import *

MAX_FILE_SIZE = 50 * 1024 *1024 # 50MB


async def send_file(
    chat_id: int, file_path: str, context: ContextTypes.DEFAULT_TYPE
) -> None:
    bot = context.bot
    try:
        if not check_file_size(file_path):
            await bot.send_message(chat_id=chat_id, text="The file is too large.")
            remove_file(file_path)
            #TODO split file and send it
            # files = split_file(file_path)
            # for part_file in files:
            #     await send_log(f"Uploading audio: {part_file}", context=context)
            #     with open(part_file, "rb") as file_obj:
            #         await bot.send_audio(chat_id=chat_id, audio=file_obj)
            #         remove_file(part_file)
            return
        else:
            await bot.send_chat_action(
                chat_id=chat_id, action=ChatAction.UPLOAD_DOCUMENT
            )
            await send_log(f"Uploading audio: {file_path}", context=context)
            with open(file_path, "rb") as file_obj:
                await bot.send_audio(chat_id=chat_id, audio=file_obj)
                remove_file(file_path)
    except FileNotFoundError:
        msg = f"El archivo no fue encontrado: {file_path}"
        logging.error(msg)
        await send_exception_log(msg, context=context)
    except TelegramError as e:
        msg = f"Error al enviar el archivo: {e}"
        logging.error(msg)
        await send_exception_log(msg, context=context)
    except Exception as e:
        msg = f"Error desconocido: {e}"
        logging.error(msg)
        await send_exception_log(msg, context=context)


def check_file_size(file_path: str) -> bool:
    try:
        file_size = os.path.getsize(file_path)
        if file_size > MAX_FILE_SIZE:
            return False
        return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Unknown error occurred: {e}")
        return False
