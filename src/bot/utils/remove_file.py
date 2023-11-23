import os


# Desc: Remove a file
def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"Removed: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
