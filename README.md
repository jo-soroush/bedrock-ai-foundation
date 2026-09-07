# Amazon Bedrock Question Analyzer

This project uses **Amazon Bedrock** to analyze user questions and return structured responses. It interacts with AWS Bedrock's Amazon Nova Micro model to generate AI-powered analysis with token usage tracking and latency metrics.

## What This Project Does

The application:
- Takes a user question as input
- Sends it to Amazon Bedrock (Nova Micro model)
- Analyzes the question and returns:
  - A summary
  - A category classification
  - A confidence score (0.0 to 1.0)
- Displays token usage and performance metrics

## Repository Structure

Here are the main files in this repository:

| File | Description |
|------|-------------|
| **app.py** | Main application script that prompts for user input and displays results |
| **bedrock_client.py** | AWS Bedrock client module with the `ask_bedrock()` function |
| **bedrock_test.py** | Simple test script to verify your Bedrock connection |
| **requirements.txt** | Python dependencies (boto3) |
| **.gitignore** | Specifies which files Git should ignore |

## Prerequisites

Before you begin, make sure you have:

1. **Python 3.7 or higher** installed on your system
2. An **AWS account** with access to Amazon Bedrock
3. **AWS credentials** configured (see setup instructions below)
4. Access to the **Amazon Nova Micro model** in your AWS region

## Local Setup Instructions

Follow these steps to set up and run the project on your local machine:

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Python Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.

**On macOS/Linux:**
```bash
python3 -m venv venv
```

**On Windows:**
```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### Step 4: Install Dependencies

Install all required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install `boto3`, the AWS SDK for Python.

### Step 5: Configure AWS Credentials

You need to configure your AWS credentials to authenticate with Amazon Bedrock. The easiest way is to use the AWS CLI:

```bash
aws configure
```

You'll be prompted to enter your AWS Access Key ID, Secret Access Key, default region (e.g., `us-east-1`), and output format.

**⚠️ IMPORTANT SECURITY WARNING:**
- **NEVER commit AWS credentials to this repository**
- **NEVER hardcode credentials in your code**
- Use environment variables, AWS CLI configuration, or IAM roles instead

## How to Run the Project

Once setup is complete, you can run the application:

```bash
python app.py
```

The program will prompt you to enter a question. Type your question and press Enter. The application will:
1. Send your question to Amazon Bedrock
2. Display the analysis results
3. Show token usage and latency metrics

### Testing Your Connection

To verify that your AWS Bedrock connection is working, run the test script:

```bash
python bedrock_test.py
```

This will send a simple test query to Amazon Bedrock and display the response.

## Troubleshooting

**"AWS credentials were not found"**
- Run `aws configure` to set up your credentials
- Ensure your AWS Access Key ID and Secret Access Key are correct

**"Could not connect to AWS Bedrock"**
- Check your internet connection
- Verify that your AWS region supports Amazon Bedrock

**"Access denied" or permission errors**
- Ensure your AWS user/role has permissions to use Amazon Bedrock
- You may need the `bedrock:InvokeModel` permission

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

## Additional Resources

- AWS Bedrock uses AI models from various providers
- This project uses Amazon Nova Micro, a fast and cost-effective model
- Token usage is tracked to help you monitor costs

---

**Remember:** Keep your AWS credentials secure and never commit them to version control!
