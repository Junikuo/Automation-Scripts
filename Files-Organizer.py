import os
import shutil

print("=== File Organizer ===")

folder = input("Enter the folder you want to organize: ")


files = os.listdir(folder)


for file in files:
    file_path = os.path.join(folder, file)


    if os.path.isdir(file_path):
        continue

    
    name, extension = os.path.splitext(file)

    extension = extension.lower()  

    # 
    if extension in [".png", ".jpg", ".jpeg"]:
        category = "Images"
    elif extension in [".mp4", ".mov", ".avi"]:
        category = "Videos"
    elif extension in [".pdf", ".docx", ".txt"]:
        category = "Documents"
    else:
        category = "Others"

  
    category_path = os.path.join(folder, category)
    os.makedirs(category_path, exist_ok=True)


    shutil.move(file_path, os.path.join(category_path, file))

print("Organization complete!")
