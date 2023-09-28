from lib.track_playlist import MusicTracker

def test_empty_music_tracker():
    """
    Given an empty music tracker
    #add_track adds a track to the list
    #view_listened_tracks returns an empty list
    """
    tracker = MusicTracker()
    tracker.add_track("Song 1")
    assert tracker.view_listened_tracks() == ["Song 1"]

def test_add_track():
    """
    Given a music tracker with one track added
    #view_listened_tracks returns a list with one track
    """
    tracker = MusicTracker()
    tracker.add_track("Song 1")
    assert tracker.view_listened_tracks() == ["Song 1"]

def test_multiple_tracks():
    """
    Given a music tracker with multiple tracks added
    #view_listened_tracks returns a list with all tracks in the order they were added
    """
    tracker = MusicTracker()
    tracker.add_track("Song 1")
    tracker.add_track("Song 2")
    tracker.add_track("Song 3")
    assert tracker.view_listened_tracks() == ["Song 1", "Song 2", "Song 3"]
