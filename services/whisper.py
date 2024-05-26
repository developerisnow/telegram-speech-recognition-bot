import re
import logging
import aiohttp
import config.botSettings as config

async def transcribe_whisper_api(file_path, language):
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'rb') as f:
            audio_data = f.read()
        async with session.post(config.WHISPER_ASR_WEBSERVICE_URL, data={'file': audio_data, 'language': language}) as response:
            result = await response.json()
            return result['text']

