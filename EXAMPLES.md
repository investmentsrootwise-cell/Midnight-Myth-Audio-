# Examples

This directory contains example scripts and usage patterns for the Midnight Myth Audio system.

## Example 1: Basic Audio Script Generation

```python
from audio_script_generator import AudioScriptGenerator

# Initialize the generator
generator = AudioScriptGenerator()

# Create chapter data
chapter = {
    "title": "The Fox Demon's Awakening",
    "content": "In the ancient forest, a fox demon stirs..."
}

# Generate audio script
result = generator.generate_chapter_audio_script(
    ebook_id="ebook_fox_demon_001",
    chapter=chapter,
    chapter_number=1,
    myth_theme="Japanese yokai horror",
    affiliate_hook="Share the legend and earn mythic badges"
)

print(f"✅ Script generated: {result['script_id']}")
```

## Example 2: Multiple Chapters Generation

```python
from audio_script_generator import AudioScriptGenerator

generator = AudioScriptGenerator()
ebook_id = "ebook_midnight_chronicles"

chapters = [
    {"title": "The Summoning", "content": "..."},
    {"title": "The Awakening", "content": "..."},
    {"title": "The Hunt Begins", "content": "..."}
]

for i, chapter in enumerate(chapters, start=1):
    result = generator.generate_chapter_audio_script(
        ebook_id=ebook_id,
        chapter=chapter,
        chapter_number=i,
        myth_theme="time-travel horror",
        affiliate_hook="Join the chronicle"
    )
    print(f"Chapter {i} completed: {result['script_id']}")

# View session progress
progress = generator.get_session_progress()
print(f"\n📊 Total events tracked: {len(progress)}")
```

## Example 3: Custom Theme Generation

```python
from audio_script_generator import AudioScriptGenerator

generator = AudioScriptGenerator()

themes = {
    "vampire": "Gothic Victorian vampire lore",
    "werewolf": "Full moon transformation horror",
    "ghost": "Haunted mansion spectral mystery"
}

for theme_key, theme_desc in themes.items():
    chapter = {
        "title": f"Tale of the {theme_key.title()}",
        "content": f"A story of {theme_desc}..."
    }
    
    result = generator.generate_chapter_audio_script(
        ebook_id=f"ebook_{theme_key}",
        chapter=chapter,
        chapter_number=1,
        myth_theme=theme_desc,
        affiliate_hook=f"Share the {theme_key} legend"
    )
```

## Example 4: Accessing Generated Data

```python
import json
from audio_script_generator import AudioScriptGenerator

generator = AudioScriptGenerator()

# Generate a script...
result = generator.generate_chapter_audio_script(...)

# Read the generated audio script
with open('data/audio_scripts.json', 'r') as f:
    scripts = json.load(f)
    script = scripts[result['script_id']]
    print(f"Title: {script['title']}")
    print(f"Duration: {script['estimated_duration']}")
    print(f"Number of script elements: {len(script['script'])}")

# Read grant logs
with open('data/grant_logs.json', 'r') as f:
    logs = json.load(f)
    print(f"Total grant logs: {len(logs)}")

# Read notifications
with open('data/notifications.json', 'r') as f:
    notifications = json.load(f)
    for notif in notifications:
        print(f"📢 {notif['title']}: {notif['message']}")
```

## Example 5: Session Progress Analysis

```python
from audio_script_generator import AudioScriptGenerator
from datetime import datetime

generator = AudioScriptGenerator()

# Generate multiple chapters...

# Analyze progress
progress = generator.get_session_progress()

print(f"Total events: {len(progress)}")
print(f"First event: {progress[0]['event']} at {progress[0]['timestamp']}")
print(f"Last event: {progress[-1]['event']} at {progress[-1]['timestamp']}")

# Count event types
event_types = {}
for entry in progress:
    event = entry['event']
    event_types[event] = event_types.get(event, 0) + 1

print("\nEvent Distribution:")
for event, count in event_types.items():
    print(f"  {event}: {count}")
```

## Example 6: Error Handling

```python
from audio_script_generator import AudioScriptGenerator

generator = AudioScriptGenerator()

try:
    result = generator.generate_chapter_audio_script(
        ebook_id="ebook_001",
        chapter={"title": "Test"},
        chapter_number=1
    )
    print("✅ Success!")
except Exception as e:
    print(f"❌ Error: {e}")
    # The system will still track progress even on error
    progress = generator.get_session_progress()
    print(f"Events tracked: {len(progress)}")
```

## Running Examples

To run any of these examples:

1. Save the example code to a file (e.g., `example1.py`)
2. Make sure you have the required dependencies installed
3. Run: `python3 example1.py`

For production use with actual Gemini AI:
```bash
export GOOGLE_API_KEY="your-api-key-here"
python3 your_script.py
```
