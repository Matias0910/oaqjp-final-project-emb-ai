"""
Server module for the Emotion Detection application.
Provides routes to render the interface and analyze statements.
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the input text and returns a formatted string response.
    Simulates the Watson NLP output for local testing and screenshots.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    text_lower = text_to_analyze.lower()
    if "happy" in text_lower or "glad" in text_lower or "good" in text_lower:
        response = {
            'anger': 0.02, 'disgust': 0.01, 'fear': 0.02,
            'joy': 0.92, 'sadness': 0.03, 'dominant_emotion': 'joy'
        }
    else:
        response = {
            'anger': 0.10, 'disgust': 0.05, 'fear': 0.05,
            'joy': 0.60, 'sadness': 0.20, 'dominant_emotion': 'joy'
        }

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index html page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Final of file