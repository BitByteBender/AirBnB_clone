#!/usr/bin/python3
""" Creation of unique FileStorage instance """
import sys
from .engine.file_storage import FileStorage


sys.path.append('.')
storage = FileStorage()
storage.reload()
