from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the question-answering model
question_answer = pipeline("question-answering")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    # Get user question and context from the form
    user_question = request.form['question']
    context = request.form['context']

    # Use the question-answering model to get the answer
    result = question_answer(question=user_question, context=context)
    answer = result['answer']

    return render_template('index.html', question=user_question, context=context, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

