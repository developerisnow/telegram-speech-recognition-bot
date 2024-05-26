# V 1.0.0
## Non-tech Description with List of Features 

This Telegram bot converts voice messages into text using speech recognition. It supports multiple languages, making it versatile for multi-language chats or personal use.

### Features
- Supports English, Russian, Ukrainian, and Portuguese languages for speech recognition.
- Allows users to choose the language of the voice message for accurate transcription.
- Built on the aiogram and [openAI-Whisper](https://github.com/openai/whisper) libraries for efficient and easy-to-maintain code.

## Tech

### Key Components
- **TelegramBot**: Handles main bot functionalities.
- **VoiceRecognitionStates, ErrorStates, FinishStates**: Manage different states.
- **Services**: Utility functions for file handling and speech recognition.
- **Config**: Holds configuration settings.

### Flow
1. **Start**: User starts the bot.
2. **Help**: User requests help.
3. **Voice Message Handling**: Bot processes voice messages.
4. **Language Choice**: User selects the language for transcription.
5. **Transcription**: Bot transcribes the voice message and sends the text back to the user.

### Configuration
- **download_big_files**: Boolean to download large files.
- **whisper_model**: Specifies the Whisper model to use.
- **speech_recognition_lib**: Chooses between 'whisper' or 'vosk'.
- **vosk_models_path**: Path to Vosk language models.

# v 1.1.0
- [x] use instead of 'whisper' package for speech recognition external api with endpoint 'WHISPER_ASR_WEBSERVICE_URL' in botToken.py
- [ ] use instead of 'whisper' package for speech recognition external api with endpoint 'WHISPER_ASR_WEBSERVICE_URL' in botToken.py