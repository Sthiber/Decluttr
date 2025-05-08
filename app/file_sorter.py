import os
import shutil

def move_files_by_type(src_dir, file_types, dest_folder_name):
    if not os.path.exists(src_dir):
        raise FileNotFoundError("Source directory does not exist.")
    
    dest_path = os.path.join(src_dir, dest_folder_name)
    os.makedirs(dest_path, exist_ok=True)

    moved_count = 0

    for file in os.listdir(src_dir):
            full_path = os.path.join(src_dir, file)
            if os.path.isfile(full_path) and any(file.endswith(ext) for ext in file_types):
                shutil.move(full_path, os.path.join(dest_path, file))
                moved_count += 1
    
         
    return moved_count