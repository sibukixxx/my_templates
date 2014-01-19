恐らくWebサービス等でAWSを使っているところが増えてきているかと思われます。そして、よく知られているように、AWSはだいたいのことはコンソールコマンドや、各種言語のライブラリで制御できるAPIも公開されていることはご存じだと思います。

最近、自分が働いてるスタートアップにて、例えば新しくインスタンスを立ち上げたさいに、セキュリティーグループに何らかのインスタンスを入れるという手順があるのですが、これを自動化したい！なぜなら面倒くさいし俺は忘れる！という理由から、Pythonでスクリプトを書いてました。

# Botoを使う

そこで、Pythonのライブラリである[Boto](https://github.com/boto/boto)を使うと、これらのインスタンスを立ち上げたり、セキュリティーグループに追加したりといった部分が楽になります。そこでこのBotoライブラリの簡単な概要を説明したいと思います。

# 必要なもの

AWS用のAuthキーを発行しましょう。以下のヘルプの手順をみながら、Keyを発行してもらいます。

* [Getting Your Access Key ID and Secret Access Key](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html)

# 接続してみる

まず最初に、Botoを使ってAWSに接続してみましょう。自分の場合ですと、下のように書いています。

```python
connection = boto.ec2.connect_to_region(
    REGION,
    aws_access_key_id=YOUR_ACCESS_KEY,
    aws_secret_access_key=YOUR_SECRET_KEY)
```

自分が少しはまったところとしては、`region`をどのように指定するかということです。`region`を指定する場合、例えば`ap-northeast-1`のように指定してあげる必要があります

また、`connect_to_region`を使った場合、コネクションの入り口となるインスタンスが発行されます。今後の操作は、基本的にはここからやります。

# セキュリティーグループに各IPをセットしてみる

例えば、現状存在しているセキュリティーグループの一覧を取得してみましょう。

```python
security = connection.get_all_security_groups(groupnames=['foo', 'bar'])
```

このようにすることによって、各セキュリティーグループを取得することができます。横着して詳しくは調べていませんが、ただ`groupnames`で指定した場合、それぞれのセキュリティーグループに接続するためのインスタンスが発行されます。例えば、最初のグループを利用したい場合は、下のようになる?と思います。

```python
security[0].authorize(
    ip_protocol="tcp",
    from_ports=ps[1],
    to_port=ps[1],
    cidr_ip="YOUR.IP/32")
```

ちなみに、ちょっと忘れがちなこととしては、`cidr_ip`の指定のときに、`/32`等をつけないと、エラーが返ってきます。また既にセキュリティーグループに該当IPが存在する場合も、エラーが返ってきます。したがって、下のように`try`してやる必要があります。

```python
try:
    # do it
except EC2ResponseError, e:
    if e.status == 400:
        print("No Problem!!")
    else:
        raise e
```

ちなみに、`dry_run`に成功した場合は、`412`のステータスコードが返ってくるようです。

# 最後に

最近のキーワードとして、自動化が注目されるようになりました。またベンチャー企業だと、突然スケールすることも見込んで、AWSを使用しているところもあるでしょう。ただ、いちいちAWSを叩くのは面倒くさいです。ですが、ありがたいことに、AWSはこのようなAPIが充実しています。以前は、インスタンスを立てることもやっていました。

このようなライブラリを使い、普段の手順をコマンド一つにしてしまうと、何かとAWS業務がはかどります。皆さんも一つ、自分の言語で試してみてはいかがでしょうか。