import os.path
from os import path

def does_path_exist(path):
  return os.path.exists(path)

def make_directory_if_not_exists(path):
  if not does_path_exist(path):
    os.makedirs(path)

def remove_file(path):
  if does_path_exist(path):
    os.remove(path)

def remove_directory(path):  
  if does_path_exist(path):
    os.rmdir(path)