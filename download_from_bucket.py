import boto3

# connect to s3
s3 = boto3.client("s3")


# download from s3 bucket
s3.download_file("tech230-ahmed-boto", "sampletext.txt", "sampletext1.txt")

print(s3.download_file)