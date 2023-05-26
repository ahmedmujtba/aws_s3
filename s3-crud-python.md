# How to perform CRUD operations with AWS buckets using python

You will need to install python library called 'boto3' to interact with aws buckets, To do this:

- Run `pip install boto3` in relevant directory

## Access S3

To access any bucket (in our case that is S3), create a python file 'access_s3.py'

1. Import boto3 with `import boto3`
2. Connect with your bucket using the `resource` module, e.g.:

- `s3 = boto3.resource("s3")`

3. To obtain a list of buckets within this resource, create a for loop:

- `for bucket in s3.buckets.all():
print(bucket.name)`

## Create Bucket

import boto3

# connect to s3

```
s3 = boto3.client("s3")

#create a bucket on s3
bucket_name = s3.create_bucket(Bucket = "tech230-ahmed-boto", CreateBucketConfiguration = {"LocationConstraint": "eu-west-1"})

print(bucket_name)
```

## Upload to Bucket

```
import boto3

# connect to s3
s3 = boto3.resource("s3")

# open the file we want to send, store it in a variable called data
data = open("sampletext.txt", "rb")

# specify what bucket we are sending the file to, .put_object names the file and sends it's contents
s3.Bucket("tech230-ahmed-boto").put_object(Key="sampletext.txt", Body=data)
```

## Download from Bucket

```
import boto3

# connect to s3
s3 = boto3.client("s3")


# download from s3 bucket
s3.download_file("tech230-ahmed-boto", "sampletext.txt", "sampletext1.txt")

print(s3.download_file)
```

## Delete from Bucket

```
import boto3

# connect to s3
s3 = boto3.resource("s3")

# delete file in a specfic bucket
s3.Object("tech230-ahmed-boto", "sampletext.txt").delete()
```

## Delete Bucket

```
import boto3

# connect to s3
s3 = boto3.resource("s3")

#
bucket = s3.Bucket("tech230-ahmed-boto")
response = bucket.delete()

print(response)
```
