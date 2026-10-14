import boto3
import json
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "aws-access-key"
    region_name = "us-east-2"

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)   # parse the JSON string into a dict

credentials = get_secret()

# Extract the values; if AWS_REGION isn't in the secret, use the region from the session
AWS_ACCESS_KEY_ID = credentials.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = credentials.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = credentials.get("AWS_REGION", boto3.session.Session().region_name or "us-east-2")