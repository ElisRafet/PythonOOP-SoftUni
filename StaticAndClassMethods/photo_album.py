from math import ceil
from typing import List

class PhotoAlbum:
    PAGE_SIZE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos: List[List[str]]= [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PAGE_SIZE))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < self.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        separator = "-" * 11 + "\n"
        result = separator
        for page in self.photos:
            result += " ".join("[]" for _ in page) + "\n"
            result += separator
        return result.strip()