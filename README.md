# Amazon Bedrock AI Assistant

A simple Python application that uses Amazon Bedrock's Nova Micro AI model to analyze user questions and return structured JSON responses with summaries, categories, and confidence scores.

## What This Project Does

This project demonstrates how to interact with Amazon Bedrock, AWS's fully managed service for foundation models. The application:

- Takes a question from the user
- Sends it to Amazon's Nova Micro AI model via AWS Bedrock
- Receives a structured JSON response with:
  - A summary of the question
  - A category classification
  - A confidence score
- Displays token usage and latency metrics

## Files in This Repository

- **`app.py`**: The main application that takes user input and displays AI-generated analysis results
- **`bedrock_client.py`**: Contains the `ask_bedrock()` function that handles communication with AWS Bedrock
- **`bedrock_test.py`**: A simple test script to verify your Bedrock connection is working
- **`requirements.txt`**: Lists Python dependencies (boto3 for AWS SDK)
- **`.gitignore`**: Specifies files that should not be committed to version control

## Prerequisites

Before you can run this project, you need:

1. **Python 3.10 or higher** installed on your computer
2. **An AWS account** with access to Amazon Bedrock
3. **AWS credentials** configured with appropriate permissions
4. **Access to Amazon Nova Micro model** in the `us-east-1` region

## Local Setup Instructions

Follow these steps to set up and run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone https://github.com/jo-soroush/bedrock-ai-foundation.git
cd bedrock-ai-foundation
```

### Step 2: Create a Python Virtual Environment

A virtual environment keeps this project's dependencies separate from your system Python installation.

**On macOS and Linux:**

```bash
python3 -m venv .venv
```

**On Windows:**

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

**On macOS and Linux:**

```bash
source .venv/bin/activate
```

**On Windows (Command Prompt):**

```bash
.venv\Scripts\activate.bat
```

**On Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

When activated, you should see `(.venv)` at the beginning of your command prompt.

### Step 4: Install Dependencies

With your virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

This installs `boto3`, the AWS SDK for Python.

### Step 5: Configure AWS Credentials

You must configure your AWS credentials to authenticate with Amazon Bedrock. **Never commit credentials to this repository.**

**Configure using AWS CLI:**

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, default region (use `us-east-1`), and output format when prompted. This is the recommended approach for local development.

### Step 6: Run the Application

**To run the main interactive application:**

```bash
python app.py
```

You'll be prompted to enter a question. The AI will analyze it and return structured results.

**To run the connection test:**

```bash
python bedrock_test.py
```

This simple script verifies that you can connect to Amazon Bedrock successfully.

## Important Security Notes

⚠️ **NEVER commit AWS credentials to this repository or any version control system.**

Always use AWS CLI configuration or IAM roles for authentication. Do not hardcode AWS access keys or secret keys in your code.

## Troubleshooting

- **"AWS credentials were not found"**: Make sure you've configured your AWS credentials (see Step 5)
- **"Could not connect to AWS Bedrock"**: Check your internet connection and AWS region settings
- **Permission errors**: Ensure your AWS IAM user/role has permissions to invoke Bedrock models
- **Model access errors**: You may need to request access to the Nova Micro model in the AWS Bedrock console
