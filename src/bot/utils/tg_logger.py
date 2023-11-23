import os
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from dotenv import load_dotenv

load_dotenv()
CHANNEL_LOGS_ID = os.getenv("CHANNEL_LOGS_ID")
if not CHANNEL_LOGS_ID:
    raise ValueError("CHANNEL_LOGS_ID is not defined")


async def send_exception_log(msg: str, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_log(context=context, message=f"An error ocurred: \n\n <pre>{msg}</pre>")


async def send_log(message: str, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHANNEL_LOGS_ID, text=message, parse_mode=ParseMode.HTML
    )
