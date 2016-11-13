#!/usr/bin/env python
from flask import Flask, request, render_template
from PyDictionary import PyDictionary

dictionary = PyDictionary()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    plagiarize_body = []
    body = "Enter text that you want to steal"
    if request.method == 'POST':
        body = request.form['body']
        plagiarize_body = []
        
    for word in body.split():
        new_word = word
        try:
            if len(word) > 4:
                new_word = dictionary.synonym(word)[0]
        except Exception:
            pass
        plagiarize_body.append(new_word)

    return render_template(
        'index.html',
        body=body,
        plagiarize_body=" ".join(plagiarize_body)
    )


if __name__ == '__main__':
    app.debug = True
    app.run()
