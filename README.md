# 動作環境
* Windows
    * Windows10 で制作
    * Windows10でのみ動作検証しました
    * Windows以外では正常に動作しません
* Python3.1x
    * 利用しているモジュール
        * [Tkinter](https://docs.python.org/ja/3/library/tkinter.html)
        * [OS](https://docs.python.org/ja/3/library/os.html)
        * [Subprocess](https://docs.python.org/ja/3/library/subprocess.html)
        * [JSON](https://docs.python.org/ja/3/library/json.html)
        * [glob](https://docs.python.org/ja/3/library/glob.html)
# 使い方
1.導入したいソフトウェアとバージョンを選択<br>
2.`参照`ボタンからフォルダを選択<br>
3.`実行`ボタンを押す<br>

対応しているソフトウェア
* [Aviutl.exe](http://spring-fragrance.mints.ne.jp/aviutl/)
* [拡張編集プラグイン](http://spring-fragrance.mints.ne.jp/aviutl/)
* [L-SMASH-Works rev1100](https://github.com/Mr-Ojii/L-SMASH-Works-Auto-Builds/releases)
* [x264guiEx 3.16](https://rigaya34589.blog.fc2.com/?cat=5)
* [かんたんMP4出力 2020-04-23](https://aoytsk.blog.jp/aviutl/34586383.html)
  
`DownloadLink.json`とセットで利用してください<br>
`応答なし`になっても気にしないでください

# 利用する変数について

## ウィンドウ`システムを起動する前に`

### ウィンドウ
|変数名|内容|
|:---:|:---:|
|AskAgree|利用規約|

### テキスト
|変数名|型|内容|
|:---:|:---:|:---:|
|Warning_message_title|tkinter.Label|このソフトウェアを利用するにあたって|
|Warning_message_1|tkinter.Label|以下の事項を必ずご確認ください|
|Warning_message_2|tkinter.Label|・利用するPCをインターネットに接続してください。（通信料は利用者負担）|
|Warning_message_3|tkinter.Label|・Windows10のみ動作テストを行いました。(Windows以外では正常に動作しません)|
|Warning_message_4|tkinter.Label|・Aviutlをすでに導入されているならば必ずバックアップを行ってください。|
|Warning_message_5|tkinter.Label|・いかなる損害にも製作者は責任を負いません。|
|Warning_message_6|tkinter.Label|・その他のルールは製作者のGitHubにある本プログラムのReadmeをご確認ください。|
|Warning_message_7|tkinter.Label|上記の項目を確認の上、「同意」を選択してください。|

### ボタン
|変数名|型|内容|
|:---:|:---:|:---:|
|Agree_button|tkinter.button|`main`を実行する|
|Refuse_button|tkinter.button|`Refuse`を実行しプログラム終了|

## ウィンドウ`Aviutl Auto Setup`

### ウィンドウ

|変数名|内容|
|:---:|:---:|
|root|メインウィンドウ|

### テキスト
|変数名|型|内容|
|:---:|:---:|:---:|
|Select_version_lavel|tkinter.Label|1.ソフトウェアの選択|
|Setup_folder_path_lavel|tkinter.Label|2.構築先フォルダを選択|

### Aviutl.exeの設定に関係する変数
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|Aviutl_exe_ckb|True OR False|なし|チェックが入っているときのときAviutl.exeの設定を行う|
|Aviutl_exe_checkbox|-|チェックボックス|`Aviutl_exe_ckb`を設置|
|Aviutl_exe_List|List|なし|`Aviutl_exe_Combobox`で利用する内容のリスト|
|Aviutl_exe_Combobox|Comobox|プルダウンメニュー|設定を行うバージョンを選択|


### 拡張編集プラグインに関する変数
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|Extend_Editor_ckb|True OR False|なし|チェックが入っているとき拡張編集プラグインの設定を行う|
|Extend_Editor_checkbox|-|チェックボックス|`Extend_Editor_ckb`のを設置|
|Extend_Editor_List|List|なし|`Extend_Editor_Combbox`で表示する内容のリスト|
|Extend_Editor_Combbox|Combobox|プルダウンメニュー|設定を行うバージョンを選択|

### L-SMASHに関する変数
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|LSMASH_ckb|True OR False|なし|チェックが入っているときL-SMASHの設定を行う|
|LSMASH_checkbox|-|チェックボックス|`LSMASH_ckb`を設置|
|LSMASH_List|List|なし|`LSMASH_combobox`で表示する内容のリスト|
|LSMASH_combobox|Combobox|プルダウンメニュー|設定を行うバージョンを選択|

### エンコーダーに関する変数
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|Encoder_ckb|True OR False|なし|チェックが入っているときエンコーダーの選定を行う|
|Encoder_checkbox|-|チェックボックス|`Encoder_ckb`を設置|
|Encoder_List|List|なし|`Encoder_combobox`で表示するソフトウェアのリスト|
|Encoder_combobox|Combobox|プルダウンメニュー|設定を行うソフトウェアを選択|
|BeforePath|文字列|なし|バージョン付きフォルダ名をリネームする|

### 構築先パスに関する変数
関数`Select_Setup_folder_path`
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|Setup_folder_path_textbox|tkinter.Entry|テキストボックス|構築先パスを入力|
|Setup_folder_path|文字列|なし|`Filedialog`で取得した内容の格納|
|Setup_folder_path_button|tkinter.Button|ボタン|関数`Select_Setup_folder_path`を実行|

### 実行関数に関する変数（共通）
関数`Execute`
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|ERROR|数値|なし|エラーの数を数える|
|path|文字列|なし|`Setup_folder_path_textbox`の内容を格納|
|URL_json|文字列|なし|`DownloadLinks.json`からURLを格納|
|Cache_Check|Yes OR No|なし|`Cache`フォルダの上書き確認|
|plugins_path|文字列|なし|`Plugins`フォルダのパスを格納|
|Exceute_button|tkinter.Button|ボタン|関数`Execute`を実行|

### 実行関数に関する変数（L-SMASH）
|変数名|型|内容|
|:---:|:---:|:---:|
|i|数値|ファイル探索で用いるカウンタ|

### 実行関数に関する変数（x264guiEx）
|変数名|型|内容|
|:---:|:---:|:---:|
|MiddleDir|数値|フォルダ連番<br>JSONの内容とリンクしている|
|D_StopSignal|数値|Whileループの停止条件（１で停止）<br>検索ファイルがあるディレクトリを決めるループ|
|M_StopSignal|数値|Whileループの停止条件（１で停止）<br>ファイルを検索するループ|
|SearchFile|数値|検索対象のファイル連番<br>JSONの内容とリンクしている|
|Check_MiddleDir|文字列|`MiddleDir`に対応したフォルダパスを格納|
|Check_File|文字列|`SearchFile`に対応したファイルパスを格納|

# 参考
[【Python】tkinterでファイル&フォルダパス指定画面を作成する](https://qiita.com/dgkmtu/items/2367a73f7e2d498e6075)（閲覧日2022年12月26日）

[【Python tkinter】Entry（エントリー）の使い方：オプション一覧（サイズ・外観）](https://office54.net/python/tkinter/python-tkinter-entry)（閲覧日2022年12月26日）

[TypeError: insert() missing 1 required positional argument: 'string'](https://stackoverflow.com/questions/36946334/typeerror-insert-missing-1-required-positional-argument-string)（閲覧日2022年12月26日）

[PythonでJSON 読み込み](https://qiita.com/kikuchiTakuya/items/53990fca06fb9ba1d8a7)（閲覧日2022年12月27日）

[Pythonでエスケープシーケンスを無視（無効化）するraw文字列](https://note.nkmk.me/python-raw-string-escape/)（閲覧日2022年12月27日）

[pythonでの文字列の扱い](https://qiita.com/hiroyuki_mrp/items/1504645ab6eb1a6a4103)（閲覧日2022年12月27日）

[Pythonで型の違いを意識してjson loadsを具体的に使ってみよう！](https://www.sejuku.net/blog/78985)（閲覧日2022年12月29日）

[while文を使った繰り返し](https://www.javadrive.jp/python/for/index1.html)（閲覧日2022年12月29日）

[【Python入門】os.renameでファイル名を変更する方法を解説！](https://www.sejuku.net/blog/63732)（閲覧日2022年12月29日）

[python, os.rename エラー](https://teratail.com/questions/230259)（閲覧日2022年12月29日）
