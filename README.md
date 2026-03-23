# corelyn-sdk

Python SDK for Corelyn AI API.

## Installation

```bash
pip install corelyn-sdk
``` 

## Usage

```python
from corelyn_sdk import CorelynSDK

sdk = CorelynSDK(api_key="YOUR_API_KEY")
response = sdk.get_ai_response("Make me a site about bananas in one html file", model="nvidia/meta/llama-3.2-1b-instruct")
print(response)
```