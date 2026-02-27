from project.song import Song

class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song in self.songs:
            return f"Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song = next((song for song in self.songs if song.name == song_name), None)
        if song is None:
            return f"Song is not in the album."
        if self.published:
            return f"Cannot remove songs. Album is published."
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        final_details = []
        final_details.append(f"Album {self.name}")
        for song in self.songs:
            final_details.append(f"== {Song.get_info(song)}")
        return "\n".join(final_details)