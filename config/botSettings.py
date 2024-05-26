import os

# To download big files you should create new Telegram Client.
# Follow instructions at https://core.telegram.org/api/obtaining_api_id 
# and fulfill API_ID and API_HASH in botToken.py
download_big_files = os.getenv('DOWNLOAD_BIG_FILES', 'True') == 'True'

# Whisper speech recognition software's model options and their relative speed and size of DB:
# tiny (x32, 78MB), base(x16, 145MB), small(x6, 484MB), medium(x2, 1.5GB), large(x1, 3.1GB).
# These are general models. English-only models also exist. Check https://github.com/openai/whisper .
whisper_model = os.getenv('WHISPER_MODEL', 'tiny')

# Selecting the Speech Recognition Library: 'whisper' or 'vosk'
speech_recognition_lib = os.getenv('SPEECH_RECOGNITION_LIB', 'whisper')

# Path to the Language Models Folder for vosk
vosk_models_path = os.getenv('VOSK_MODELS_PATH', 'vosk_models')