import os
from google.cloud import storage


'''
Upload files to bucket in Storage.
'''
def upload(blob_name,file_path,bucket_name):
    try:
        '''
        - GOOGLE_APPLICATION_CREDENTIALS name is used by default by the library.
        - STORAGE_BUCKET_NAME abstracted for protection.
        '''
        GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
        STORAGE_BUCKET_NAME = os.environ.get('STORAGE_BUCKET_NAME')
        bucket_name = STORAGE_BUCKET_NAME

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        
        '''
        uploads to cloud storage.
        '''
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        
        '''
        removes json file from directory.
        '''
        os.remove(file_path)
        return True
    
    except Exception as e:
        print(e)
        return False


    


