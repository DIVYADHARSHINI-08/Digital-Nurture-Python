import os
import shutil

source_folder = "source_files"
backup_folder = "backup_files"

copied_files = set()

os.makedirs(backup_folder, exist_ok=True)

try:
    files = os.listdir(source_folder)

    with open("backup.log", "a") as log_file:

        for file_name in files:

            source_path = os.path.join(source_folder, file_name)
            backup_path = os.path.join(backup_folder, file_name)

            if file_name in copied_files:
                log_file.write(f"Skipped duplicate: {file_name}\n")
                continue

            try:
                shutil.copy(source_path, backup_path)

                copied_files.add(file_name)

                log_file.write(f"Copied: {file_name}\n")

            except FileNotFoundError:
                log_file.write(f"File not found: {file_name}\n")

            except PermissionError:
                log_file.write(f"Permission denied: {file_name}\n")

    print("Backup completed successfully.")

except FileNotFoundError:
    print("Error: Source folder not found.")

except Exception as e:
    print("Error:", e)