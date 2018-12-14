# !/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
import logging
import codecs
import os
from gensim.models import word2vec

"""設定ファイルの読み込み"""
inifile = configparser.ConfigParser(allow_no_value = True,interpolation = configparser.ExtendedInterpolation())
inifile.readfp(codecs.open("./Word2vec_train.ini",'r','utf8'))

"""読み込み先・保存先の設定"""
INPUT_FILE = inifile.get('setting','INPUT_FILE')
OUTPUT_DIR = inifile.get('setting','OUTPUT_DIR')
OUTPUT_MODEL_NAME = inifile.get('setting','OUTPUT_MODEL_NAME')

"""パラメータの読み込み"""
size = inifile.get('params','size')
sg = inifile.get('params','sg')
window = inifile.get('params','window')
min_count = inifile.get('params','min_count')
iteration = inifile.get('params','iteration')
epoch = inifile.get('params','epoch')

"""進捗表示・log保存"""
logging.basicConfig(filename=os.path.join(OUTPUT_DIR,OUTPUT_MODEL_NAME+".log"),format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

"""学習"""
def train(sentences):
	model = word2vec.Word2Vec(size=int(size),
                          	  sg=int(sg),
                              min_count=int(min_count),
                              window=int(window),
						      iter=int(iteration))
	model.build_vocab(sentences)

	for x in range(int(epoch)):
		print("学習回数：" + str(x+1))
		model.train(sentences,total_examples=model.corpus_count,epochs=model.iter)
		model.save(os.path.join(OUTPUT_DIR,OUTPUT_MODEL_NAME + "_" + str(x+1) + ".model"))

if __name__ == '__main__':
	sentences = word2vec.LineSentence(INPUT_FILE)
	train(sentences)
