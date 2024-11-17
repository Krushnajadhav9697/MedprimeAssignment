import os

def rename_files(folder_name):

    if not os.path.isdir(folder_name):
        print(f"The folder '{folder_name}' does not exist")
        return 

    all_files=[]
    for file in os.listdir(folder_name):
        if os.path.isfile(os.path.join(folder_name,file)):
            all_files.append(file)

    all_files=sorted(all_files)
    
    if not all_files:
        print('The folder is empty. No files to rename')
        return

    for i , file_name in enumerate(all_files,start=1):
        file_path=os.path.join(folder_name,file_name)
        file_extension=os.path.splitext(file_name)[1]
        new_name=f'{i}{file_extension}'
        new_file_path=os.path.join(folder_name,new_name)

        try:
            os.rename(file_path,new_file_path)
            print(f"File '{file_name}' reaname to '{new_name}'")
        except PermissionError:
            print(f"Unable to rename file '{file_name}' due to permission issues")
        except Exception as e:
            print(f"cant rename file due to {e}")

    print('Renaming Completed')


if __name__ =='__main__':
    folder_path=input('Enter the folder path :')
    rename_files(folder_path)


    