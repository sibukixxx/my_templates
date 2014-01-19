

# Go言語標準のtestingパッケージが個人的に使いづらかったのがきっかけ

個人的にカジュアルにTDDをしたかったので、PythonでいうassertEqualみたいなものが無いtestingパッケージが個人的に使いづらかったというだけです。(※筆者はPythonをよく使っています)

# 単なるユニットテストならgithub.com/stretchr/testify/assertパッケージが良いと思った

これです。

- https://github.com/stretchr/testify

testifyパッケージの下にassert, http, mockパッケージがあって、それぞれ独立して使うことが出来ます。

importするときは、事前に`go get github.com/stretchr/testify`を行い、コード内部でこんな感じにimportすれば以下のように使えます。公式サイトの例のままですが。

```example.go
package yours

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {

  assert.True(t, true, "True is true!")

}
```

詳しくは[githubリポジトリのREADME](https://github.com/stretchr/testify/blob/master/README.md)のInstallationの項目を読めば分かると思います。

`assert.True(t, true, "True is true!")`のように、Pythonのunittestモジュールライクな関数が手頃に使えるので、testingパッケージの使い方が分からなかった私でも簡単に使えました。私はこれでGo言語のTDDを始められたといっても過言ではないです。

どんな便利関数があるかは[assertパッケージのAPIドキュメント](http://godoc.org/github.com/stretchr/testify/assert)を読めばいいと思いますよ。

私はよく知らなかったんですが、'A lightweight RESTful web framework for Go'と謳っている[goweb](https://github.com/stretchr/goweb)を[作った会社(の人たち)](https://github.com/stretchr)が作っているみたいなので、定期的にメンテされそうな気がするのも個人的にはポイントだったので挙げてみました。

どういう風に作っているのか気になったのでtesting/assertパッケージのソースコードを少し見てみましたが、それほど大きくないパッケージで、標準のtestingパッケージをreflectパッケージとか活用した薄めなラッパーなので、私みたいなGo言語初心者はソースコード読んでみると勉強になると思います。特にreflectパッケージの使い方とか。

testify/assertパッケージだけでなく、testify/mockパッケージもあるので、モックを使う機会があったらこっちも試してみたいですね。モックに関してはこちらの[gomock](https://code.google.com/p/gomock/)の方がデファクトなのかもしれませんが。

# BDDスタイルのテストを書きたい!!!という人はこういったものがあります

これらです。他にもあるとは思いますが。

- https://github.com/onsi/ginkgo
- https://github.com/r7kamura/gospel

私はたまたま[こういった記事をたまたま最初に見た](http://pivotallabs.com/announcing-ginkgo-and-gomega-bdd-style-testing-for-golang/)ので、ginkgoの方を使い始めましたが、後者のgospelは日本の[@r7kamura](https://twitter.com/r7kamura)さんが作っていますし、以下のようなブログ記事を書いて使い方も説明してあるので使い方に詰まったら質問しやすいかと思います。

- [Go言語のテスト用ライブラリとGospel](http://r7kamura.hatenablog.com/entry/2013/10/06/231236)

…まあ、上記どちらの方が使いやすいかというより、どっちかというとRSpecのようなBDDスタイルのテスティングフレームワークを使った経験があるかどうかで使いやすさが全然違うと思いました。私はRSpecみたいなものを使ったことが無かったのでginkgoのドキュメントを読んでいるとき、Contextとか色々あって最初意味不明でしたね。今でも意味がよく分かってないと思います。

## 追記(2013/10/29): 他の方のGo言語テスティングフレームワーク関連の記事

私よりも詳しく上記パッケージ+αを紹介していて、かつWindows関連の情報を記載している記事を見かけたのでリンクしておきます。

- [go言語のテスティングフレームワークについて - さにあらず](http://taichi.hatenablog.com/entry/2013/10/28/215532)

# Go言語のデファクトなテスティングフレームワークが欲しくなってきています

余裕が無くて標準のtestingパッケージ以外には上記二つのパッケージしか試せていないのですが、どうやってテストを書けばいいのか分からなくなってくることが多いし、LLとは違ってビルド時に型間違いとか気づきやすくなっているとは言ってもテストしたくなる箇所も割とあるので、デファクトなテストフレームワーク、というかGo言語らしいテストのやり方決定版みたいなものが早く共有されて欲しいなあ、と最近思っています。