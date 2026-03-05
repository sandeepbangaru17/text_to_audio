import os
import base64
import requests
import json
from dotenv import load_dotenv

# Set your target language here (e.g., 'te-IN' for Telugu, 'hi-IN' for Hindi, 'en-IN' for English)
TARGET_LANGUAGE = "te-IN"
SPEAKER = "shubh"
MODEL = "bulbul:v3"
MAX_CHARS_PER_CHUNK = 2000

def get_audio_from_api(text, language_code):
    """
    Calls Sarvam.ai's TTS API for a single chunk of text.
    """
    api_key = os.getenv("SARVAM_API_KEY")
    if not api_key:
        print("Error: SARVAM_API_KEY not found in environment.")
        return None

    url = "https://api.sarvam.ai/text-to-speech"
    payload = {
        "text": text,
        "target_language_code": language_code,
        "speaker": SPEAKER,
        "model": MODEL
    }
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "audios" in data and len(data["audios"]) > 0:
            return base64.b64decode(data["audios"][0])
    except Exception as e:
        print(f"Error calling API: {e}")
        if hasattr(e, 'response') and e.response:
            print("Response:", e.response.text)
    return None

def chunk_text(text, max_len=MAX_CHARS_PER_CHUNK):
    """
    Splits text into chunks of roughly max_len, trying not to break sentences.
    """
    chunks = []
    while len(text) > max_len:
        split_at = text.rfind('.', 0, max_len)
        if split_at == -1: split_at = max_len
        chunks.append(text[:split_at + 1].strip())
        text = text[split_at + 1:].strip()
    if text:
        chunks.append(text)
    return chunks

def convert_text_to_audio(story_file="story.txt", output_file="audio.mp3"):
    load_dotenv()
    
    if not os.path.exists(story_file):
        print(f"Error: {story_file} not found.")
        return

    try:
        with open(story_file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    if not text:
        print("Error: Input file is empty.")
        return

    chunks = chunk_text(text)
    print(f"Processing {len(chunks)} chunk(s) for language: {TARGET_LANGUAGE}...")

    all_audio_data = []
    for i, chunk in enumerate(chunks):
        if len(chunks) > 1:
            print(f"Converting chunk {i+1}/{len(chunks)}...")
        
        audio_data = get_audio_from_api(chunk, TARGET_LANGUAGE)
        if audio_data:
            all_audio_data.append(audio_data)
        else:
            print(f"Failed to convert chunk {i+1}. Stopping.")
            return

    # Combine all chunks into one file
    with open(output_file, "wb") as f:
        for chunk_data in all_audio_data:
            f.write(chunk_data)
    
    print(f"Success! Combined audio saved as: {output_file}")

if __name__ == "__main__":
    convert_text_to_audio()
