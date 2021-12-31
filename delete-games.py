from tasks.mansion_saver import get_mansions_directory, setup_mansions_directory
import os

setup_mansions_directory()
mansions_directory = get_mansions_directory()
mansion_directories = os.listdir(mansions_directory)

# loop through directories
for mansion_directory in mansion_directories:
  mansion_dir_path = mansions_directory + mansion_directory
  mansion_files = os.listdir(mansion_dir_path)
  # loop through files
  for mansion_file in mansion_files:
    mansion_file_path = mansion_dir_path + "/" + mansion_file
    # remove file
    os.remove(mansion_file_path)
  # remove directory
  os.rmdir(mansion_dir_path)
  