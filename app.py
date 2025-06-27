from flask import Flask, render_template, request, jsonify, session
import json
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'keys'  # Needed for session
CORS(app)

# SambaNova/DeepSeek API client setup
client = OpenAI(
    api_key="94d90e1b-09f0-4814-a77b-a53ae1fabc7x",
    base_url="https://api.sambanova.ai/v1"
)

@app.route('/')
def home():
    with open('products.json') as f:
        products = json.load(f)
    return render_template('index.html', products=products)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data['message']

    # Initialize conversation history if not present
    if 'history' not in session:
        session['history'] = [
            {"role": "system", "content": """
             You are an AI assistant for an e-commerce electronics website. Your job is to only answer customer questions related to:

Delivery: will start soon and pre-order by sending sms on +91 1234567890

Product-Specific Questions

Prices, specifications, display, performance, and usage.

Product Comparison & Recommendations

Best for gaming, cheapest, lightest, display quality.

Ratings & Reviews

Product ratings or comparisons.

👨Account & Support

Account requirements, how to contact support.
support mail: support@mail.com

Product One-liners:
Lenovo V15 – ₹42,890 – Ryzen 7, 16GB RAM, 512GB SSD, 15.6" FHD, Radeon graphics, rated 3.9★.

Lenovo LOQ 2024 – ₹63,974 – Ryzen 5, 12GB DDR5, RTX 3050 6GB, 144Hz 15.6" display, rated 4.5★.

MacBook Air (M4) – ₹99,900 – M4 chip, 16GB RAM, 256GB SSD, 13.6" Retina, MagSafe, rated 5.0★.

If the question is not related to the topics above (e.g., "How many days in a year?"), respond with:

"Sir, this is not relevant to our website."

Do not provide answers unrelated to the website's products, orders, or services. Be polite, direct, and one liner only. Brief only when customer asks for it."""}
        ]

    # Append user's message
    session['history'].append({"role": "user", "content": user_input})

    # Send full context to the model
    response = client.chat.completions.create(
        model="DeepSeek-V3-0324",
        messages=session['history'],
        temperature=0.1,
        top_p=0.1
    )

    bot_reply = response.choices[0].message.content.strip()

    # Append bot's reply to session
    session['history'].append({"role": "assistant", "content": bot_reply})

    return jsonify({'reply': bot_reply})

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('history', None)
    return jsonify({'message': 'Conversation reset.'})

if __name__ == '__main__':
    app.run(debug=True)

