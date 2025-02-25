# AWS Lambda Motivational Quotes Scheduler

## 📌 Overview
This project is an AWS Lambda function that sends a **random motivational quote** daily at **9:00 AM UTC** using **Amazon EventBridge Scheduler** and **Amazon SES**.

## 🚀 Features
- Fetches a random quote from a **CSV file** stored in **S3**.
- Sends an **email notification** using **Amazon SES**.
- Uses **AWS EventBridge Scheduler** to run the function **daily at 9:00 AM**.

## 🏗 Architecture
- **Amazon S3**: Stores the CSV file containing motivational quotes.
- **AWS Lambda**: Reads the CSV file, selects a random quote, and triggers SES.
- **Amazon SES**: Sends the email with the quote.
- **Amazon EventBridge**: Triggers Lambda function daily at 9:00 AM.

![Architecture Diagram](docs/Architecture Diagram.png.png)

## 🛠 Setup & Deployment
### Prerequisites
- AWS Account
- IAM Role with permissions for Lambda, EventBridge, SES, and S3
- Python installed locally

### Deploying the Lambda Function
1. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
