import requests
import json

def emotion_detector(text_to_analyze):
    """
    Función que conecta con la API de Watson NLP para detectar emociones.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"Glba-Share-Token": "https://sn-watson-emotion.labs.skills.network"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Tarea 7: Manejo de error para código de estado 400 (texto vacío)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # Tarea 3: Formatear la salida si es exitosa
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Encontrar la emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions