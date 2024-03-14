[公式ドキュメント](https://flask.palletsprojects.com/en/3.0.x/)
***
# how to
Pythonファイルと同階層に移動し、`flask --app "ファイル名" run (--debug)`
--debug：デバッグモード。コード変更等をリアルタイム反映

***
# ファイル説明
- hello.py
  - 単一ファイルでのFlask実行

- escape.py
  - 変数とエスケープ処理
  - ブラウザからの入力のエスケープ処理
  - インジェクション攻撃から保護するためにエスケープする

- routing.py
  - デコレータ(@)で「route()関数」の使い方

- url.py
  - 特定の関数への URL を構築