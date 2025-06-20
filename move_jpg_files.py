import os
import shutil

source_folder = r"C:\Users\alaga\Downloads"
destination_folder = r"D:\ROSHANI\codealpha"


os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")
