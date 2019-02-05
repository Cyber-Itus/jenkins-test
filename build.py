import os
import subprocess
import boto3

KEY = os.environ('S3_BUILD_KEY')
SECRET = os.environ('S3_BUILD_SECRET')
BUCKET = os.environ('S3_BUILD_BUCKET')

output = subprocess.check_output(['git', 'tag'])
current_tag = str(output.decode().strip())
print("### working on tag ... ####".format(current_tag))

# Make the archive file using the system commands
build_file = "consumer-service-{}.tar.gz".format(current_tag)
os.system("tar -cvf {}  consumer".format(build_file))
print("#### uploading ...######")
client = boto3.client("s3", config= boto3.session.Config(signature_version='s3v4'),
                            aws_access_key_id=KEY,
                            region_name="us-east-1",
                            aws_secret_access_key=SECRET)
client.upload_file(build_file, BUCKET, build_file)
print("####### removing archive #######")
os.system("rm {}".format(build_file))