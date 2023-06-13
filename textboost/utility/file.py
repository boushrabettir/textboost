from dataclasses import dataclass
from typing import List


@dataclass
class File:
    """Struct to hold file related data"""

    file_path: str
    font_size: str
    bolding_per_word: str
    file_name: str
