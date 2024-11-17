import os
import zipfile


def zipping_folder(folder_name):
    if not os.path.exists(folder_name):
        print(f"The Folder {folder_name} Not exist ")
        return
    
    if not os.path.isdir(folder_name):
        print(f"The folder {folder_name} is not derectory")
        return 
    
    zip_file=f"{folder_name}.zip"

    try:
        with zipfile.ZipFile(zip_file,'w',zipfile.ZIP_DEFLATED) as zip:
            for root,dirs,files in os.walk(folder_name):
                for dirs_name in dirs:
                    dir_path=os.path.join(root,dirs_name)
                    zip.write(dir_path,os.path.relpath(dir_path,os.path.dirname(folder_name)))

                for file_name in files:
                    file_path=os.path.join(root,file_name)
                    zip.write(file_path,os.path.relpath(file_path,os.path.dirname(folder_name)))

        print(f"zip file creted {zip_file}")
    except PermissionError:
        print("cant create zip file due to persission isshu")
    except Exception as e:
        print(f'Could not crete zip file due to {e} error')


if __name__=='__main__':
    
    folder_name=input("enter the folder name ")
    zipping_folder(folder_name)


