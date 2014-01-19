########
vagrantのansibleプロビジョニングを試してみた
########

:日時: 2014-01-16
:作: @sibukixxx
:バージョン: 0.2.0

**参考URL**

- `時雨堂を支える技術 <https://gist.github.com/voluntas/6308998>`_
- `時雨堂を支える環境 <https://gist.github.com/voluntas/6333304>`_
- `時雨道場 <https://gist.github.com/voluntas/6831251>`_

仕事
====

時雨堂ではお仕事を募集しております。

- Web アプリケーション (主に Python/Django)
- ネットワークサーバ(主に Erlang/OTP)
- サーバサイド設計
- テストツール
- 教育 (Python/Django や Erlang/OTP)
- コードや設計のレビュー
- タスク管理

色々対応可能です。

まずはご連絡頂ければお話しを伺いに参ります。

:mail: contact at shiguredo.jp

卒業
====

3 ヶ月間立ちまして、無事 2013-12-27 に卒業しました。

今後は就職先と相談しながらにはなりますが、
週 1 程度時雨堂で次のレベル目指して修行予定です。

ちなみに、修行していた人の Twitter アカウントは @nakopage です。

概要
====

**この時雨道場は無償で提供しております**

ふとしたきっかけからウェブプログラマを目指している方の修行をお手伝いすることになった。
ということで、方針、教えた内容などを記録していく。

前提
====

- ほぼプログラミング経験なし
- 気合いと根性あり
- IT 業界経験あり
- 就職先決定!!
- 時雨堂に好きな時間に来て好きな時間だけ勉強して好きなときに帰る
- たまに時間があるとき @voluntas が面倒を見る

目標
====

- スケールしないウェブアプリを作れるようになる
- 問題を発見し、修正出来るようになる
- 新機能をイメージできるようになる
- 就職先で力尽きない技術を身につける

方針
====

- 自分たちが知らないことは教えない
- ウェブプログラマの基礎を身につける

  - フロント、サーバサイド、インフラ、チーム開発
- 流行技術を「あたかも当たり前」として伝える

  - Vagrant からはじまり Ansible など
- 直近で必要となる技術を教える
- スパルタ

  - 遠慮無く鞭を振るってます

自分の言葉でまとめる
--------------------

自分の勉強ノートを Gist で作らせています。

そこにまとめる際、ウェブサイトのコピペでは無く自分の言葉でまとめさせています。
理解して自分の武器するのが目的なので、「わかったつもりにならない」というのが大事だと伝えています。

そのためにも、自分の言葉でまとめることが大切です。

わからないを知る
----------------

勉強していて一番危険なのは「わかったつもりになる」事です。
これはとてもコワイ事なのでまずは「自分がわからない事」を明確にするという事を伝えています。

わからないという事があるというのは大切なことで、
別に恥では無いをという事をしつこく伝えています。

世の中にはわかることよりわからないことの方が多いので、
メモを取るときはとにかくわからなかった事を明確にさせています。

そして、わからない点をざっと自分で調べたけどわからない場合は、聞いてもらうようにします。
こちらも全部わかるわけでは無いので、お互いわからない場合は一緒に調べていきます。

沢山のわからないを少しずつ理解していくことが大切だと考えています。

また、全部わかる必要は無く、
わからないのは「わからないという認識のまま残しておく」というのも大事です。

色々学んで成長すればいつの日か「わかる」タイミングが来るとと考えています。

環境
====

**単に修行者の持っているマシンです**

:OS: Mac OS X 10.8.5
:PC: MBP 13 Retina

学習
====

フェーズ 1
----------

- Python
- Django
- SQLite
- MySQL
- Vim
- reStructuredText
- Git

フェーズ 2
----------

- Ansible
- Vagrant
- Packer
- VirtualBox
- PyCharm

フェーズ 3
----------

- JavaScript
- Bootstrap
- AWS
- Zsh
- tmux

フェーズ 4
----------

- nginx
- supervisor
- gunicorn

フェーズ 5
----------

- Redis
- Elasticsearch

サービス
--------

- Trello
- GitHub
- BitBucket
- drone.io
- grove.io
- Hall

日々
====

- 日数は「教えた日」であって「過ぎた日」では無いです

Python
------

暗記するくらい読む事と伝えている

Python チュートリアル — Python 2.7ja1 documentation
    http://docs.python.jp/2/tutorial/

Django
------

Django チュートリアル part 1 ~ 6 までを繰り返し行う

Writing your first Django app, part 1 | Django documentation | Django
    https://docs.djangoproject.com/en/1.5/intro/tutorial01/

Gist
----

調べたことを全てメモをする

書籍
----

