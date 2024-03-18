from flask import Flask, render_template, request
from ia import answer_question

app = Flask(__name__, template_folder='C:/Users/tu_usuario/Documents/iahis', static_folder='C:/Users/tu_usuario/Documents/iahis/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def get_answer():
    question = request.form['question']
    answer = answer_question(question)
    return render_template('ans.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
