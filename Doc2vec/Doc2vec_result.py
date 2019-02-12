# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
学習済みモデルを用いて，文書の類似度・演算を計算
"""

from gensim import models
import sys
sys.path.append("..")
from Preprocessing import Wakati

"""類似度（モデル内の文書とモデル内の文書）"""
def doc2vec_sim(model,Target,topn):
	print("「" + Target + "（文書）の類似度」")
	sims = []
	try:
	    sims = model.docvecs.most_similar(Target,topn=topn)
	except:
	    print(Target + "is nothing in this model. ")
	return sims

"""類似度（未知文書とモデル内の文書）"""
def doc2vec_sim_unknow(model,Target,topn):
	print("「" + Target + "（未知文書）の類似度」")
	with open(Target,'r',encoding='UTF-8') as file_in:
		text = file_in.read()
		words_list = Wakati.words_list(text)
		vector = model.infer_vector(words_list)

	sims = model.docvecs.most_similar([vector],topn=20)
	return sims

"""演算（モデル内の文書とモデル内の文書）"""
def doc2vec_cal(model,pos1,neg1,pos2,topn):
	pos1_word = pos1.split("\\")[-1]
	neg1_word = neg1.split("\\")[-1]
	pos2_word = pos2.split("\\")[-1]
	print("「" + pos1_word + "-" + neg1_word + "+" + pos2_word + "（文書）の演算」")
	sims = []
	try:
		sims = model.docvecs.most_similar(positive=[pos1,pos2],negative=[neg1],topn=topn)
	except:
		print("\"" + pos1 + "\"or" + neg1 + "\"or" + pos2 + "\" is nothing.")
	return sims

"""演算（未知文書とモデル内の文書）"""
def doc2vec_cal_unknown(model,pos1,neg1,pos2,topn):
	pos1_word = pos1.split("\\")[-1]
	neg1_word = neg1.split("\\")[-1]
	pos2_word = pos2.split("\\")[-1]
	print("「" + pos1_word + "-" + neg1_word + "+" + pos2_word + "（未知文書）の演算」")
	with open(pos1,'r',encoding='UTF-8') as file_in:
		text = file_in.read()
		words_list = Wakati.words_list(text)
		pos1_vec = model.infer_vector(words_list)
	with open(neg1,'r',encoding='UTF-8') as file_in:
		text = file_in.read()
		words_list = Wakati.words_list(text)
		neg1_vec = model.infer_vector(words_list)
	with open(pos2,'r',encoding='UTF-8') as file_in:
		text = file_in.read()
		words_list = Wakati.words_list(text)
		pos2_vec = model.infer_vector(words_list)

	sims = model.docvecs.most_similar(positive=[pos1_vec,pos2_vec],negative=[neg1_vec],topn=topn)
	return sims

if __name__ == '__main__':
	INPUT_MODEL = XXXXXXXXXX
	model = models.Doc2Vec.load(INPUT_MODEL)

	#モデル情報
	print("文書数：" + str(model.corpus_count))
	print("語彙数：" + str(len(model.wv.vocab)))

	#類似度（モデル内の文書とモデル内の文書）
	Target = XXXXXXXXXX
	sims = Doc2vec_result.doc2vec_sim(model,Target,20)#類似度
	for sim in sims:
	    print(sim)

	#類似度（未知文書とモデル内の文書）
	Target_unknown = XXXXXXXXXX
	sims = Doc2vec_result.doc2vec_sim_unknow(model,Target_unknown,20)#類似度（未知文書）
	for sim in sims:
	    print(sim)

	#演算（モデル内の文書とモデル内の文書）
	pos1 = XXXXXXXXXX
	pos2 = XXXXXXXXXX
	neg1 = XXXXXXXXXX
	sims = Doc2vec_result.doc2vec_cal(model,pos1,neg1,pos2,20)#演算
	for sim in sims:
	    print(sim)

	#演算（未知文書とモデル内の文書）
	pos1_unknown = XXXXXXXXXX
	pos2_unknown = XXXXXXXXXX
	neg1_unknown = XXXXXXXXXX
	sims = Doc2vec_result.doc2vec_cal_unknown(model,pos1_unknown,neg1_unknown,pos2_unknown,20)#演算（未知文書）
	for sim in sims:
	    print(sim)
