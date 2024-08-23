from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

# Carregar o modelo spaCy
nlp = spacy.load('pt_core_news_sm')

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    text = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        token_type = request.form.get('token_type', '')
        doc = nlp(text)
        tokens = [token.text for token in doc if token.pos_ == token_type]
    return render_template('index.html', text=text, tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)
