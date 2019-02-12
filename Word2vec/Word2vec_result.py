# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
word2vecの学習済みモデルを用いて，単語の類似度・演算を計算
"""

from gensim.models import word2vec

"""類似度"""
def word2vec_sim(model,Target,topn):
	print("単語「" + Target + "」との類似度」")
	sims = []
	try:
		sims = model.most_similar(Target,topn=topn)
		for sim in sims:
			print(sim)
	except:
		print(TARGET_WORD + " is nothing.")
	return sims

"""演算"""
def word2vec_cal(model,pos1,neg1,pos2,topn):
	print("「" + pos1 + "-" + neg1 + "+" + pos2 + "の演算」")
	sims = []
	try:
		sims = model.most_similar(positive=[pos1,pos2],negative=[neg1],topn=topn)
		for sim in sims:
			print(sim)
	except:
		print("\"" + pos1 + "\"or" + neg1 + "\"or" + pos2 + "\" is nothing.")
	return sims


if  __name__ == "__main__":
	INPUT_MODEL = XXXXXXXXXX
	model = word2vec.Word2Vec.load(INPUT_MODEL)

	#モデル情報
	print("コーパスの行数（学習に用いた文章数）：" + str(model.corpus_count))
	print("語彙数：" + str(len(model.wv.vocab)))

	#類似度
	sims = Word2vec_result.word2vec_sim(model,"日本",20)
	for sim in sims:
		print(sim)

	#演算
	sims = Word2vec_result.word2vec_cal(model,"東京都","ドイツ","日本",20)
	for sim in sims:
		print(sim)
