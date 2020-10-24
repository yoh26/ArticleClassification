To Japanese description

## Overview

ArticleClassification categorizes news titles.

## Details

### 1. Collecting data

News titles are collected from [News API](https://newsapi.org/).

The following labels are appended to news titles, then write in **Dataset.txt**.

○labels

|Categories|Labels|
|--------|------|
|business|0|
|entertainment|1|
|health|2|
|science|3|
|sports|4|
|technology|5|

○Data examples

> Omaha’s megabillionaire down the street — Warren Buffett — set to celebrate his 90th birthday 0<br>
Prince Harry, Meghan Markle have received millions of dollars in gifts: Book 1<br>
This Beloved Tourist Destination Has Become a COVID Superspreader 2<br>
An Asteroid Is Headed for Earth Just Before Election Day 3<br>
LIVE: Coman Heads Bayern Munich Ahead of PSG in Champions League Final 4<br>
SpaceX Crew Dragon capsule arrives in Florida for next NASA astronaut launch 5<br>


### 2. Preprocessing data

1. Remove duplication

   There are some duplication in Dataset. It needs to remove duplication.

2. Remove punctuation

3. Change to lowercase

4. Change all numbers to 0

5. Remove Stopwords

6. Remove over max length data

7. Change to num vectors and 0 pad

8. Split data

   Split dataset to train dataset and validation dataset

9. Split data to batches

### 3. Assemble model

The model is assembled by Sequential model of Tensorflow.keras.

### 4. Evaluate

○Result

Loss: 0.57430499792099

Accuracy: 0.8771112561225891

![Loss_Accuracy](https://user-images.githubusercontent.com/69742531/96570950-eb659780-1305-11eb-8939-ecca360ce4f6.png)


## 概要

ニュースタイトルからニュースのカテゴリ分けを行う

## 詳細

### 1. データ収集

データ収集には[News API](https://newsapi.org/)を利用

取得したニュースタイトルの末尾に下記のラベルを付与し、**Dataset.txt**へ書きこんでいく

○カテゴリラベル

|カテゴリ|ラベル|
|--------|------|
|business|0|
|entertainment|1|
|health|2|
|science|3|
|sports|4|
|technology|5|

○データ例

> Omaha’s megabillionaire down the street — Warren Buffett — set to celebrate his 90th birthday 0<br>
Prince Harry, Meghan Markle have received millions of dollars in gifts: Book 1<br>
This Beloved Tourist Destination Has Become a COVID Superspreader 2<br>
An Asteroid Is Headed for Earth Just Before Election Day 3<br>
LIVE: Coman Heads Bayern Munich Ahead of PSG in Champions League Final 4<br>
SpaceX Crew Dragon capsule arrives in Florida for next NASA astronaut launch 5<br>


### 2. データ下準備

1. 重複データ削除

　　データセットには重複が存在するため、重複を削除する

2. 記号削除

3. 小文字化

4. すべての数字を0に変換

5. Stopwordsの削除

6. 指定単語数以上のデータを削除

7. 数値ベクトルへ変換&0パッド

　　単語を数値へ変換、数値ベクトルを作成し、一番長いベクトルと同じ長さになるように0埋めを行う

8. データ分割

　　訓練データとテストデータへ分割する

9. バッチに分割

### 3. モデル構築

モデル構築にはTensorflow.kerasのSequentialモデルを使用

### 4. 評価

○学習結果

Loss: 0.57430499792099

Accuracy: 0.8771112561225891

![Loss_Accuracy](https://user-images.githubusercontent.com/69742531/96570950-eb659780-1305-11eb-8939-ecca360ce4f6.png)
