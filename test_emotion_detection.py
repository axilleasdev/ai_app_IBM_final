from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        resp1 = emotion_detector("I am glad this happened")
        resp2 = emotion_detector("I am really mad about this")
        resp3 = emotion_detector("I feel disgusted just hearing about this")
        resp4 = emotion_detector("I am so sad about this")
        resp5 = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(resp1['dominant_emotion'], 'joy')
        self.assertEqual(resp2['dominant_emotion'], 'anger')
        self.assertEqual(resp3['dominant_emotion'], 'disgust')
        self.assertEqual(resp4['dominant_emotion'], 'sadness')
        self.assertEqual(resp5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