- `初めてのPython 第3版 <http://www.amazon.co.jp/dp/4873113938/twistedmind-22/ref=nosim/>`_
- `Head First SQL ―頭とからだで覚えるSQLの基本 <http://www.amazon.co.jp/dp/4873113695/twistedmind-22/ref=nosim/>`_
- `アジャイルレトロスペクティブズ　強いチームを育てる「ふりかえり」の手引き <http://www.amazon.co.jp/dp/4274066983/twistedmind-22/ref=nosim/>`_


1 日目
------

**色々なサービスのアカウントを作る**

- アカウント名は統一して作る

  - GitHub アカウントの作成

    - https://github.com/
  - BitBucket アカウントの作成

    - https://bitbucket.org/
  - Trello アカウントの作成

    - https://trello.com/
- Trello の使い方

  - カード、リスト、チェックリスト、リプライのやり方
- タスク管理の基本的考え方

  - to-do / doing / done の基本的な考え方
- バージョン管理の基本的考え方

  - なぜバージョン管理が必要なのか
- Xcode インストール
- Command Line Tools インストール
- MacPorts インストール

  - dmg でインストール
- MacPorts 経由で Python 2.7 インストール

  - $ sudo port install python27
- Alfred の使い方

  - http://www.alfredapp.com/
- Terminal の設定

  - フォントを osaka-mono へ変更
  - フォントサイズを大きめへ変更
- Gist の使い方

  - rst 形式で書く
- reStructuredText の使い方

  - http://www.planewave.org/translations/rst/quickref.html
  - http://www.planewave.org/translations/rst/quickstart.ja.html

2 日目
------

**MacPorts を使って Python 環境を整える**

- MacPorts で py27-setuptools のインストール
- MacPorts で py27-pip のインストール
- MacPorts で py27-virtualenv のインストール

- .virtualenv 以下に default という名前で virtualenv を追加

  - $ virtualenv default ~/.virtualenv

- 宿題: ターミナル起動時に default/bin/activate が適用されるようにする

  - ヒント

    - ~/.bashrc
    - ~/.bash_profile
    - source コマンド

3 日目
------

**Django をインストールしてチュートリアルをスタートする**

- virtualenv (default) の pip を使って Django をインストールする

  - $ pip install django
- Django Tutorial (バージョン 1.5) を Part1 からやりはじめる

4 日目
------

**.vimrc を設定する**

- .vimrc にスパルタ設定を追加する

  - 矢印と BS を使わせない設定

.. code-block:: vim

    noremap <Up> :<C-u>echohl WarningMsg \| echo "Don't use Up key!!! Press [k]" \| echohl None<CR>
    noremap! <Up> <ESC>:<C-u>echohl WarningMsg \| echo "Don't use Up key!!! Press [ESC][k]" \| echohl None<CR>
    noremap <Down> :<C-u>echohl WarningMsg \| echo "Don't use Down key!!! Press [j]" \| echohl None<CR>
    noremap! <Down> <ESC>:<C-u>echohl WarningMsg \| echo "Don't use Down key!!! Press [ESC][j]" \| echohl None<CR>
    noremap <Left> :<C-u>echohl WarningMsg \| echo "Don't use Left key!!! Press [l]" \| echohl None<CR>
    noremap! <Left> <ESC>:<C-u>echohl WarningMsg \| echo "Don't use Left key!!! Press [ESC][l]" \| echohl None<CR>
    noremap <Right> :<C-u>echohl WarningMsg \| echo "Don't use Right key!!! Press [h]" \| echohl None<CR>
    noremap! <Right> <ESC>:<C-u>echohl WarningMsg \| echo "Don't use Right key!!! Press [ESC][h]" \| echohl None<CR>
    noremap <BS> :<C-u>echohl WarningMsg \| echo "Don't use BackSpace key!!! Press [ctrl-h]" \| echohl None<CR>
    noremap! <BS> <ESC>:<C-u>echohl WarningMsg \| echo "Don't use BackSpace key!!! Press [ctrl-h]" \| echohl None<CR>

- Django の MTV モデルを理解する

  - Model とは何か
  - Template とは何か
  - View とは何か
  - https://docs.djangoproject.com/en/dev/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names

5 日目
------

**Django チュートリアルを始める**

- pip install django
- python manage.py syncdb

6 日目
------

**SQLite3 の使い方**

- sqlite3 コマンドの使い方

  - .tables
  - select * from table
- Django の models.py の書き方

  - ForeignKey の使い方とイメージ
- ウェブアプリとデータベースの関係性
- SQLite3 と Django ORM の関係性

7 日目
------

**Git の使い方と Django アプリの作成開始**

