import json
import boto3
import pandas as pd
import io

s3_client = boto3.client('s3')
ses_client = boto3.client("ses", region_name="us-east-1") 

# S3 bucket and file details
bucket_name = 'nishadawsbucket'
file_key = 'motivational_quotes.csv'
sender_email = 'nkushal77@gmail.com'
recipient_email = 'kushal.nishad@dcmail.ca'

def lambda_handler(event, context):

    print("Starting the function")
    
    # Download the Excel file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read()
    read_csv_data = io.BytesIO(file_content)
    df = pd.read_csv(read_csv_data)
    print(df.head())

    # Selecting a random row from the DataFrame
    random_row = df.sample(n=1).iloc[0]
    quote = random_row['Quote']
    author = random_row['Author']

    #print("Quote:", quote)
    #print("Author:", author)

    subject = "Your Daily Motivational Quote 🌟"
    body_text = f'"{quote}"\n\n- {author}'

    print("Body text", body_text)

    # Send Email via AWS SES
    ses_client.send_email(
        Source=sender_email,
        Destination={"ToAddresses": [recipient_email]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body_text}},
        }
    )
