# How to create a simple python ai chatbot
**Author**: Debugshala

## Overview

After the announcement of Gemini AI, Google has released API access for its Gemini models. Currently, the company offers API access to Gemini Pro, including text-only and text-and-vision models. This guide provides instructions on how to access and use the Gemini API.

### Note:

The Google Gemini API key is currently free for both text and vision models until general availability early next year. You can send up to 60 requests per minute without setting up Google Cloud billing or incurring any costs.

## Set Up Python and Pip on Your Computer

1. Install Python along with Pip on your PC or Mac. You need Python 3.9 or above.
   - For Windows: Install Python and Pip, and verify installation using `python -V` and `pip -V` commands in Command Prompt.
   - For Linux: Install Python and Pip on Ubuntu or other distros, and verify installation similarly.

2. Install Google’s Generative AI dependency:
   ```
   pip install -q -U google-generativeai
   ```

## How to Get the Gemini Pro API Key

1. Visit [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey) and sign in with your Google account.
2. Under API keys, click the “Create API key in new project” button.
3. Copy the API key and keep it private. Do not publish or share it publicly.

## How to Use the Gemini Pro API Key (Text-only Model)

1. Launch a code editor or use Notepad++ for beginners or Visual Studio Code for advanced users.
2. Copy the provided Python code below and paste it into your editor:

```python
import google.generativeai as genai

genai.configure(api_key='PASTE YOUR API KEY HERE')

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.text)
```

3. Replace `'PASTE YOUR API KEY HERE'` with your Gemini API key.
4. Save the file with a `.py` extension (e.g., `gemini.py`).
5. Open Terminal and navigate to the directory containing the file.
6. Run the file using the command:
   ```
   python gemini.py
   ```

## How to Use the Gemini Pro API Key (Text-and-Vision Model)

1. Open a new file in your code editor and paste the provided Python code below:

```python
import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('image.jpg')

genai.configure(api_key='PASTE YOUR API KEY HERE')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["what is the total calorie count?", img])

print(response.text)
```

2. Replace `'PASTE YOUR API KEY HERE'` with your Gemini API key.
3. Save the file with a `.py` extension (e.g., `bot.py`).
4. Ensure the image file mentioned in the code is saved in the same location.
5. Open Terminal, navigate to the directory, and run the file using:
   ```
   python bot.py
   ```

## Conclusion

These examples demonstrate how to use Google's Gemini API key to access the Gemini Pro models. You can interact with the text-only and text-and-vision models using simple Python scripts. Experiment with different queries and images to explore Gemini's capabilities.

For more information and updates, stay tuned for Gemini AI-related content.

---
