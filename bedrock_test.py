import boto3


client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
)


response = client.converse(
    modelId="amazon.nova-micro-v1:0",

    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Explain Amazon Bedrock in one sentence."
                }
            ],
        }
    ],

    inferenceConfig={
        "maxTokens": 200,
        "temperature": 0.2,
        "topP": 0.9,
    },
)


answer = response["output"]["message"]["content"][0]["text"]

usage = response["usage"]


print("\nNova Micro:")
print(answer)

print("\nToken usage:")
print(f"Input tokens:  {usage['inputTokens']}")
print(f"Output tokens: {usage['outputTokens']}")
print(f"Total tokens:  {usage['totalTokens']}")

print("\nResponse info:")
print(f"Stop reason: {response['stopReason']}")
print(f"Latency:     {response['metrics']['latencyMs']} ms")