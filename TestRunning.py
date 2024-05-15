import unittest
import os
from pathlib import Path

def compute_path_without_file_name(path):
    return __name__[0:__name__.rfind('.') + 1]

def compute_test_files_in_directory(directory, test_file_name_ending, extension_size):
    return [file[:-extension_size] for file in os.listdir(directory) if file.endswith(test_file_name_ending)]

path = compute_path_without_file_name(__name__)
test_files = compute_test_files_in_directory(Path(__file__).parent, "Tests.py", 3)
for file in test_files:
    unittest.main(exit=False, module=path + file)