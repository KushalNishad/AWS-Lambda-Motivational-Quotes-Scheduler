import json
import boto3
import pandas as pd
import io
import openpyxl

s3_client = boto3.client('s3')

# S3 bucket and file details
bucket_name = '<bucket-name>'
file_key = 'motivational_quotes.xlsx'
sender_email = 'XXXXXXXXXXXXXXXXXXX'
recipient_email = 'XXXXXXXXXXXXXXXXXXX'

def lambda_handler(event, context):

    print("Starting the function")
    
    # Download the Excel file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read()
    read_excel_data = io.BytesIO(file_content)
    df = pd.read_excel(read_excel_data, engine='openpyxl')
    #print(df.head())

    # Selecting a random row from the DataFrame
    random_row = df.sample(n=1).iloc[0]
    quote = random_row['Quote']
    author = random_row['Author']

    #print("Quote:", quote)
    #print("Author:", author)

    subject = "Your Daily Motivational Quote í¼Ÿ"
    body_text = f'"{quote}"\n\n- {author}'

    print("Body text", body_text)
