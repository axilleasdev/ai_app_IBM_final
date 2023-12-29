import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    text = response.text
    info_dic = json.loads(text)["emotionPredictions"][0]
    res_dic = {
        'anger': info_dic["emotion"]["anger"],
        'disgust': info_dic["emotion"]["disgust"],
        'fear': info_dic["emotion"]["fear"],
        'joy': info_dic["emotion"]["joy"],
        'sadness': info_dic["emotion"]["sadness"],
    }
    res_dic["dominant_emotion"] = max(res_dic, key=res_dic.get)
    return res_dic
