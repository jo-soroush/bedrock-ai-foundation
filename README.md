# Bedrock AI Foundation

This project is a beginner-friendly Python example that calls **Amazon Bedrock** (Nova Micro) to analyze a question and return structured JSON (summary, category, and confidence).

## Repository files

- `app.py` — interactive CLI app; asks for a question and prints Bedrock results.
- `bedrock_client.py` — Bedrock client and `ask_bedrock(prompt)` helper with error handling.
- `bedrock_test.py` — simple script that sends a sample prompt to Nova Micro and prints the response.
- `requirements.txt` — Python dependencies for this project.

## Local setup

1. Make sure Python 3 is installed.
2. Open a terminal in this repository:
   ```bash
   cd /home/runner/work/bedrock-ai-foundation/bedrock-ai-foundation
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
4. Activate the virtual environment:
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run locally

Run the interactive app:

```bash
python app.py
```

Optional: run the simple Bedrock test script:

```bash
python bedrock_test.py
```

## AWS credentials and security

You must have valid AWS credentials configured locally to call Amazon Bedrock.

- Never hardcode credentials in code.
- Never commit credentials, access keys, or `.env` secrets to this repository.
