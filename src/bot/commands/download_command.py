from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction
from bot.utils import remove_file
from bot.utils import tg_logger
from bot.utils import validate_url
from youtube.downloader.download import download_audio
from bot.utils.upload import send_file
from bot.utils.remove_file import remove_file


async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        message_text = update.message.text
        user = update.effective_user
        _, url = message_text.split(" ", 1)

        if not validate_url.is_youtube_url(url) or not validate_url.is_url(url):
            await update.message.reply_text("Youtube URL invalid")
            return
        await tg_logger.send_log(
            f"Downloading audio from YouTube... Ask by {user.mention_html()}",
            context=context,
        )
    except ValueError:
        await update.message.reply_text(
            "Please provide a YouTube URL. Usage: /download <URL>"
        )
        return
    try:
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.RECORD_VOICE
        )

        audio_file_path = download_audio(url)

        if audio_file_path:
            name_file = audio_file_path.split("/")[-1]
            await tg_logger.send_log(f"Uploading audio: {name_file}", context=context)
            await send_file(update.effective_chat.id, audio_file_path, context)
            remove_file(audio_file_path)
        else:
            await tg_logger.send_exception_log(
                "Failed to download audio.", context=context
            )
            await update.message.reply_text("Failed to download audio.")
            return None

    except Exception as e:
        await tg_logger.send_exception_log(str(e), context=context)
        return None
