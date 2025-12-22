# Midnight Myth Audio

Time travel fox-demon horror storytelling platform with AI-powered audio script generation.

## Overview

Midnight Myth Audio is a creative-tech platform that generates immersive audio scripts for horror stories using Google's Gemini AI. The system includes session progress tracking, grant compliance logging, and affiliate notification features.

## Features

- **AI-Powered Audio Script Generation**: Uses Gemini AI to create detailed audio scripts with narration, sound effects, music cues, and character dialogue
- **Session Progress Tracking**: Tracks all generation events and user data throughout the session
- **Grant Compliance Logging**: Logs all creative deliverables for grant compliance and reporting
- **Affiliate Notifications**: Broadcasts new content to affiliates for promotional purposes
- **Data Persistence**: Stores all scripts, logs, and notifications in JSON format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/investmentsrootwise-cell/Midnight-Myth-Audio-.git
cd Midnight-Myth-Audio-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

## Usage

### Basic Usage

```python
from audio_script_generator import AudioScriptGenerator

# Initialize the generator
generator = AudioScriptGenerator()

# Create chapter data
chapter = {
    "title": "The Midnight Summoning",
    "content": "In the depths of the forest..."
}

# Generate audio script
result = generator.generate_chapter_audio_script(
    ebook_id="ebook_001",
    chapter=chapter,
    chapter_number=1,
    myth_theme="fox-demon horror",
    affiliate_hook="Share this tale and earn mythic rewards"
)

print(f"Script ID: {result['script_id']}")
```

### Command Line Usage

```bash
python audio_script_generator.py
```

## Session Progress Tracking

The system automatically tracks all activities:

- Script generation start/completion
- Document additions to collections
- Notification broadcasts
- All events with timestamps and metadata

Progress is saved to `data/session_progress.json` and can be retrieved:

```python
progress = generator.get_session_progress()
for entry in progress:
    print(f"[{entry['timestamp']}] {entry['event']}")
```

## Data Structure

### Audio Script Format

```json
{
  "title": "Chapter Title",
  "ebookId": "ebook_001",
  "chapterNumber": 1,
  "script": [
    {"type": "narration", "text": "...", "timing": "..."},
    {"type": "sfx", "description": "..."},
    {"type": "music", "description": "..."},
    {"type": "dialogue", "character": "...", "text": "...", "emotion": "..."}
  ],
  "estimated_duration": "5 minutes",
  "theme": "fox-demon horror"
}
```

### Grant Log Format

```json
{
  "eventType": "ebook_created",
  "ebookId": "ebook_001",
  "metadata": {
    "chapter_number": 1,
    "theme": "fox-demon horror",
    "affiliate_hook": "..."
  },
  "created_at": "2025-12-22T09:00:00.000000"
}
```

### Notification Format

```json
{
  "title": "New Lore: The Midnight Summoning",
  "message": "A new chapter has manifested. Share to unlock mythic badges.",
  "metadata": {
    "ebookId": "ebook_001",
    "scriptId": "audio_scripts_20251222_090000_123456"
  },
  "timestamp": "2025-12-22T09:00:00.000000"
}
```

## API Reference

### AudioScriptGenerator

Main class for generating audio scripts with progress tracking.

#### Methods

- `__init__(api_key: Optional[str] = None)`: Initialize with Gemini API key
- `ai_generate_json(model_name: str, prompt: str) -> Dict`: Generate JSON content using Gemini AI
- `add_doc(collection: str, document: Dict) -> str`: Add document to a collection
- `send_broadcast(title: str, message: str, metadata: Dict) -> None`: Send broadcast notification
- `track_progress(event: str, data: Dict) -> None`: Track session progress
- `get_session_progress() -> list`: Get current session progress
- `generate_chapter_audio_script(...)`: Generate complete audio script for a chapter

## Development

### Project Structure

```
Midnight-Myth-Audio-/
├── audio_script_generator.py  # Main application
├── requirements.txt           # Python dependencies
├── .env.example              # Environment configuration template
├── .gitignore                # Git ignore rules
├── README.md                 # This file
├── LICENSE                   # License file
└── data/                     # Generated data (gitignored)
    ├── audio_scripts.json
    ├── grant_logs.json
    ├── notifications.json
    └── session_progress.json
```

## Important Notes

### Concurrency

The current implementation uses file-based JSON storage, which is suitable for single-user/single-process scenarios. For production environments with concurrent access requirements, consider:

- Implementing file locking mechanisms
- Using a proper database (PostgreSQL, MongoDB, etc.)
- Adding queue-based processing for write operations

### API Keys

For production use with actual Gemini AI generation:
- Set the `GOOGLE_API_KEY` environment variable
- Keep your API keys secure and never commit them to version control
- Use the `.env` file for local development (already gitignored)

## License

GNU General Public License v3.0 - See LICENSE file for details

## Author

Robert Stokes - Founder of Midnight Myth Audio

