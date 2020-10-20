# ArticleClassification

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

> Omaha’s megabillionaire down the street — Warren Buffett — set to celebrate his 90th birthday 0

> Prince Harry, Meghan Markle have received millions of dollars in gifts: Book 1

> This Beloved Tourist Destination Has Become a COVID Superspreader 2

> An Asteroid Is Headed for Earth Just Before Election Day 3

> LIVE: Coman Heads Bayern Munich Ahead of PSG in Champions League Final 4

> SpaceX Crew Dragon capsule arrives in Florida for next NASA astronaut launch 5


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

モデル構築には、Tensolflow.kerasのSequentialモデルを使用

### 4. 評価

○学習結果
