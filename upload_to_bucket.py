import boto3

# connect to s3
s3 = boto3.resource("s3")

# open the file we want to send, store it in a variable called data
data = open("sampletext.txt", "rb")

# specify what bucket we are sending the file to, .put_object names the file and sends it's contents
s3.Bucket("tech230-ahmed-boto").put_object(Key="sampletext.txt", Body=data)