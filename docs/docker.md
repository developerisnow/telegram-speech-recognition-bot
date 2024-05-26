# Docker Deployment Instructions

## Prerequisites
- Docker
- Docker Compose

## Steps

1. **Build the Docker Image**:
    ```bash
    docker build -t telegram-speech-recognition-bot .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -d -p 80:80 --name telegram-bot telegram-speech-recognition-bot
    ```

3. **Using Docker Compose**:
    - Create a `.env` file with your environment variables:
        ```plaintext
        API_TOKEN=your_api_token
        API_HASH=your_api_hash
        API_ID=your_api_id
        CLIENT_NAME=your_client_name
        DOWNLOAD_BIG_FILES=True
        WHISPER_MODEL=tiny
        SPEECH_RECOGNITION_LIB=whisper
        VOSK_MODELS_PATH=vosk_models
        ```
    - Run the container with Docker Compose:
        ```bash
        docker-compose -f docker-compose-prod.yml up -d
        ```

## Notes
- Ensure `config/botSettings.py` is configured correctly for your environment.
- For development, you can modify the `docker-compose-prod.yml` to mount local directories for live code updates.

