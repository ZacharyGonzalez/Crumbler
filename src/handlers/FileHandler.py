import os

class FileHandler:
    def __init__(self, file_path: str = ""):
        self.file_path = file_path

    @staticmethod
    def load_path(filename: str) -> str:
        base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "test_files", "images")
        return os.path.abspath(os.path.join(base_dir, filename))
