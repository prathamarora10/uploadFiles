import dropbox 
import os
import shutil
from dropbox.files import WriteMode

class TransferData: 
    def __init__(self, access_token): 
        self.access_token = access_token 
        
    def upload_file(self, file_from, file_to): 
        dbx = dropbox.Dropbox(self.access_token) 

        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,  relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite') )

        
def main(): 
    access_token = "sl.A2RO9JN94j3OH04zSom6QkT1n-UN4UcRh1MU5pl-xJD16Np9L3LC3Z7I3IxtdKyssWcByrMjwvsdOBAJKZTOb3e6iXBj-igHi8BqLxgBv6MIcNK2wVqt7OqK7XAhhsflznZ77OU"
    transferData = TransferData(access_token) 
    file_from = '/Users/prathamarora/Downloads/Python_Projects/test.txt'
    file_to = '/pratham_c105/test.txt' 
    transferData.upload_file(file_from, file_to) 
    print("Uploaded Successfully !!")
 
if __name__ == '__main__': 
    main()
