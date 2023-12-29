''' A Flask application for Emotion detection using Watson NLP library
    through our implemented library EmotionDetection, the app is deployed
    on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector", methods=['GET'])
def sent_detector():
    ''' This code receives text from the HTML interface and
        runs emotion detector over it using emotion_detector()
        function.
        The output returned is a json with the info about score
        of each emotion and the dominant emotion for the provided text.
    '''
    text_to_detect = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_detect)
    # Case of invalid input
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {res['anger']},"
    f"'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and "
    f"'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
