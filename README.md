# corelyn-sdk

Python SDK for Corelyn AI API.

## Installation

```bash
pip install corelyn-sdk
``` 

## Usage

### For setting the System Prompt once
```python
from corelyn_sdk import CorelynSDK

sdk = CorelynSDK(
    api_key="your-api-key",
    system_prompt="You are a helpful assistant",
    default_model="cerebras/llama3.1-8b"
)

print(sdk.get_ai_response("Explain AI"))
```

### For overiting the System Prompt per prompt
```python
from corelyn_sdk import CorelynSDK

sdk = CorelynSDK("your-api-key")

print(
    sdk.get_ai_response(
        "Write a joke",
        system_prompt="You are a sarcastic comedian"
    )
)
```

### For full conversations (good for chatbots)
```python
from corelyn_sdk import CorelynSDK

messages = [
    {"role": "system", "content": "You are Corelyn"},
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi!"},
    {"role": "user", "content": "Tell me a joke"}
]

sdk = CorelynSDK("your-api-key")

print(sdk.get_ai_response(messages=messages))
```

# Set diffrent model
```python
sdk.set_model("nvidia/moonshotai/kimi-k2.5")
```
