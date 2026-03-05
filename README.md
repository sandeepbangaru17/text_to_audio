# Text to Audio Converter (Sarvam.ai)

This project converts text from a `story.txt` file into an audio file (`audio.mp3`) using the Sarvam.ai Text-to-Speech (TTS) API.

## Prerequisites

- Python 3.8+
- Sarvam.ai API Key

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file from the template and add your Sarvam.ai API key:
   ```bash
   cp .env.example .env
   ```
   Then, edit `.env` and replace `YOUR_API_KEY_HERE` with your actual key.

## Usage

1. Place your text in `story.txt`.
2. Run the script:
   ```bash
   python main.py
   ```
3. The output will be saved as `audio.mp3`.

## Features

- Supports Indian English (`en-IN`) by default.
- Handles text reading from `story.txt`.
- Saves output directly to MP3 format.
