def is_youtube_url(url: str) -> bool:
    if "youtube.com" in url or "youtu.be" in url:
        return True
    else:
        return False
    
def is_url(url: str) -> bool:
    return True if "http://" in url or "https://" in url else False
    