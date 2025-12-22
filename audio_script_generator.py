"""
Midnight Myth Audio - Audio Script Generator
Generates audio scripts for chapters with Gemini AI, tracks progress, and manages grant logging.
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

try:
    from google import genai
    GENAI_CLIENT = None
except ImportError:
    try:
        import google.generativeai as genai
        GENAI_CLIENT = None
    except ImportError:
        genai = None
        GENAI_CLIENT = None


# Audio script template
AUDIO_SCRIPT_TEMPLATE = """
Generate a detailed audio script for the following chapter:

Chapter Title: {chapter_title}
Theme: {theme}
Tone: Dark, mysterious, horror-themed
Target Audience: Mature audiences interested in mythic horror

The script should include:
1. Narrative text with dramatic pacing
2. Sound effect cues (e.g., [SFX: footsteps], [SFX: wind howling])
3. Music cues (e.g., [MUSIC: suspenseful], [MUSIC: crescendo])
4. Character dialogue with emotional direction
5. Timing suggestions for audio production

Format the response as JSON with the following structure:
{{
  "title": "Chapter title",
  "script": [
    {{"type": "narration", "text": "...", "timing": "..."}},
    {{"type": "sfx", "description": "..."}},
    {{"type": "music", "description": "..."}},
    {{"type": "dialogue", "character": "...", "text": "...", "emotion": "..."}}
  ],
  "estimated_duration": "minutes",
  "theme": "horror theme"
}}
"""


class AudioScriptGenerator:
    """Manages audio script generation and progress tracking."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the generator with API key."""
        self.api_key = api_key or os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        if self.api_key and genai:
            try:
                genai.configure(api_key=self.api_key)
            except AttributeError:
                # New API doesn't have configure method
                pass
        self.session_data = {}
        self.progress_log = []
    
    def ai_generate_json(self, model_name: str, prompt: str) -> Dict[str, Any]:
        """
        Generate JSON content using Gemini AI.
        
        Args:
            model_name: Name of the Gemini model to use
            prompt: Prompt for content generation
            
        Returns:
            Generated content as dictionary
        """
        if not genai:
            print("Warning: Gemini AI library not available. Using fallback data.")
            return self._get_fallback_script()
        
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            
            # Parse JSON from response
            text = response.text
            # Remove markdown code blocks if present
            if '```json' in text:
                text = text.split('```json')[1].split('```')[0]
            elif '```' in text:
                text = text.split('```')[1].split('```')[0]
            
            return json.loads(text.strip())
        except Exception as e:
            print(f"Error generating content: {e}")
            # Return a fallback structure
            return self._get_fallback_script(error=str(e))
    
    def _get_fallback_script(self, error: Optional[str] = None) -> Dict[str, Any]:
        """Get fallback script data when AI generation fails."""
        return {
            "title": "Generated Script",
            "script": [
                {
                    "type": "narration",
                    "text": "In the midnight hour, when shadows dance...",
                    "timing": "0:00-0:10"
                },
                {
                    "type": "sfx",
                    "description": "distant wolf howl"
                },
                {
                    "type": "music",
                    "description": "eerie atmospheric tension"
                }
            ],
            "estimated_duration": "5 minutes",
            "theme": "horror",
            **({"error": error} if error else {})
        }
    
    def add_doc(self, collection: str, document: Dict[str, Any]) -> str:
        """
        Add a document to a collection (simulated database).
        
        Args:
            collection: Collection name (e.g., 'audio_scripts', 'grant_logs')
            document: Document data to store
            
        Returns:
            Document ID
        """
        doc_id = f"{collection}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Store document in JSON file
        filepath = f"data/{collection}.json"
        
        # Load existing data
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
        else:
            data = {}
        
        # Add new document
        data[doc_id] = {
            **document,
            'id': doc_id,
            'created_at': datetime.now().isoformat()
        }
        
        # Save updated data
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        # Track progress
        self.track_progress(f"Added document to {collection}", {"doc_id": doc_id})
        
        return doc_id
    
    def send_broadcast(self, title: str, message: str, metadata: Dict[str, Any]) -> None:
        """
        Send a broadcast notification.
        
        Args:
            title: Notification title
            message: Notification message
            metadata: Additional metadata
        """
        notification = {
            'title': title,
            'message': message,
            'metadata': metadata,
            'timestamp': datetime.now().isoformat()
        }
        
        # Store notification
        os.makedirs('data', exist_ok=True)
        filepath = 'data/notifications.json'
        
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                notifications = json.load(f)
        else:
            notifications = []
        
        notifications.append(notification)
        
        with open(filepath, 'w') as f:
            json.dump(notifications, f, indent=2)
        
        print(f"📢 Broadcast sent: {title}")
        print(f"   Message: {message}")
        
        # Track progress
        self.track_progress("Broadcast sent", notification)
    
    def track_progress(self, event: str, data: Dict[str, Any]) -> None:
        """
        Track session progress for user data.
        
        Args:
            event: Event description
            data: Event data
        """
        progress_entry = {
            'timestamp': datetime.now().isoformat(),
            'event': event,
            'data': data
        }
        
        self.progress_log.append(progress_entry)
        
        # Save progress log
        os.makedirs('data', exist_ok=True)
        with open('data/session_progress.json', 'w') as f:
            json.dump(self.progress_log, f, indent=2)
    
    def get_session_progress(self) -> list:
        """
        Get current session progress.
        
        Returns:
            List of progress entries
        """
        return self.progress_log
    
    def generate_chapter_audio_script(
        self,
        ebook_id: str,
        chapter: Dict[str, Any],
        chapter_number: int,
        myth_theme: str = "horror",
        affiliate_hook: str = ""
    ) -> Dict[str, str]:
        """
        Generate audio script for a chapter with grant compliance logging.
        
        Args:
            ebook_id: eBook identifier
            chapter: Chapter data
            chapter_number: Chapter number
            myth_theme: Theme for the chapter
            affiliate_hook: Affiliate marketing hook
            
        Returns:
            Dictionary with ebook_id, script_id, and grant_log_id
        """
        # Track start of generation
        self.track_progress(
            "Chapter audio script generation started",
            {
                "ebook_id": ebook_id,
                "chapter_number": chapter_number,
                "theme": myth_theme
            }
        )
        
        # Generate audio script for this chapter
        script_prompt = AUDIO_SCRIPT_TEMPLATE.format(
            chapter_title=chapter.get("title", f"Chapter {chapter_number}"),
            theme=myth_theme
        )
        audio_script = self.ai_generate_json("gemini-2.0-flash-exp", script_prompt)
        audio_script["ebookId"] = ebook_id
        audio_script["chapterNumber"] = chapter_number
        script_id = self.add_doc("audio_scripts", audio_script)
        
        # Grant compliance: log the creation as a deliverable (internal)
        grant_log_id = self.add_doc("grant_logs", {
            "eventType": "ebook_created",
            "ebookId": ebook_id,
            "metadata": {
                "chapter_number": chapter_number,
                "theme": myth_theme,
                "affiliate_hook": affiliate_hook
            }
        })
        
        # Notify affiliates subtly (optional broadcast)
        self.send_broadcast(
            f"New Lore: {chapter.get('title', 'Chapter ' + str(chapter_number))}",
            "A new chapter has manifested. Share to unlock mythic badges.",
            {"ebookId": ebook_id, "scriptId": script_id}
        )
        
        # Track completion
        self.track_progress(
            "Chapter audio script generation completed",
            {
                "ebook_id": ebook_id,
                "script_id": script_id,
                "grant_log_id": grant_log_id
            }
        )
        
        return {
            "ebook_id": ebook_id,
            "script_id": script_id,
            "grant_log_id": grant_log_id
        }


def main():
    """Main function to demonstrate usage."""
    generator = AudioScriptGenerator()
    
    # Example chapter data
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
    
    print("\n✅ Audio Script Generation Complete!")
    print(f"   eBook ID: {result['ebook_id']}")
    print(f"   Script ID: {result['script_id']}")
    print(f"   Grant Log ID: {result['grant_log_id']}")
    
    # Display session progress
    print("\n📊 Session Progress:")
    for entry in generator.get_session_progress():
        print(f"   [{entry['timestamp']}] {entry['event']}")


if __name__ == "__main__":
    main()
