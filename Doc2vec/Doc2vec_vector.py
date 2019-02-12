#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
学習済みモデルを用いて，未知文書（コーパス外の文書）をベクトル化
"""

import os
import codecs
import pickle
from gensim import models
from tqdm import tqdm

import sys
sys.path.append("..")
from Preprocessing import File_operation
from Preprocessing import Wakati

"""モデルの読み込み"""
INPUT_MODEL = XXXXXXXXXX
model = models.Doc2Vec.load(INPUT_MODEL)

"""読み込み先・保存先"""
keyword = XXXXXXXXXX
INPUT_DIR = XXXXXXXXXX
OUTPUT_DIR = XXXXXXXXXX
filelists = File_operation.get_all_paths(INPUT_DIR)

"""ベクトル化"""
dictionary = {}
for i,file in enumerate(tqdm(filelists)):
    title = file.split("\\")[-1]

    with codecs.open(file,'r','UTF-8',"ignore")as file_in:
        sentence = file_in.read()
        words = Wakati.words_list(sentence)
        vector = model.infer_vector(words)

    dictionary[title] = vector

"""pickleファイルに保存"""
with open(os.path.join(OUTPUT_DIR,keyword + ".pkl"), mode='wb') as f:
    pickle.dump(dictionary, f)
