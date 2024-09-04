from flask import Flask, render_template, request, redirect, url_for
from note import get_note
from datetime import datetime
from random import choice

app = Flask(__name__)

duration = 1
played_note = None
actual_note = None
streak = 0
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/instructions', methods=['GET'])
def instructions():
    return render_template('instructions.html')


@app.route('/fretboard-memorizer', methods=['GET', 'POST'])
def fretboard_memorizer():
    global duration
    global played_note
    global actual_note
    global notes
    global streak

    if actual_note is not None:
        played_note = get_note(duration)
        if played_note == actual_note:
            streak += 1
        else:
            streak = 0

        print(f"Played note: {played_note}")
        print(f"Actual note: {actual_note}")

    actual_note = choice(notes)

    return render_template('fretboard-memorizer.html', actual_note=actual_note, streak=streak)


if __name__ == '__main__':
    app.run(debug=True)
