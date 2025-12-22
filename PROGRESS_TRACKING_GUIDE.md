# Session Progress Tracking User Guide

## Overview

The Midnight Myth Audio system includes comprehensive session progress tracking that records every operation during audio script generation. This guide explains how to use and interpret the progress tracking features.

## What is Tracked?

The system automatically tracks:

1. **Script Generation Events**
   - When generation starts
   - When generation completes
   - Any errors or warnings

2. **Data Operations**
   - Document additions to collections
   - File writes and reads
   - Database operations

3. **Notifications**
   - Broadcast messages sent
   - Affiliate notifications
   - System alerts

4. **User Actions**
   - API calls
   - Configuration changes
   - Custom tracking points

## Progress Data Structure

Each progress entry contains:

```json
{
  "timestamp": "2025-12-22T09:00:00.000000",
  "event": "Event description",
  "data": {
    "key": "value",
    "additional": "metadata"
  }
}
```

### Fields

- **timestamp**: ISO 8601 formatted timestamp
- **event**: Human-readable event description
- **data**: Dictionary containing event-specific metadata

## Using Progress Tracking

### Automatic Tracking

Most operations are tracked automatically:

```python
from audio_script_generator import AudioScriptGenerator

generator = AudioScriptGenerator()

# This automatically tracks progress
result = generator.generate_chapter_audio_script(
    ebook_id="ebook_001",
    chapter={"title": "Chapter 1"},
    chapter_number=1
)

# View all tracked events
progress = generator.get_session_progress()
for entry in progress:
    print(f"[{entry['timestamp']}] {entry['event']}")
```

### Manual Tracking

You can also manually track custom events:

```python
generator = AudioScriptGenerator()

# Track a custom event
generator.track_progress(
    "Custom user action",
    {"user_id": "12345", "action": "preview_generated"}
)
```

## Accessing Progress Data

### In-Memory Access

```python
# Get current session progress
progress = generator.get_session_progress()

# Count events
total_events = len(progress)

# Filter by event type
script_events = [
    entry for entry in progress 
    if "script" in entry['event'].lower()
]
```

### File Access

Progress is automatically saved to `data/session_progress.json`:

```python
import json

# Read progress from file
with open('data/session_progress.json', 'r') as f:
    progress = json.load(f)

# Analyze progress
for entry in progress:
    timestamp = entry['timestamp']
    event = entry['event']
    print(f"{timestamp}: {event}")
```

## Common Use Cases

### 1. Debugging Issues

```python
generator = AudioScriptGenerator()

try:
    result = generator.generate_chapter_audio_script(...)
except Exception as e:
    # Check progress to see where it failed
    progress = generator.get_session_progress()
    last_event = progress[-1]
    print(f"Failed after: {last_event['event']}")
    print(f"Error data: {last_event['data']}")
```

### 2. Performance Monitoring

```python
from datetime import datetime

generator = AudioScriptGenerator()

# Generate content
start_time = datetime.now()
result = generator.generate_chapter_audio_script(...)
end_time = datetime.now()

# Analyze timing
progress = generator.get_session_progress()
print(f"Total time: {end_time - start_time}")
print(f"Events recorded: {len(progress)}")
```

### 3. Audit Trail

```python
# Generate multiple scripts
generator = AudioScriptGenerator()

for i in range(5):
    generator.generate_chapter_audio_script(
        ebook_id=f"ebook_{i}",
        chapter={"title": f"Chapter {i}"},
        chapter_number=i
    )

# Create audit report
progress = generator.get_session_progress()

# Count by event type
audit = {}
for entry in progress:
    event_type = entry['event']
    audit[event_type] = audit.get(event_type, 0) + 1

print("Audit Report:")
for event_type, count in audit.items():
    print(f"  {event_type}: {count} times")
```

### 4. User Activity Tracking

```python
generator = AudioScriptGenerator()

# Track user session start
generator.track_progress(
    "User session started",
    {"user_id": "user_123", "session_id": "session_456"}
)

# Generate content
result = generator.generate_chapter_audio_script(...)

# Track user action
generator.track_progress(
    "User downloaded script",
    {"script_id": result['script_id'], "format": "pdf"}
)

# Track session end
generator.track_progress(
    "User session ended",
    {"duration_minutes": 15}
)
```

## Progress File Format

The `data/session_progress.json` file contains an array of progress entries:

```json
[
  {
    "timestamp": "2025-12-22T09:00:00.000000",
    "event": "Chapter audio script generation started",
    "data": {
      "ebook_id": "ebook_001",
      "chapter_number": 1,
      "theme": "horror"
    }
  },
  {
    "timestamp": "2025-12-22T09:00:15.123456",
    "event": "Added document to audio_scripts",
    "data": {
      "doc_id": "audio_scripts_20251222_090015_123456"
    }
  }
]
```

## Best Practices

1. **Regular Review**: Periodically review progress logs to identify patterns or issues

2. **Custom Tracking**: Add custom tracking points for business-critical operations

3. **Data Retention**: Implement a strategy for archiving old progress logs

4. **Privacy**: Ensure progress logs don't contain sensitive user information

5. **Integration**: Use progress data for analytics, monitoring, and alerting

## Analytics Examples

### Event Timeline

```python
import matplotlib.pyplot as plt
from datetime import datetime

progress = generator.get_session_progress()

# Parse timestamps
times = [datetime.fromisoformat(e['timestamp']) for e in progress]
events = [e['event'] for e in progress]

# Plot timeline
plt.figure(figsize=(12, 6))
plt.scatter(times, range(len(times)))
plt.yticks(range(len(times)), events)
plt.xlabel('Time')
plt.title('Session Progress Timeline')
plt.tight_layout()
plt.savefig('progress_timeline.png')
```

### Success Rate

```python
progress = generator.get_session_progress()

# Count starts and completions
starts = sum(1 for e in progress if 'started' in e['event'])
completions = sum(1 for e in progress if 'completed' in e['event'])

success_rate = (completions / starts * 100) if starts > 0 else 0
print(f"Success Rate: {success_rate:.1f}%")
```

## Troubleshooting

### Progress Not Saving

If progress isn't being saved to file:

1. Check that the `data/` directory exists
2. Verify write permissions
3. Ensure disk space is available

### Missing Events

If expected events aren't tracked:

1. Verify you're using the same generator instance
2. Check for exceptions that interrupt tracking
3. Review the event tracking code

### Large Progress Files

If progress files become too large:

1. Implement log rotation
2. Archive old progress data
3. Add file size monitoring

## Support

For issues or questions about progress tracking:

1. Check the examples in `EXAMPLES.md`
2. Review the test suite in `test_audio_script_generator.py`
3. Open an issue on GitHub with progress log excerpts
