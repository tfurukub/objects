# objects
# Parameters
ACCESS_KEY='hogehoge'
SECRET_KEY='hogehoge'
SERVER = 'http://xx.xx.xx.xx'
ACCESS_KEY and SECRET_KEY can be created on Prism Central

# List all Buckets/Folders/Files
python3.6 object.py list

# Create Bucket
python3.6 objects.py create_bucket <bucket name>

# Delete Bucket
python3.6 objects.py delete_bucket <bucket name>

# Upload file (only one file)
python3.6 objects.py upload <filename on local> <bucket name> <filename(=Key) on Objects>

# Download file (only one file)
python3.6 objects.py download <bucket name> <filename(=Key) on Objects> <filename on local>

# Delete file (only one file)
python3.6 objects.py delete_file <bucket name> <filename(=Key) on Objects>
