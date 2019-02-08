# Distributed-Representation

## Requirements

This implementation has been tested with the following versions.

```
python 3.6.2
mecab-python 0.996
gensim 3.2.0
```

## How to Use
・Word2vec/Word2vec_train.py  
word2vecの学習を行うプログラム．  

・Word2vec/Word2vec_result.py  
word2vecの単語ベクトルを用いて，単語間の類似度・演算を行うプログラム．  

・Doc2vec/Doc2vec_preprocessing.py  
doc2vecの学習に用いるコーパスの前処理のプログラム．  
Preprocessingから前処理の関数を用いている点に注意．  

・Doc2vec/Doc2vec_train.py  
doc2vecの学習を行うプログラム．  
Preprocessingからファイル操作の関数を用いている点に注意．  

・Doc2vec/Doc2vec_vector.py  
doc2vecの学習済みモデルを用いて，未知文書のベクトル化を行うプログラム．  
Preprocessingから前処理の関数を用いている点に注意．  

・Doc2vec/Doc2vec_result.py  
doc2vecの単語ベクトル・文書ベクトルを用いて，類似度・演算を行うプログラム．
