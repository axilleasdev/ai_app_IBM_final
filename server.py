"""
This is a simple Flask application for emotion detection.
"""

from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import HTTPException
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_api():
    """
    API endpoint for emotion detection.
    """
    try:
        if request.method == 'POST':
            data = request.json
            statement = data.get('statement', '')
        elif request.method == 'GET':
            statement = request.args.get('textToAnalyze', '')

        # Handle blank entries
        if not statement:
            return jsonify({'error': 'Text is required for analysis.'})

        result = emotion_detector(statement)

        return jsonify(result)
    except HTTPException as http_err:
        return jsonify({'error': f'HTTP exception occurred: {http_err.description}'})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
