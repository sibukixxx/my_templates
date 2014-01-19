- `Sphinx-Users.jp <http://sphinx-users.jp/gettingstarted/use_markup.html>`_

.. index:: ベルモール


.. ディレクティブ名:: オプション
:引数:
:パラメータ付き引数: パラメータ

.. っっｄ


.. index:: ベルモール

.. index::
         pair: 遊園地; 那須ハイランドパーク

.. index:
         triple: うさぎや; チャット; お菓子


.. ディレクティブ名:: オプション
         :引数:
   :パラメータ付き引数: パラメータ

* 宇都宮市
* 那須塩原市
* 真岡市

1. まさし
2. みんみん
#. 夢餃子(#を使うと、自動で数字が割り当てられます)

餃子
   宇都宮の名物として有名。餃子の像もある。静岡の浜松がライバル。
ジャズ
   宇都宮はジャズの町としても売り出し中。
   楽器メーカーを多数抱える静岡の浜松がライバル
焼きそば
   知る人ぞ知る宇都宮の名物。専門店多数。なぜかビニール袋で持ち帰る。


**太字**

*斜体*

``リテラル``

`リンク付きテキスト <http://python.org>`_


+---------------------+
|栃木県内の勉強会     |
+========+============+
|宇都宮  |集合知勉強会|
+        +------------+
|        |Objective-C |
+--------+------------+
|西那須野|とちぎRuby  |
+--------+------------+



=========== ==================================
勉強会で使う本
----------------------------------------------
言語        本の名前
=========== ==================================
Ruby        dRubyによる分散・Webプログラミング
Python      集合知プログラミング
Objective-C 詳解Objective-C 2.0
=========== ==================================


.. ディレクティブ名:: オプション
      :引数:
   :パラメータ付き引数: パラメータ

   コンテンツ
   
   
.. image:: fighting_dogs.png


.. index:: ベルモール

.. index::
      pair: 遊園地; 那須ハイランドパーク

.. index:
      triple: うさぎや; チャット; お菓子
   
   
.. ディレクティブ名:: オプション
      :引数:
   :パラメータ付き引数: パラメータ

   コンテンツ
   
.. note::
      注釈です

.. warning::
      警告です！
   
+-------+---------------------------------------------------+
| ".. " | ディレクティブタイプ "::" ディレクティブブロック  |
+-------+                                                   |
        |                                                   |
        +---------------------------------------------------+


.. DANGER::
      Beware killer rabbits!

.. note:: This is a note admonition.
      This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

.. table:: Truth table for "not"

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

.. csv-table:: Frozen Delights!
      :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

.. list-table:: Frozen Delights!
      :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. todo:: ブロック図を書く

.. contents:: これは目次です
      :depth: 2
   
.. csv-table:: 外部ファイル読み込みサンプル
      :file: sample.csv
   :encoding: euc-jp
   :header-rows: 1
   
# 部: オーバーライン付き
* 章: オーバーライン付き
=, セクション
-, サブセクション
^, サブサブセクション
", パラグラフ

.. function:: foo(x)
                 foo(y, z)
   :bar: no

   ユーザから入力されたテキストのうち、１行を返します。
   
Lorem ipsum [#f1]_ dolor sit amet          ... [#f2]_

.. rubric:: 脚注

.. [#f1] 最初の脚注のテキストです。
   .. [#f2] ２番目の脚注のテキストです。

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] 参考になった書籍、論文、URL、その他
