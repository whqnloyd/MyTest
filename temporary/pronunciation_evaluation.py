"""
Created on Fri May 18 10:49:30 2018
@author: Yifeng He and Hao Liu

This file contains the API for pronunication evaluation: evaluate_pronunication()
"""
import requests
import json


def process_audio_score(results):
    scores = {}
    text_score = results['text_score']['quality_score']
    word_score_list = []
    for word_info in results['text_score']['word_score_list']:
        word_score = {}
        word_score.update({'word': word_info['word']})
        word_score.update({'word_score': word_info['quality_score']})

        phone_score_list = []
        for phone_info in word_info['phone_score_list']:
            phone_score = {}
            phone_score.update({'phone': phone_info['phone']})
            phone_score.update({'phone_score': phone_info['quality_score']})
            phone_score_list.append(phone_score)

        word_score.update({'phones': phone_score_list})
        word_score_list.append(word_score)
    scores.update({'text_score': text_score})
    scores.update({'word_score_list': word_score_list})
    return scores


def evaluate_pronunication(input_audio_file, input_text):
    url = 'https://consumer.speechace.com/api/scoring/text/v0.1/json?key=HXpStHKnzrR2X%2BuEXk8vx0IW8H5IQbVJbMQ0%2FHhZR3PU%2FXLGiiTdgkI2ZvDH6hf7&user_id=002'
    files = [
        ('user_audio_file', open(input_audio_file, 'rb')),
    ]
    data = [
        ('text', input_text),
        ('dialect', 'en-us'),
        ('user_id', '1234')
    ]
    results = requests.post(url, files=files, data=data).text
    try:
        return process_audio_score(json.loads(results))
    except:
        return {}


if __name__ == '__main__':
    input_audio_file = './data/pronunication_evaluation_sample.wav'
    input_text = 'Some parents admire famous athletes as strong role models, so they name their children after them'
    score_results = evaluate_pronunication(input_audio_file, input_text)
    print(score_results)
