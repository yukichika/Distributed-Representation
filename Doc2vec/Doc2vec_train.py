#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import collections
import random
import json
from gensim import models
from gensim.models.doc2vec import LabeledSentence
import sys
sys.path.append("..")
from Preprocessing import File_operation

"""パラメータの設定"""
corpus = "Wiki_1012155"
dm = 1
model_name = "dm"
size = 20
window = 5
min_count = 5
iteration = 1
epoch = 20
RADOM_NUMBER = 100
#PASSING_PRECISION = 93#閾値

"""読み込み先・保存先"""
INPUT = XXXXXXXXXX
OUTPUT_DIR = XXXXXXXXXX
OUTPUT_MODEL_NAME = corpus + "_" + model_name + "_" + str(size) + "_w" + str(window) + "_m" + str(min_count)

"""ログ出力"""
logging.basicConfig(filename=os.path.join(OUTPUT_DIR,OUTPUT_MODEL_NAME+".log"),format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

"""学習に与えるリストを取得"""
def corpus_to_sentences(dictionary):
    docs = [LabeledSentence(words=dictionary[x], tags=[x]) for x in dictionary]
    return docs

"""学習"""
def train(sentences):
    model = models.Doc2Vec(size=int(size),
                           dm=int(dm),
                           min_count=int(min_count),
                           window=int(window),
                           iter=int(iteration))

    model.build_vocab(sentences)

    for x in range(int(epoch)):
        print("学習回数：" + str(x+1))
        model.train(sentences,total_examples=model.corpus_count,epochs=model.iter)

        # ranks = []
        # for doc_id in range(RADOM_NUMBER):
        #     inferred_vector = model.infer_vector(sentences[doc_id].words)
        #     sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
        #     rank = [docid for docid, sim in sims].index(sentences[doc_id].tags[0])
        #     ranks.append(rank)
        # print(collections.Counter(ranks))

        model.save(os.path.join(OUTPUT_DIR,OUTPUT_MODEL_NAME + "_" + str(x+1) + ".model"))

    return model

if __name__ == '__main__':
    sentences = []
    if os.path.isdir(INPUT) == True:
        print("Multi")
        filelists = File_operation.get_all_paths(INPUT)
        for i,file in enumerate(filelists):
            with open(file,'r',encoding='UTF-8') as f:
                json_datas = json.load(f)
                sentence = corpus_to_sentences(json_datas)
                sentences.extend(sentence)
                print(len(sentence))
    else:
        print("One")
        with open(INPUT,'r',encoding='UTF-8') as f:
            json_datas = json.load(f)
            sentence = corpus_to_sentences(json_datas)
            sentences.extend(sentence)
            print(len(sentence))
    print("ファイル数：" + str(len(sentences)))
    train(sentences)
