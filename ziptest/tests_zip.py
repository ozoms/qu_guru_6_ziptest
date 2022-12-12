#from zipfile import ZipFile
import pathlib
import zipfile
import os
import shutil

current_dir = os.path.abspath(os.path.dirname(__file__))
resources_dir = os.path.join(current_dir, 'resources')
directory = pathlib.Path(resources_dir)

with zipfile.ZipFile('testzip.zip', mode="w") as archive:
    for file_path in directory.iterdir():
        archive.write(file_path, arcname=file_path.name)

shutil.move('testzip.zip', directory)

resources_zip_dir = os.path.join(resources_dir, 'testzip.zip')
directory_testzip = pathlib.Path(resources_zip_dir)

with zipfile.ZipFile(directory_testzip, mode="r") as archive:
    name_info = archive.namelist()

assert ['tests_data.csv', 'tests_doc.pdf', 'tests_table.xlsx'] == name_info
