from utils.prompts import BASE_PROMPT
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re
import codecs
import json5

load_dotenv()

def init_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    return genai.GenerativeModel("gemini-2.0-flash")

def extract_json_from_code_block(text):
    """
    Extract JSON from a markdown code block, e.g.
    ```json
    { ... }
    ```
    """
    # Try to match ```json ... ```
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text.strip()

def generate_question(topic: str):
    model = init_gemini()
    # Prompt Gemini to return a JSON object
    prompt = (
        BASE_PROMPT.format(topic=topic) +
        "\nReturn the result as a JSON object with keys: question, options (list of 4), correct (A/B/C/D), and explanation."
    )
    response = model.generate_content(prompt)
    print("Gemini full response:", response)
    print("Gemini raw response:", repr(response.text))
    text = extract_json_from_code_block(response.text)
    if not text:
        return {"error": "Gemini returned an empty response. Check your API key, quota, or for error messages.", "raw": ""}
    # Try to extract JSON from the response
    try:
        data = json5.loads(text)  # Use json5 for more robust parsing
        return data
    except Exception as e:
        return {"error": f"Failed to parse JSON: {e}", "raw": text}