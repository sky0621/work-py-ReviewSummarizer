# 文章要約ツール
## ■修正履歴
###### 2016/09/15 公開
## ■紹介
###### 最近、自然言語処理や機械学習に手を出し始めたので、それ絡みのツールを作ろうと思い、ネタを探していたのですが、
###### ニュースアプリって、長いニュースを”要するに”でまとめたりしてて、時間ないとき重宝するので、
###### グルメサイトや旅行サイトの口コミとかも、「参考にしたいけど、全部読むの大変」という意見があるんじゃないかと思い、適用してみました。
###### とはいえ、肝になる”文章要約”ロジックは他の人が作ったものなので、むしろ他人のツールの紹介ですが。
http://blog.recruit-tech.co.jp/2015/10/30/summpy-released/
　
###### 事例で言うと、
###### 「
###### 女子会で利用させて頂きました(^^)
###### 店内の照明は明るすぎず暗すぎずちょうど良くて、ついつい長居をしてしまいそうなとても落ち着いた雰囲気…
###### 池や水が流れる壁などの内装は南国のようです♪
###### ビリヤードやダーツもあるので合コンなどにも良さそうだなあ…と思いました(>_<)
###### 女の子ならきっと喜んでしまうお店ではないでしょうか♪
###### デート、合コン、女子会、色んな用途に使えそうなので、また是非行きたいです♪
###### 」
###### ↑こんな口コミが、
###### 「
###### 女子会で利用させて頂きました(^^)
###### 女の子ならきっと喜んでしまうお店ではないでしょうか♪
###### デート、合コン、女子会、色んな用途に使えそうなので、また是非行きたいです♪
###### 」
###### と３行に要約されます。
## ■作成言語
###### 今回の肝である文章要約ツールが要求している Python(2.7) です。
###### フレームワークは軽量な bottle を採用。
http://bottlepy.org/docs/dev/index.html
　
###### フレームワークこそ１ファイルで軽量な bottle を使ったものの、summpyが依存するモジュールがふんだんで pip 駆使しなくてはいけなかったのでVPSに環境用意しました。
###### （最初はHerokuに環境用意したのですが、summpyないしsummpyが依存するモジュールの何かが抵触するのかうまく動きませんでした。）
　
###### 開発に使ったエディタは Intellij つくってる JetBrains の PyCharm です。
