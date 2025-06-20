# Math Word Problem Generator (Grades 3–6)

This project is an interactive AI agent that generates multiple-choice math word problems for children in grades 3 to 6, using the Gemini 2.0 Flash model via the Gemini API. The app is built with Streamlit and the OpenAI Agents SDK.

## Features
- Select a real-life topic (e.g., Pocket money, School cafeteria, Birthday party, Toy shopping, Homework planning)
- Get a math word problem with four answer options (A–D)
- Choose your answer and receive instant feedback and explanation

## Setup

1. **Clone the repository**
2. **Install dependencies**

```bash
pip install -e .
```

3. **Set your Gemini API key**

You need a Google Gemini API key. Set it as an environment variable:

**On Linux/macOS:**
```bash
export GEMINI_API_KEY=your_gemini_api_key_here
```
**On Windows (cmd):**
```cmd
set GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Run the Streamlit app**

```bash
streamlit run src/tutor/app.py
```

## Notes
- Requires Python 3.11+
- Uses the Gemini 2.0 Flash model via the Gemini API
- Built with OpenAI Agents SDK, Streamlit, and Pydantic

---
MIT License
