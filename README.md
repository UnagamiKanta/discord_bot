# Discord上で動く、githubの操作ができるBot
## 使い方
1. DISCORD_API_TOKENとGITHUB_API_TOKENを発行して環境変数に登録
2. main.pyを常に実行させる
## コマンド集(今後追加するかも)
- !repos
  - botが扱えるリポジトリを表示します。後述するmkissueのrepoにコピペすると楽
- !mkissue repo=(リポジトリ名) title=(イシュータイトル) (これ以降任意) body=(イシューテキスト) asignee=(担当者) label=(ラベル","で複数つけられる)
  - issueを建てられる
- !clsissue repo=(リポジトリ名) title=(イシュータイトル)
  - issueを閉じれる
