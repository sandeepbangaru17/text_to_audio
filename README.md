# Text to Audio Converter (Sarvam.ai)

This project converts text from a `story.txt` file into an audio file (`audio.mp3`) using the Sarvam.ai Text-to-Speech (TTS) API.

## Prerequisites

- Python 3.8+
- Sarvam.ai API Key

## Setup (Recommended: Virtual Environment)

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your text in `story.txt`.
2. Ensure your virtual environment is active (`source venv/bin/activate`).
3. Run the script:
   ```bash
   python main.py
   ```
4. The output will be saved as `audio.mp3`.

## Audio Preview

Listen to the generated audio directly here:

<div align="center">
  <video controls src="https://github.com/ppavankumar19/text-to-audio/raw/main/audio.mp3" width="100%" height="50"></video>
  <br>
  <a href="https://github.com/ppavankumar19/text-to-audio/raw/main/audio.mp3" download><b>Download audio.mp3</b></a>
</div>

> **Note:** GitHub's security settings often block inline playback for files in the repository. If the player above is empty, please click **Download** or the **audio.mp3** file in the file list above to play it in GitHub's native player.

## Features

- Supports Indian English (`en-IN`), Telugu (`te-IN`), and other Indian languages.
- **Smart Chunking:** Automatically splits long text files to stay within API limits.
- **Native Experience:** Uses GitHub's secure, built-in player for the best audio quality.
