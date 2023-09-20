import os
import shutil

source_dir = r"C:\Users\Asus\Desktop\dowlnloader\z2"
pendrive_dir = r"F:"

file_modifcation_times = {}

def take_inc_back_up(source_dir, pendrive_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            print(source_file_path)
            
            # modify the source file path to destination file path, saving another read operation on destination storage 
            destination_file_path = source_file_path.replace(source_dir, pendrive_dir)
            print(destination_file_path)
            
            # store the modification time of the file in the dictionary
            file_modifcation_times[source_file_path] = os.path.getmtime(source_file_path)
            print(file_modifcation_times[source_file_path])
            
            if (not os.path.exists(destination_file_path) or file_modifcation_times[source_file_path] > os.path.getmtime(destination_file_path)):
                shutil.copy2(source_file_path, destination_file_path)
                print(f"{destination_file_path}, copied successfully!!")
            else:
                print("Nothing to do... Already resolved!!")
            

take_inc_back_up(source_dir, pendrive_dir)