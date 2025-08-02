from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/prompt', methods=['POST'])
def prompt():
    try:
        data = request.json
        prompt_text = data.get('prompt')

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_text}]
        )

        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
