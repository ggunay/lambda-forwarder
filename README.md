# AWS Lambda Forwarder for API Gateway Test Environment

This repository contains a simple AWS Lambda function written in Python, designed to be used in a test environment for AWS API Gateway and Lambda functions. The Lambda function acts as a message forwarder, accepting a query as input, sending the query to an external API, and returning the response back to the API Gateway.

## Requirements

- Python 3.8 or later
- Docker
- AWS SAM CLI (Serverless Application Model CLI) for local testing
- AWS CLI configured with the necessary permissions to deploy Lambda functions and API Gateway

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/ggunay/lambda-forwarder.git
cd lambda-forwarder
```

Create and activate a virtual environment (optional but recommended):
```bash
python -m venv env
source env/bin/activate     # On Windows, use "env\Scripts\activate" instead
```

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Local Testing

To test the Lambda function locally, you can use the AWS SAM CLI. The SAM CLI allows you to simulate the Lambda and API Gateway environment on your local machine.

Make sure you have Docker installed and running on your machine.

Run the following command to start the local API Gateway:

```bash
sam local start-api
```
The API Gateway will be running at http://127.0.0.1:3000. You can now use tools like curl or Postman to test the Lambda function locally.

## Deploy to AWS

To deploy the Lambda function to AWS, follow these steps:

Build the SAM application:
```bash
sam build --use-container
```

Deploy the application:
```bash
sam deploy --guided
```
Follow the prompts to configure the deployment settings, such as the AWS Region, stack name, and other parameters.

## Usage

The Lambda function acts as a message forwarder and accepts a POST request with a JSON body containing a query field. The function will send this query to the specified external API and return the response back to the API Gateway. The API Gateway can be configured to invoke this Lambda function and handle the requests from clients.

Example request:

```json
{
  "query": "value1"
}
```
Example response:

```json
{
  "message": "Query received: value1"
}
```