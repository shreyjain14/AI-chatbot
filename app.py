from ai import ask_ai, get_chat, reset_chat
from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv('.env')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class AIForm(FlaskForm):
    question = StringField(validators=[InputRequired()])
    submit = SubmitField('Submit')


class User:
    def __init__(self):
        self.chat = []

    def add(self, question, answer):
        self.chat.append(question)
        self.chat.append(answer)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = AIForm()
    if form.validate_on_submit():
        question = form.question.data
        response = ask_ai(question)
        chat = get_chat(question, response)

        return render_template('index.html', form=form, chat=chat)

    return render_template('index.html', form=form)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    reset_chat()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
