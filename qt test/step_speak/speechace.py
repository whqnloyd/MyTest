"""
Created on Fri May 18 10:49:30 2018
@author: Yifeng He and Hao Liu
This file contains the API for pronunication evaluation: evaluate_pronunication()
"""
import requests


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


def evaluate_pronunication(input_blob, input_text):
    # us server api
    # url = 'https://api.speechace.co/api/scoring/text/v0.1/json?key=cQ4fZtrloOfOcwBo9TnPCkk0%2FY8yXxR1%2BbiBDJl3kKwjeMvHcuUuCc%2Fq3exqfLQVDk8Csi9upxSDdHztAbvzetgkbb7oMHtFnt0T11VGxfrFeetgzkF4COWIDidsqOeD'
    # Singapore server api
    url = 'https://consumer.speechace.com/api/scoring/text/v0.1/json?key=HXpStHKnzrR2X%2BuEXk8vx0IW8H5IQbVJbMQ0%2FHhZR3PU%2FXLGiiTdgkI2ZvDH6hf7'

    files = {'user_audio_file': input_blob}
    data = {'text': input_text, "dialect": 'en-us', "user_id": '1234'}
    response = requests.post(url, data=data, files=files).json()

    try:
        return process_audio_score(response)
    except:
        return {}


def sort_word_scores(result):
    list_words_scores = result['word_score_list']
    list_pairs = []
    for s in list_words_scores:
        list_pairs.append((s['word'], s['word_score']))
    list_pairs_sorted = sorted(list_pairs, key=lambda x: x[1])
    return list_pairs_sorted


if __name__ == '__main__':
    input_audio_file = './data/pronunication_evaluation_sample.wav'
    input_text = 'Some parents admire famous athletes as strong role models, so they name their children after them'
    score_results = evaluate_pronunication(input_audio_file, input_text)
    print(sort_word_scores(score_results))