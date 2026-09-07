from bedrock_client import ask_bedrock


user_question = input("You: ")

result = ask_bedrock(user_question)

if result["success"]:
    data = result["data"]
    usage = result["usage"]

    print("\nResult:")
    print(f"Summary:    {data['summary']}")
    print(f"Category:   {data['category']}")
    print(f"Confidence: {data['confidence']}")

    print("\nToken usage:")
    print(f"Input tokens:  {usage['inputTokens']}")
    print(f"Output tokens: {usage['outputTokens']}")
    print(f"Total tokens:  {usage['totalTokens']}")

    print("\nResponse info:")
    print(f"Stop reason: {result['stop_reason']}")
    print(f"Latency:     {result['latency_ms']} ms")

else:
    print("\nERROR:")
    print(result["error"])