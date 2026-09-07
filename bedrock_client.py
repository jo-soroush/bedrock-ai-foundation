import boto3
import json

from botocore.exceptions import (
    ClientError,
    NoCredentialsError,
    EndpointConnectionError,
)

MODEL_ID = "amazon.nova-micro-v1:0"
REGION = "us-east-1"

client = boto3.client(
    "bedrock-runtime",
    region_name=REGION,
)


def ask_bedrock(prompt):
    try:
        response = client.converse(
            modelId=MODEL_ID,

            system=[
                {
                    "text": (
                        "You are an AI assistant. "
                        "Return ONLY valid JSON. "
                        "Do not include markdown or text outside the JSON."
                    )
                }
            ],

            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": (
                                f"Analyze this question: {prompt}\n\n"
                                "Return this exact structure:\n"
                                "{\n"
                                '  "summary": "short summary",\n'
                                '  "category": "category name",\n'
                                '  "confidence": 0.0\n'
                                "}"
                            )
                        }
                    ],
                }
            ],

            inferenceConfig={
                "maxTokens": 300,
                "temperature": 0.1,
                "topP": 0.9,
            },
        )

        text = response["output"]["message"]["content"][0]["text"]

        data = json.loads(text)

        return {
            "success": True,
            "data": data,
            "usage": response["usage"],
            "stop_reason": response["stopReason"],
            "latency_ms": response["metrics"]["latencyMs"],
        }

    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Model returned invalid JSON.",
        }

    except NoCredentialsError:
        return {
            "success": False,
            "error": "AWS credentials were not found.",
        }

    except EndpointConnectionError:
        return {
            "success": False,
            "error": "Could not connect to AWS Bedrock.",
        }

    except ClientError as error:
        return {
            "success": False,
            "error": error.response["Error"]["Message"],
        }

    except Exception as error:
        return {
            "success": False,
            "error": str(error),
        }