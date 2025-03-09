import google.generativeai as genai
import config
from flask import Flask, request, render_template

app = Flask(__name__)

# Configure Google Generative AI API key
genai.configure(api_key=config.GOOGLE_API_KEY)

def generate_marketing_copy(brand, product_description, audience, tone):
    """
    Generates a catchy ad headline and marketing copy using Google Gemini AI with a specific tone.
    """
    prompt = f"""
    Create an ad for:
    Brand: {brand}
    Product: {product_description}
    Target Audience: {audience}
    
    The tone of the ad should be: {tone}.
    Generate a short, catchy ad headline and a 2-3 sentence marketing description.
    """
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text if response.text else "Could not generate copy. Try again!"

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_copy = ""
    selected_tone = "Exciting"  # Default tone
    
    if request.method == 'POST':
        brand = request.form['brand']
        product_description = request.form['product_description']
        audience = request.form['audience']
        tone = request.form['tone']  # Get selected tone from the form
        generated_copy = generate_marketing_copy(brand, product_description, audience, tone)
        selected_tone = tone  # Preserve selected tone
    
    return render_template('index.html', generated_copy=generated_copy, selected_tone=selected_tone)

if __name__ == "__main__":
    app.run(debug=True)