- Git の使い方

  - とにかく困ったら git status
  - ステージングの概念
  - git diff で変更履歴
  - git add でステージングに追加
  - git commit でステージングにあるファイルをコミットする

    - コミットログは「〜する」などの命令形で書く事
    - 日本語で問題ない
  - git push で GitHub へ送る
  - git log コミットログが見れる
  - .gitignore は「Git の管理下に入れないファイルを指定する」

    - *.pyc などを指定する

- git-flow を少し触る

  - git-flow インストール

    ::

        $ curl -L -O https://raw.github.com/nvie/gitflow/develop/contrib/gitflow-installer.sh
        $ sudo bash gitflow-installer.sh
  - develop と master ブランチの役割を説明する
  - feature と release ブランチの役割説明をする

- GitHub にリポジトリを作る

  - ssh の鍵を生成する

    ::

        $ ssh-keygen -b 2048
        $ cat .ssh/id_rsa.pub

  - git flow init でリポジトリを初期化する
  - git remote add origin ... でリモートの GitHub を連携させる
  - git push でローカルのデータを反映する
  - develop をデフォルトのブランチに設定する
  - README.rst を作る

    - アプリの説明などを書いていく、日本語で問題ない

- Django でアプリケーションを作り始めた

  - 簡単な EC サイトを作る
  - ただ最初から大きいサイトではなく、まずは勉強がてら色々作って壊していくのを想定
- まずは app は作らず project で作れらたところに views.py や models.py を作っていく

構成::

    project/
        manage.py
        core/
            __init__.py
            templates/
                core/
                    *.html
            wsgi.py
            settings.py
            models.py
            views.py
            urls.py

- 商品の追加、削除、更新、一覧の URL を決めるところからスタート

  - 商品というのは出品する商品を想定
- 名前重要ということで、色々議論しながら考えさせる
- 正規表現の説明 \d+ の意味を理解する
- url にバインドするビューは一目見て何をする処理なのか理解する
- url で一覧を取るときは複数形にする

  - ただしこれは絶対では無く、参考程度として覚える事
  - url 設計に絶対は無いのでそのアプリ毎に考える
- まずは urls を決めて、その後 models を簡単に作ったら、views を埋めていく
- templates は最後で良い

  - HTML は後回し

7.5 日目
--------

**宿題へのコメント**

- flake8 の導入

  - pip install flake8
  - flake8 を実行してエラーが出ないようにする
- Django アプリにコメント

  - import の順番 (ビルトイン、サードパーティ、オレオレ)
  - コメントは行の上へ
  - # coding: utf8

8 日目
------

**GitHub で PR**

- git-flow で feature ブランチの切り方

  - git flow feature start <branch-name>
- git-flow で feature ブランチを remote に公開する方法

  - git flow feature publish <branch-name>
- GitHub で feature ブランチを Pull-Request(PR) する方法

  - description には「どんな変更なのかを箇条書きで書く事」
- 今後は全て git-flow で feature ブランチを機能毎に切って PR をする

  - PR 後 レビューを受けて修正して push する
  - マージされたら git pull して反映する
- 全ての作業を develop で行わず feature ブランチで行う事
- Django アプリの開発

  - とにかく遠回りさせる
  - トップページを作る
  - 商品一覧ページを作る
  - 商品詳細ページを作る
- リクエストの流れの概念をつかむ
- わかったきにならない
- 「なぜこうなるのか」を説明出来るようにする
- urls -> views -> templates という流れを理解する
- クエリーの all と filter と get の違いを理解する
- urls の正規表現で判定した部分を views に持ってくるところを理解する
- shortcut の render を使う
- context がテンプレートに渡されることを理解する
- とにかくなんとなく動くやコピペすれば動くをやめる

- commit する前に flake8 でコードをチェックする

9 日目
------

**HTTP とウェブアプリのテスト**

- HTTP プロトコル

  - ステータスコードを覚える

    - 200, 302, 400, 401, 403, 404, 500, 503
  - メソッドを覚える

    - GET / POST
    - GET は情報を読み込む
    - POST は情報を書き込む
- ウェブアプリでの一番簡単なテスト

  - urls.py でディスパッチされるページに request を投げて 200 が返ってくるかどうかを確認
  - 毎回ブラウザで確認しなくていい
  - 最初にテストを書いておけば実装するとき確認が楽、ただ別に後から書いてもいい
  - まずは色気を出さないで、簡単なテストから学ぶ

10 日目
-------

**Sentry のインストール**

- エラートラッカー
- 障害状況が整理される

- https://gist.github.com/voluntas/6937403

- まずは動かしてみる
- 就職先に導入出来るよう、いじってみる