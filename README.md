# AI-Powered E-Commerce Chatbot

This is the base structure of an AI-powered product support bot with e-commerce features.

It answers product-related questions like:
- Specifications
- Prices
- Comparisons
- Ratings
- General FAQs (shipping, return policy, etc.)

## 🤖 How it works

- Frontend: Simple UI to ask product-related questions
- Backend: Python Flask app
- AI: Uses OpenAI or similar LLMs to answer contextually from a fixed dataset
- Products: Data stored in JSON (for demo) but can be switched to MySQL/PostgreSQL
- Tools: The `/tools` folder will contain additional scripts (e.g., price scrapers, order bots, etc.)

## ⚙️ Setup Instructions

```bash
# 1. Fork the repository
# Click the "Fork" button on the top right of the GitHub page

# 2. Clone your forked repo and enter the directory
git clone https://github.com/yashtanwar17/ecommerce-ai-chatbot
cd ecommerce-ai-chatbot

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Configure your AI API key
# Open app.py and replace 'YOUR_API_KEY_HERE' with your actual key

# 5. (Optional) Add your own features:
# - Logging chat responses
# - Saving chats/products to MySQL
# - Fetching prices from Amazon, Flipkart, etc.
# - Direct Amazon ordering for dropshipping
# - UI & product image scraping from source sites
# - Telegram/WhatsApp integration for queries

# 6. Run the app
python app.py
