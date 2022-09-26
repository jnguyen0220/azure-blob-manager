import os
from azure.storage.blob import BlobServiceClient, ContainerClient

MESSAGE_CONTAINER_DOESNT_EXIST = "Container doesn't exist"

def list_blobs(container):
    try:
        return [True, container.list_blobs()] 
    except Exception as e:
        return [False, e]

def upload_blob(container, blob_name, data, isSas = False):
    if not isSas and not container.exists():
        container.create_container()
    try:
        client = container.get_blob_client(blob_name)
        return [True, client.upload_blob(data)] 
    except Exception as e:
        return [False, e]

def download_blob(container, path):
    try:
        return [True, container.download_blob(path).readall()]
    except Exception as e:
        return [False, e]


class AzureBlobManager:
    def __init__(self, connection_string):
        self.connection = BlobServiceClient.from_connection_string(connection_string)

    def list_blobs(self, container_name):
        container = self.connection.get_container_client(container_name)
        return list_blobs(container)

    def upload_blob(self, container_name, blob_name, data):
        container = self.connection.get_container_client(container_name)
        return upload_blob(container, blob_name, data)

    def download_blob(self, container_name, path):
        container =  self.connection.get_container_client(container_name)
        return download_blob(container, path)
    
class AzureBlobSas:
    def __init__(self, sas_url):
        self.container = ContainerClient.from_container_url(sas_url)
    
    def list_blobs(self):
        return list_blobs(self.container)

    def upload_blob(self, blob_name, data):
        return upload_blob(self.container, blob_name, data, isSas=True)

    def download_blob(self, path):
        return download_blob(self.container, path)

if __name__ == "__main__":
    f = bytes("some initial text data",'UTF-8') 
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    azure_blob_manager = AzureBlobManager(connect_str)
    list_success, list_response = azure_blob_manager.list_blobs("sample")
    upload_success, upload_response = azure_blob_manager.upload_blob("sample","sample/test2.txt", f)
    download_success, download_response = azure_blob_manager.download_blob("sample","sample/test2.txt")

    print("Container", list_success, upload_success, download_success)

    sas_str = os.getenv('AZURE_SAS_URL')
    azure_sas = AzureBlobSas(sas_str)
    list_success, list_response = azure_sas.list_blobs()
    upload_success, upload_response = azure_sas.upload_blob("data/jonny-test.txt", f)
    download_success, download_response = azure_sas.download_blob("data/jonny-test.txt")

    print("SAS", list_success, upload_success, download_success)