#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MeCab
import os
import json
from tqdm import tqdm

import sys
sys.path.append("..")
from Preprocessing import Delete
from Preprocessing import File_operation
from Preprocessing import Wakati

"""読み込み先・保存先"""
keyword = XXXXXXXXXX
INPUT_DIR = XXXXXXXXXX
OUTPUT_DIR = XXXXXXXXXX

"""ファイルから文書を取得"""
def read_document(path):
    with open(path, 'r', encoding='UTF-8', errors='ignore') as f:
        return f.read()

"""文書のtag(フルパス)と単語のリストをdictionaryで取得"""
def corpus_to_dictionary(corpus):
    dictionary = {}
    docs = [read_document(x) for x in corpus]
    for idx, (doc, name) in enumerate(tqdm(zip(docs, corpus))):
        words = Wakati.words_list(doc)
        dictionary[name] = words
    return dictionary

if __name__ == '__main__':
    print(keyword)
    corpus = File_operation.get_all_paths(INPUT_DIR)
    dictionary = corpus_to_dictionary(corpus)
    with open(os.path.join(OUTPUT_DIR,keyword+".json"),'w',encoding='UTF-8') as file_out:
        json.dump(dictionary,file_out)
