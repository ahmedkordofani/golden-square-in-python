class MusicTracker:
    def __init__(self):
        self.listened_tracks = []

    def add_track(self, track_name):
        self.listened_tracks.append(track_name)

    def view_listened_tracks(self):
        return self.listened_tracks
