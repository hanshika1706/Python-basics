#duplicate_file_finder.py
import os
import hashlib

hashes = {}

for root, _, files in os.walk("."):
    for file in files:
        path = os.path.join(root, file)
        with open(path, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        if file_hash in hashes:
            print("Duplicate:", path)
        else:
            hashes[file_hash] = path
