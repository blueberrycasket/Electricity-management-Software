import google.generativeai as genai

# Add this after `configure(api_key=gemini_api_key)`
models = genai.list_models()
for model in models:
    print(f"Model Name: {model.name}, Supported Methods: {model.supported_generation_methods}")