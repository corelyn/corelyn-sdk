# corelyn-sdk

Python SDK for Corelyn AI API.

## Installation

```bash
pip install corelyn-sdk
``` 

## Usage

```python
from corelyn_sdk import CorelynSDK

sdk = CorelynSDK(
    api_key="your-api-key",
    system_prompt="You are a helpful assistant"
)

print(sdk.get_ai_response("Explain AI"))
```
