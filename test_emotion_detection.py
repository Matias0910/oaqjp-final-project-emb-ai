import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector(self, mock_post):
        # 1. Test para Alegría (joy)
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"emotionPredictions": [{"emotion": {"anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.9, "sadness": 0.01}}]}'
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        
        # 2. Test para Furia (anger)
        mock_post.return_value.text = '{"emotionPredictions": [{"emotion": {"anger": 0.9, "disgust": 0.01, "fear": 0.01, "joy": 0.01, "sadness": 0.01}}]}'
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        
        # 3. Test para Disgusto (disgust)
        mock_post.return_value.text = '{"emotionPredictions": [{"emotion": {"anger": 0.01, "disgust": 0.9, "fear": 0.01, "joy": 0.01, "sadness": 0.01}}]}'
        result = emotion_detector("I am shocked and revolted by this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
        # 4. Test para Tristeza (sadness)
        mock_post.return_value.text = '{"emotionPredictions": [{"emotion": {"anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.01, "sadness": 0.9}}]}'
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
        # 5. Test para Miedo (fear)
        mock_post.return_value.text = '{"emotionPredictions": [{"emotion": {"anger": 0.01, "disgust": 0.01, "fear": 0.9, "joy": 0.01, "sadness": 0.01}}]}'
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()