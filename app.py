from flask import Flask, request, jsonify, render_template, session
import google.generativeai as genai
from flask_caching import Cache
from flask_session import Session

# Configuração da API do Google Generative AI
genai.configure(api_key="AIzaSyDOUQPvZru5GlT8kqtdO7-7dOa4Vu03_w0")

# Selecionando o modelo adequado
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

# Configuração do cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Configuração da sessão
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')

    # Checar se a resposta está no cache
    cached_response = cache.get(user_message)
    if cached_response:
        return jsonify({'response': cached_response})

    # Recuperar o histórico da sessão
    chat_history = session.get('chat_history', [])

    # Formatar o histórico para o formato esperado
    formatted_history = []
    for entry in chat_history:
        formatted_history.append({'role': 'user', 'parts': [{'text': entry['user']}]})
        formatted_history.append({'role': 'model', 'parts': [{'text': entry['bot']}]})

    # Iniciar o chat com o histórico formatado
    chat = model.start_chat(history=formatted_history)
    response = chat.send_message(user_message)
    response_text = response.text

    # Atualizar o histórico da sessão
    chat_history.append({"user": user_message, "bot": response_text})
    session['chat_history'] = chat_history

    # Armazenar a resposta no cache
    cache.set(user_message, response_text)

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
