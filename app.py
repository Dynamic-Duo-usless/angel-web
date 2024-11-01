from flask import Flask, render_template, request, jsonify
from assistant import wishme, search_wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    command = data['command'].lower()
    
    # Process command and call appropriate function
    if 'wikipedia' in command:
        query = command.replace('wikipedia', '').strip()
        response = search_wikipedia(query)
    elif 'greet me' in command:
        response = wishme()
    else:
        response = "I didn't understand that command."

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
