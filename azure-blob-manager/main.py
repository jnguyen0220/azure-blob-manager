import os
from azure.storage.blob import BlobServiceClient

MESSAGE_CONTAINER_DOESNT_EXIST = "Container doesn't exist"

class AzureBlobManager:
    def __init__(self, connection_string):
        self.connection = BlobServiceClient.from_connection_string(connection_string)

    def list_blobs(self, container_name):
        container = self.connection.get_container_client(container_name)
        return [True, container.list_blobs()] if container.exists() else [False, MESSAGE_CONTAINER_DOESNT_EXIST]

    def upload_blob(self, container_name, blob_name, data):
        container = self.connection.get_container_client(container_name)
        if not container.exists():
            container.create_container()
        try:
            client = container.get_blob_client(blob_name)
            return [True, client.upload_blob(data)] 
        except Exception as e:
            return [False, e]

    def download_blob(self, container_name, path):
        container =  self.connection.get_container_client(container_name)
        if container.exists():
            try:
                return [True, container.download_blob(path).readall()]
            except Exception as e:
                return [False, e]
        return [False, MESSAGE_CONTAINER_DOESNT_EXIST]
    
if __name__ == "__main__":
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    f = bytes("some initial text data",'UTF-8') 
    azure_blob_manager = AzureBlobManager(connect_str)
    list_success, list_response = azure_blob_manager.list_blobs("sample")
    upload_success, upload_response = azure_blob_manager.upload_blob("sample","sample/test2.txt", f)
    download_success, download_response = azure_blob_manager.download_blob("sample","sample/test2.txt")

    print(f"list_success:{list_success}", f"list_response:{list_response}")

    print(f"Upload_success:{upload_success}", f"upload_response:{upload_response}")

    if download_success:
        with open("my_file.txt", "wb") as file:
            file.write(download_response)

    print(f"download_success:{download_success}", f"download_response:{download_response}")