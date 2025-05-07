import EmotionDetection

import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = EmotionDetection.emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Test case 2
        result_2 = EmotionDetection.emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Test case 3
        result_3 = EmotionDetection.emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust') 

        # Test case 4
        result_4 = EmotionDetection.emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness') 

        # Test case 5
        result_5 = EmotionDetection.emotion_detector('I am really afraid that this will happen	')
        self.assertEqual(result_5['dominant_emotion'], 'fear') 

unittest.main()  