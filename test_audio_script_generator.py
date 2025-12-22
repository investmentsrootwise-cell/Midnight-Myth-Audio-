"""
Test suite for audio_script_generator module.
Tests session progress tracking, data persistence, and core functionality.
"""

import os
import json
import shutil
from audio_script_generator import AudioScriptGenerator, AUDIO_SCRIPT_TEMPLATE


def setup_test_environment():
    """Set up clean test environment."""
    if os.path.exists('data'):
        shutil.rmtree('data')
    os.makedirs('data', exist_ok=True)


def test_session_progress_tracking():
    """Test that session progress is properly tracked."""
    print("Testing session progress tracking...")
    
    setup_test_environment()
    generator = AudioScriptGenerator()
    
    # Track some events
    generator.track_progress("Test event 1", {"data": "value1"})
    generator.track_progress("Test event 2", {"data": "value2"})
    
    # Get progress
    progress = generator.get_session_progress()
    
    assert len(progress) == 2, f"Expected 2 progress entries, got {len(progress)}"
    assert progress[0]['event'] == "Test event 1"
    assert progress[1]['event'] == "Test event 2"
    
    # Verify progress file was created
    assert os.path.exists('data/session_progress.json'), "Progress file not created"
    
    print("✓ Session progress tracking test passed")


def test_add_document():
    """Test document addition to collections."""
    print("Testing document addition...")
    
    setup_test_environment()
    generator = AudioScriptGenerator()
    
    # Add a document
    doc = {"title": "Test Script", "content": "Test content"}
    doc_id = generator.add_doc("test_collection", doc)
    
    assert doc_id.startswith("test_collection_"), f"Unexpected doc_id format: {doc_id}"
    
    # Verify document was saved
    assert os.path.exists('data/test_collection.json'), "Collection file not created"
    
    with open('data/test_collection.json', 'r') as f:
        data = json.load(f)
    
    assert doc_id in data, f"Document {doc_id} not found in collection"
    assert data[doc_id]['title'] == "Test Script"
    
    print("✓ Document addition test passed")


def test_broadcast():
    """Test broadcast notification system."""
    print("Testing broadcast system...")
    
    setup_test_environment()
    generator = AudioScriptGenerator()
    
    # Send a broadcast
    generator.send_broadcast(
        "Test Title",
        "Test Message",
        {"key": "value"}
    )
    
    # Verify notification was saved
    assert os.path.exists('data/notifications.json'), "Notifications file not created"
    
    with open('data/notifications.json', 'r') as f:
        notifications = json.load(f)
    
    assert len(notifications) == 1, f"Expected 1 notification, got {len(notifications)}"
    assert notifications[0]['title'] == "Test Title"
    assert notifications[0]['message'] == "Test Message"
    
    print("✓ Broadcast system test passed")


def test_generate_chapter_audio_script():
    """Test complete audio script generation workflow."""
    print("Testing complete audio script generation...")
    
    setup_test_environment()
    generator = AudioScriptGenerator()
    
    chapter = {
        "title": "The Midnight Summoning",
        "content": "Test content"
    }
    
    result = generator.generate_chapter_audio_script(
        ebook_id="test_ebook",
        chapter=chapter,
        chapter_number=1,
        myth_theme="fox-demon horror",
        affiliate_hook="Test hook"
    )
    
    # Verify result structure
    assert 'ebook_id' in result
    assert 'script_id' in result
    assert 'grant_log_id' in result
    assert result['ebook_id'] == "test_ebook"
    
    # Verify all files were created
    assert os.path.exists('data/audio_scripts.json')
    assert os.path.exists('data/grant_logs.json')
    assert os.path.exists('data/notifications.json')
    assert os.path.exists('data/session_progress.json')
    
    # Verify progress tracking
    progress = generator.get_session_progress()
    assert len(progress) >= 5, f"Expected at least 5 progress entries, got {len(progress)}"
    
    # Find specific events
    events = [entry['event'] for entry in progress]
    assert "Chapter audio script generation started" in events
    assert "Chapter audio script generation completed" in events
    
    print("✓ Complete audio script generation test passed")


def test_template_formatting():
    """Test that the audio script template can be formatted."""
    print("Testing template formatting...")
    
    formatted = AUDIO_SCRIPT_TEMPLATE.format(
        chapter_title="Test Chapter",
        theme="horror"
    )
    
    assert "Test Chapter" in formatted
    assert "horror" in formatted
    assert "JSON" in formatted
    
    print("✓ Template formatting test passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("Running Audio Script Generator Tests")
    print("="*60 + "\n")
    
    tests = [
        test_session_progress_tracking,
        test_add_document,
        test_broadcast,
        test_generate_chapter_audio_script,
        test_template_formatting
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    # Cleanup
    if os.path.exists('data'):
        shutil.rmtree('data')
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
