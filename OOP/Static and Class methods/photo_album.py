class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        added_photo = False
        for page in self.photos:
            if len(page) < 4:
                added_photo = True
                page.append(label)
                slot_index = page.index(label)
                page_index = self.photos.index(page)
                return f"{label} photo added successfully on page {page_index+1} slot {slot_index+1}"
        if not added_photo:
            return f"No more free slots"

    def display(self):
        final_result = []
        final_result.append('-----------')
        for page in range(len(self.photos)):
            b = []
            if self.photos[page]:
                for photo in self.photos[page]:
                    b.append('[]')
            final_result.append(' '.join(b))
            final_result.append('-----------')

        return '\n'.join(final_result)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())