"""
Demo script to showcase session progress tracking functionality.
"""

from audio_script_generator import AudioScriptGenerator
import json

def main():
    print("=" * 70)
    print("Midnight Myth Audio - Session Progress Tracking Demo")
    print("=" * 70)
    print()
    
    # Initialize generator
    print("📦 Initializing AudioScriptGenerator...")
    generator = AudioScriptGenerator()
    print("✅ Generator initialized\n")
    
    # Generate three chapters
    chapters = [
        {"title": "The Awakening", "content": "A fox demon stirs..."},
        {"title": "The Hunt Begins", "content": "The villagers sense danger..."},
        {"title": "Midnight Confrontation", "content": "Time itself bends..."}
    ]
    
    ebook_id = "demo_ebook_midnight_myth"
    
    print("📝 Generating audio scripts for 3 chapters...\n")
    
    results = []
    for i, chapter in enumerate(chapters, start=1):
        print(f"Processing Chapter {i}: {chapter['title']}")
        result = generator.generate_chapter_audio_script(
            ebook_id=ebook_id,
            chapter=chapter,
            chapter_number=i,
            myth_theme="time-traveling fox-demon horror",
            affiliate_hook="Share the legend and unlock mythic badges"
        )
        results.append(result)
        print(f"  ✓ Script ID: {result['script_id']}")
        print(f"  ✓ Grant Log: {result['grant_log_id']}\n")
    
    # Display session progress
    print("=" * 70)
    print("📊 Session Progress Summary")
    print("=" * 70)
    print()
    
    progress = generator.get_session_progress()
    print(f"Total events tracked: {len(progress)}\n")
    
    # Count event types
    event_counts = {}
    for entry in progress:
        event = entry['event']
        event_counts[event] = event_counts.get(event, 0) + 1
    
    print("Event Distribution:")
    for event, count in sorted(event_counts.items()):
        print(f"  • {event}: {count}x")
    
    print("\n" + "=" * 70)
    print("📋 Recent Events (last 5)")
    print("=" * 70)
    print()
    
    for entry in progress[-5:]:
        timestamp = entry['timestamp'].split('T')[1][:8]  # Extract time
        event = entry['event']
        print(f"  [{timestamp}] {event}")
    
    print("\n" + "=" * 70)
    print("💾 Data Files Created")
    print("=" * 70)
    print()
    
    import os
    data_dir = 'data'
    if os.path.exists(data_dir):
        for filename in sorted(os.listdir(data_dir)):
            filepath = os.path.join(data_dir, filename)
            size = os.path.getsize(filepath)
            print(f"  • {filename} ({size:,} bytes)")
    
    print("\n" + "=" * 70)
    print("✅ Demo Complete!")
    print("=" * 70)
    print("\nTo view the data:")
    print("  cat data/session_progress.json | python3 -m json.tool")
    print("  cat data/audio_scripts.json | python3 -m json.tool")
    print("  cat data/grant_logs.json | python3 -m json.tool")
    print()

if __name__ == "__main__":
    main()
