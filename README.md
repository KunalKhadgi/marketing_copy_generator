# marketing_copy_generator
Uses Flash2.0 to generate a marketing headline and description for the given product, target audience in 4 different tones

# AI-Powered Marketing Copy Generator

## Overview
This project is a Flask-based AI tool that generates personalized marketing copy based on user input. It leverages **Google Gemini Flash 2.0** to create catchy ad headlines and engaging descriptions tailored to different tones and audiences.

## Features
- Generates **ad headlines** and **marketing descriptions**
- Supports **four different tones** (Exciting, Professional, Casual, Friendly)
- User-friendly **web interface** with Flask and CSS
- Uses **Google Generative AI (Gemini-1.5-Flash)** for text generation

## Installation
### 1. Clone the repository
```sh
 git clone https://github.com/your-repo-name.git
 cd your-repo-name
```

### 2. Set up a virtual environment (optional but recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `config.py` file in the root directory and add:
```python
GOOGLE_API_KEY = "your-google-api-key-here"
```

### 5. Run the application
```sh
python app.py
```
Access the web app at: `http://127.0.0.1:5000/`

## Usage
1. Enter **Brand Name**, **Product Description**, and **Target Audience**.
2. Select a **tone** (Exciting, Professional, Casual, Friendly).
3. Click **Generate Copy** to receive AI-powered ad text.

## Dependencies
- Flask
- Google Generative AI (gemini-1.5-flash)

## Future Improvements
- Support for **hashtags** and **CTAs**
- Additional customization options for branding

## License
This project is open-source. Feel free to modify and extend it as needed!

