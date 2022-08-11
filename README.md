# azure-blob-manager
Python wrapper for Microsoft azure-storage-blob library

## Install
pip install azure-blob-manager --extra-index-url https://jnguyen0220.github.io/python-library/

## Usage
```python
from az.blob.manager import AzureBlobManager

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
azure_blob_manager = AzureBlobManager(connect_str)
list_success, list_response = azure_blob_manager.list_blobs("sample") 
```