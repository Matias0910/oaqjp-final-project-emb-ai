from flask import Flask, render_template, request
from sentiment_analysis import sentiment_analyzer

app = Flask("Emotion Detector")

# CAMBIAMOS LA RUTA AQUÍ PARA QUE COINCIDA CON LA PÁGINA WEB (/emotionDetector)
@app.route("/emotionDetector")
def emo_detector():
    # Extraemos el texto que escribiste en la página
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pasamos el texto por tu función
    response = sentiment_analyzer(text_to_analyze)
    
    label = response['label']
    score = response['score']
    
    if label is None:
        return "Invalid text! Please try again."
    
    # Retornamos el formato que pide el HTML
    return f"The analyzed text is [{label}] with a score of {score}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)