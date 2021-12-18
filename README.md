## nlp
このレポジトリはpythonで自然言語処理を学習するためのものです。
* * *
#### リポジトリをクローン
```
mkdir NLP
cd NLP
git clone git@github.com:yujiromorota07/NLP.git
```
#### dockerセットアップ
dockerイメージをビルドしてコンテナを立ち上げる
```
docker compose up -d --build
```
立ち上げたコンテナへ接続
```
docker compose exec nlp bash
```
####pythonファイル実行
pythonファイルが存在する一つ下のディレクトリに移動
```
cd nlp
```
test.pyを実行
```
python test.py
```
#### ライブラリの追加
```
pip install [ライブラリ名]
```
環境を保存するにはDockerfileに以下のように記述する。  
例えばnumpyを入れる
Dockerfileの一番下の行に
```
RUN pip install numpy
```
を追加して、ビルドをやり直してコンテナ起動
```
docker compose up -d --build
```
コンテナに接続して
```
docker compose exec nlp bash
```
pythonファイルを実行
```
python test.py
```