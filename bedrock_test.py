
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import boto3
# class Chatter(OpenAI):
#     def __init__(self, provider="openai", model_name="gpt-4o", API_KEY=None, 
#                  temperature=0.7, max_tokens=4096):
#         load_dotenv()  # Load environment variables from .env file
#         providers = ["openai", "bedrock", "anthropic", "mistral"]
#         assert provider in providers, \
#             "Provider must be in '" + "', '".join(providers) + "'"
#         self.provider = provider
#         self.API_KEY = API_KEY
#         self.max_tokens = max_tokens

#         # self.anthropic = Anthropic()
#         # self.mistral = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
#         self.model_name = model_name
#         self.provider = provider
#         if provider == "openai":
#             # from openai import OpenAI
#             self.brain = self
#         elif provider == "bedrock":
#             import boto3
#             KEY = API_KEY if API_KEY else os.getenv("AWS_BEARER_TOKEN_BEDROCK")
#             # self.brain = BedrockOpenAIWrapper(model_id=model_name)
#             bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
#         elif provider == "anthropic":
#             from anthropic import Anthropic
#             key = API_KEY if API_KEY else os.getenv("ANTHROPIC_API_KEY")
#             self.brain = Anthropic(api_key=key)
#         elif provider == "mistral":
#             from mistralai import Mistral
#             key = API_KEY if API_KEY else os.getenv("MISTRAL_API_KEY")
#             self.brain = Mistral(api_key=key)
#         self.temperature = temperature


#     def chatting(self, role="user", content="Hello, world!"):
#         if self.provider == "openai":
#             response = self.brain.chat.completions.create(
#                 model=self.model_name,
#                 messages=[{"role":role, "content":content}],
#                 temperature=self.temperature
#             )
#             return response.choices[0].message.content
#         elif self.provider == "bedrock":
#             # Convert OpenAI message format to content
#             if isinstance(messages, list):
#                 content = ""
#                 for message in messages:
#                     role = message.get('role', 'user')
#                     content = message.get('content', '')
#                     if role == 'system':
#                         content += f"System: {content}\n"
#                     elif role == 'user':
#                         content += f"Human: {content}\n"
#                     elif role == 'assistant':
#                         content += f"Assistant: {content}\n"
#                 content += "Assistant:"
#             else:
#                 content = str(messages)

#             response = self.brain.invoke_model(
#                 body=json.dumps({
#                     "inputText": content,
#                     "textGenerationConfig": {
#                         "maxTokenCount": self.max_tokens,
#                         "temperature": self.temperature
#                     }
#                 }),
#                 modelId=self.model_name
#             )
#             return response.choices[0].message.content
#         elif self.provider == "anthropic":
#             response = self.brain.messages.create(
#                 model=self.model_name,
#                 messages=[
#                     {"role": role, "content": content}
#                 ],
#                 temperature=self.temperature
#             )
#             return response.choices[0].message.content
#         elif self.provider == "mistral":
#             response = self.brain.chat.complete(
#                 model=self.model_name,
#                 messages=[{"role": role, "content": content}],
#                 temperature=self.temperature
#             )
#             return response.choices[0].message.content
#         else:
#             raise ValueError("Unsupported model name")

#     # def display_markdown(self, text):
#     #     display(Markdown(text))





# Hypothetical wrapper (not official)
class BedrockOpenAIWrapper:
    def __init__(self, model_id="anthropic.claude-v2", region_name='us-east-1'):
        self.bedrock = boto3.client('bedrock-runtime', region_name=region_name)
        self.model_id = model_id

    def chat(self, content):
        response = self.bedrock.invoke_model(
            body=json.dumps({"inputText": content}),
            modelId=self.model_id
        )
        return response['body'].read().decode()

    def completions_create(self, messages, model=None, temperature=0.7, max_tokens=1000):
        """Create a chat completion similar to OpenAI's chat.completions.create"""
        if model:
            model_id = model
        else:
            model_id = self.model_id
            
        # Convert OpenAI message format to content
        if isinstance(messages, list):
            content = ""
            for message in messages:
                role = message.get('role', 'user')
                content = message.get('content', '')
                if role == 'system':
                    content += f"System: {content}\n"
                elif role == 'user':
                    content += f"Human: {content}\n"
                elif role == 'assistant':
                    content += f"Assistant: {content}\n"
            content += "Assistant:"
        else:
            content = str(messages)
        
        # Prepare request body based on model type
        if "anthropic" in model_id.lower():
            body = {
                "content": content,
                "max_tokens_to_sample": max_tokens,
                "temperature": temperature
            }
        else:
            body = {
                "inputText": content,
                "textGenerationConfig": {
                    "maxTokenCount": max_tokens,
                    "temperature": temperature
                }
            }
        
        response = self.bedrock.invoke_model(
            body=json.dumps(body),
            modelId=model_id
        )
        
        response_body = json.loads(response['body'].read().decode())
        
        # Parse response based on model type
        if "anthropic" in model_id.lower():
            content = response_body.get('completion', '')
        else:
            content = response_body.get('results', [{}])[0].get('outputText', '')
        
        # Return OpenAI-like response structure
        return {
            'choices': [{
                'message': {
                    'role': 'assistant',
                    'content': content
                }
            }]
        }
    
    def create_completion(self, content, model=None, temperature=0.7, max_tokens=1000):
        """Create a simple text completion"""
        messages = [{"role": "user", "content": content}]
        response = self.completions_create(messages, model, temperature, max_tokens)
        return response['choices'][0]['message']['content']


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the theory of relativity in simple terms."}
    ]
    

    # # OpenAI
    # openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # response = openai.chat.completions.create(
    #     model="gpt-4o", messages=messages)
    # answer = response.choices[0].message.content
    # print("OpenAI Response:")
    # print(answer)

    KEY = os.getenv("AWS_BEARER_TOKEN_BEDROCK")
    print(f"Using Bedrock Bearer Token: {KEY[:4]}...{KEY[-4:]}")
    # Bedrock
    bedrock = BedrockOpenAIWrapper(model_id="anthropic.claude-v2")
    response = bedrock.completions_create(messages, model="anthropic.claude-v2")
    answer = response['choices'][0]['message']['content']
    print("\nBedrock Response:")
    print(answer)

    # # Mistral
    # mistral = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
    # response = mistral.chat.complete(
    #     model="mistral-small-2506", messages=messages)
    # answer = response.choices[0].message.content
    # print("\nMistral Response:")
    # print(answer)