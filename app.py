from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_detection():
    try:
        # Execute your Python script here
        subprocess.Popen(['python', 'inference_classifier.py'])  # Run inference.py in a separate process
        return render_template('detectpage.html')  # Render the new HTML page
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

