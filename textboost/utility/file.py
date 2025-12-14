from dataclasses import dataclass
from typing import List


@dataclass
class File:
    """Struct to hold file related data"""

    file_path: str

    file_name: str


@dataclass
class FileUtilizer:
    """Struct which holds the current List[File]"""

    list: List[File]