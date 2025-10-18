"""
TripGain - Section 3: Gemini Integration (Applied Intelligence Task)
File: tripgain_gemini_analysis.py
Author: [Your Name]
Description:
  - Fetches live webpage content.
  - Cleans HTML using BeautifulSoup.
  - Sends cleaned content to Google Gemini 2.5 Flash model.
  - Summarizes and provides insight.
  - Saves the output to summary_output.txt.
"""

import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from datetime import datetime

# ----------------------------
# CONFIGURATION
# ----------------------------
# Replace with your actual Gemini API key
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

# You can choose one of these:
URL = "https://en.wikipedia.org/wiki/Artificial_intelligence"
# URL = "https://www.bbc.com/news/technology"
# URL = "https://edition.cnn.com/business"

# ----------------------------
# STEP 1: Fetch and Clean Webpage
# ----------------------------
def fetch_and_clean(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove scripts, styles, and nav
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text[:15000]  # limit content to avoid model input overflow


# ----------------------------
# STEP 2: Custom Prompt for Gemini
# ----------------------------
def create_prompt(content):
    prompt = f"""
You are an expert technology analyst. Analyze the following webpage text about AI or technology news.
Summarize it into 3–5 concise bullet points that focus on major themes, trends, or insights.
Then, provide one final single-line insight that interprets the overall meaning or impact.

Text to analyze:
{content}

Output format:
Summary:
• point 1
• point 2
• point 3
• point 4
• point 5

Insight:
<your one-line insight>
"""
    return prompt


# ----------------------------
# STEP 3: Send to Gemini 2.5 Flash
# ----------------------------
def analyze_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


# ----------------------------
# STEP 4: Save to File
# ----------------------------
def save_output(output_text):
    with open("summary_output.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
    print("\n--- summary_output.txt saved successfully ---")


# ----------------------------
# MAIN EXECUTION
# ----------------------------
def main():
    print("Fetching webpage content...")
    content = fetch_and_clean(URL)

    print("Creating prompt and analyzing with Gemini 2.5 Flash...")
    prompt = create_prompt(content)
    result = analyze_with_gemini(prompt)

    print("\n--- GEMINI OUTPUT ---")
    print(result)
    save_output(result)
    print(f"\nCompleted at {datetime.utcnow().isoformat()} UTC")


if __name__ == "__main__":
    main()
