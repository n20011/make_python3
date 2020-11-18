import itertools as it
import json

import requests as req


def message1():
    return """
              << COVID19-Japan>>
    ・COVID19について正確な数を知ることができます。
    ・こちらの情報は2時間ごとに更新されます。
    ・都道府県を[nunber]の[0~46]から選んでEnterを押してください。
    　[nunber]
      [ 0 ]-北海道
      [ 1 ]-青森県　[ 2 ]-岩手県　[ 3 ]-宮城県　[ 4 ]-秋田県
      [ 5 ]-山形県　[ 6 ]-福島県
      [ 7 ]-茨城県　[ 8 ]-栃木県　[ 9 ]-群馬県　[ 10 ]-埼玉県
      [ 11 ]-千葉県　[ 12 ]-東京都　[ 13 ]-神奈川県
      [ 14 ]-新潟県　[ 15 ]-富山県　[ 16 ]-石川県　[ 17 ]-福井県
      [ 18 ]-山梨県　[ 19 ]-長野県　[ 20 ]-岐阜県　[ 21 ]-静岡県
      [ 22 ]-愛知県
      [ 23 ]-三重県　[ 24 ]-滋賀県　[ 25 ]-京都府　[ 26 ]-大阪府
      [ 27 ]-兵庫県　[ 28 ]-奈良県　[ 29 ]-和歌山県
      [ 30 ]-鳥取県　[ 31 ]-島根県　[ 32 ]-岡山県　[ 33 ]-広島県
      [ 34 ]-山口県
      [ 35 ]-徳島県　[ 36 ]-香川県　[ 37 ]-愛媛県　[ 38 ]-高知県
      [ 39 ]-福岡県　[ 40 ]-佐賀県　[ 41 ]-長崎県　[ 42 ]-熊本県
      [ 43 ]-大分県　[ 44 ]-宮城県　[ 45 ]-鹿児島県　[ 46 ]-沖縄県
      入力先　==> """


def message2():
    return """
    ・知りたい情報をkeywordの[0~5]から番号で選びEnterを押してください。
    　[keyword]
      [ 0 ]  => 現在のコロナ合計感染者数を検索できます。
      [ 1 ]  => 現在のコロナによる合計死者数を検索できます。
      [ 2 ]  => 現在のpcr検査を受けた合計者数を検索できます。
      [ 3 ]  => 現在のコロナによる合計入院人数を検索できます。
      [ 4 ]  => 現在の合計退院人数を検索できます。
      [ 5 ]  => 2時間内で病状が確認された人数を検索します。
      入力先　==> """


def message3():
    return """
    ・続ける場合は [はい]＝ y
    　アプリを終了する場合は [いいえ]= n
    　を入力して[Enter]を押してください。
    　入力先　==> """


def dateinput(nunber, indate):
    uri = "https://covid19-japan-web-api.now.sh/api//v1/prefectures"
    res = req.get(uri)
    txdate = json.loads(res.text)
    keyword = {
        0: "cases",
        1: "deaths",
        2: "pcr",
        3: "hospitalize",
        4: "discharge",
        5: "symptom_confirming",
    }
    return f"    ・現在は{txdate[nunber][keyword[indate]]}人です。"


def yes_no():
    answer = input(message3())
    if "y" == answer:
        return True
    return False


for _ in it.count(0):
    nunber = int(input(message1()))
    indate = int(input(message2()))
    if nunber > 46 or indate > 5:
        print("    エラーが発生しました。再度入力してください。")
        continue
    print(dateinput(nunber, indate))
    if not yes_no():
        break

print("    外出を控えましょう。アプリを終了します。")