import os
import sys
import subprocess
import time

# Set your AWS credentials
aws_access_key_id = 'YOUR ACCESS KEY' # Replace with your S3 bucket name
aws_secret_access_key = 'SECRET KEY' # Replace with your S3 bucket name
s3_bucket_name = 'BUCKET NAME'  # Replace with your S3 bucket name

# Specify the local directory path to upload
local_directory = r'C:\\Users\\Nitesh\\Local Files\\'

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
                f's3://{s3_bucket_name}/{s3_path}',
              
            ]

            # Run the S3 sync command using subprocess
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Sync attempt {attempt + 1} failed with error: {str(e)}")
            time.sleep(retry_delay)
    
    return False

if __name__ == '__main__':
    if not os.path.exists(local_directory):
        print("Local directory not found.")
        sys.exit(1)
    
    # Specify the S3 path (prefix) where you want to sync
    s3_path = 'Remote:' # Describe your S3 Path
    
    if sync_with_retry(local_directory, s3_path):
        print("Sync completed successfully.")
    else:
        print("Sync failed after multiple retry attempts.")
import os
import sys
import subprocess
import time

# Set your AWS credentials
aws_access_key_id = 'YOUR ACCESS KEY' # Replace with your S3 bucket name
aws_secret_access_key = 'SECRET KEY' # Replace with your S3 bucket name
s3_bucket_name = 'BUCKET NAME'  # Replace with your S3 bucket name

# Specify the local directory path to upload
local_directory = r'C:\\Users\\Nitesh\\Local Files\\'

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
                f's3://{s3_bucket_name}/{s3_path}',
              
            ]

            # Run the S3 sync command using subprocess
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Sync attempt {attempt + 1} failed with error: {str(e)}")
            time.sleep(retry_delay)
    
    return False

if __name__ == '__main__':
    if not os.path.exists(local_directory):
        print("Local directory not found.")
        sys.exit(1)
    
    # Specify the S3 path (prefix) where you want to sync
    s3_path = 'Remote:' # Describe your S3 Path
    
    if sync_with_retry(local_directory, s3_path):
        print("Sync completed successfully.")
    else:
        print("Sync failed after multiple retry attempts.")
