# Deployment and Build Instructions

## Prerequisites
- Python 3.10.10
- FFmpeg

## Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/telegram-speech-recognition-bot.git
    cd telegram-speech-recognition-bot
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Token**:
    - Create a new bot on Telegram via [@botFather](https://t.me/botfather).
    - Copy `config/_example/botToken.py` to `config/prod/botToken.py` and/or `config/dev/botToken.py`.
    - Replace the placeholder `API_TOKEN` with your actual API token.

4. **Run the Bot**:
    ```bash
    python -m TelegramSpeechRecognitionBot
    ```

## Notes
- Ensure `config/botSettings.py` is configured correctly for your environment.
- For development, use the `--dev` flag to enable debug mode:
    ```bash
    python -m TelegramSpeechRecognitionBot --dev
    ```
```