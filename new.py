import os
import sys
import subprocess
import time

# Set your AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'SECRET_KEY'
s3_bucket_name = 'BUCKET_NAME'  # Replace with your S3 bucket name

# Specify the local directory path to upload
local_directory = r'C:\Users\Nitesh\Local Files\\'

# Function to run the S3 sync command with retry logic
def sync_with_retry(local_path, s3_path):
    max_retries = 50  # You can adjust the number of retry attempts
    retry_delay = 30  # Delay in seconds before each retry

    for attempt in range(max_retries):
        try:
            # Construct the S3 sync command
            command = [
                'aws', 's3', 'sync',
                local_path,
                's3://{}/{}'.format(s3_bucket_name, s3_path),  # Use string formatting for compatibility
            ]

            # Run the S3 sync command using subprocess.call
            subprocess.call(command, stderr=subprocess.STDOUT, shell=True)

            return True
        except subprocess.CalledProcessError as e:
            print('Sync attempt {} failed with error: {}'.format(attempt + 1, str(e)))  # Use string formatting
            time.sleep(retry_delay)
    
    return False

if __name__ == '__main__':
    if not os.path.exists(local_directory):
        print("Local directory not found.")
        sys.exit(1)
    
    # Specify the S3 path (prefix) where you want to sync
    s3_path = 'Remote:'  # Describe your S3 Path
    
    if sync_with_retry(local_directory, s3_path):
        print("Sync completed successfully.")
    else:
        print("Sync failed after multiple retry attempts.")
