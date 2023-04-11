import yaml
import json
from loguru import logger

global_setting = yaml.safe_load(open('./yamls/General.yaml', 'r', encoding='UTF-8'))
rand_sents = {
    "zh-cn": json.load(open('./jsons/zh-cn/rand_sents.json', 'r', encoding='UTF-8')),
    "en-us": json.load(open('./jsons/en-us/rand_sents_en.json', 'r', encoding='UTF-8')),
    "fr-fr": json.load(open('./jsons/fr-fr/rand_sents_fr.json', 'r', encoding='UTF-8')),
    "es-es": json.load(open('./jsons/es-es/rand_sents_es.json', 'r', encoding='UTF-8')),
    "ja-jp": json.load(open('./jsons/ja-jp/rand_sents_jp.json', 'r', encoding='UTF-8')),
    "ko-kr": json.load(open('./jsons/ko-kr/rand_sents_kr.json', 'r', encoding='UTF-8')),
    "ru-ru": json.load(open('./jsons/ru-ru/rand_sents_ru.json', 'r', encoding='UTF-8')),
    "zh-hk": json.load(open('./jsons/zh-hk/rand_sents_hk.json', 'r', encoding='UTF-8')),
}
voices = yaml.safe_load(open('./yamls/Voices.yaml', 'r', encoding='UTF-8'))
def bot_config(name: str):
    try:
        return global_setting[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None


def sents_config(name: str, lang: str):
    try:
        return rand_sents[lang][name]
    except KeyError:
        logger.error(f'宁确定有{lang} - {name}这个东西?')
        return None


def students_voices(name: str):
    try:
        return voices[name]
    except KeyError:
        logger.error(f'宁确定有{name}这个东西?')
        return None