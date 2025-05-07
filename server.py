"""
deploy the webapp for emotion detection
"""
from flask import Flask, render_template, request
import EmotionDetection

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """generate webapp emotion response for text provided"""
    text_to_analyze = request.args.get('textToAnalyze')
    out = EmotionDetection.emotion_detector(text_to_analyze)
    if out['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = out['anger']
    disgust = out['disgust']
    fear = out['fear']
    joy = out['joy']
    sadness = out['sadness']
    dominant_emotion = out['dominant_emotion']
    return f"For the given statement, the system response is 'anger': {anger} , \
    'disgust': {disgust}, 'fear': {fear} ,'joy': {joy} and 'sadness': {sadness}. \
    The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    """render html with the response"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
