import boto3

# connect to s3
s3 = boto3.resource("s3")

# delete file in a specfic bucket
s3.Object("tech230-ahmed-boto", "sampletext.txt").delete()