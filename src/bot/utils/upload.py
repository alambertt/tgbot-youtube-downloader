from telegram import Bot
from telegram.ext import ContextTypes
from telegram.constants import ChatAction
from telegram.error import TelegramError
from .tg_logger import send_exception_log
import logging


async def send_file(
    chat_id: int, file_path: str, context: ContextTypes.DEFAULT_TYPE
) -> None:
    bot = context.bot
    try:
        await bot.send_chat_action(chat_id=chat_id, action=ChatAction.UPLOAD_DOCUMENT)
        with open(file_path, "rb") as file:
            await bot.send_document(chat_id=chat_id, document=file)
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
