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

### 3. モデル作成

### 4. 評価
