## 利用する変数について

### テキストラベル
|変数名|型|内容|
|:---:|:---:|:---:|
|Select_version_lavel|テキスト|`1.ソフトウェアの選択`と表示|
|Setup_folder_path_lavel|テキスト|`2.構築先フォルダを選択`と表示|

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

### 構築先パスに関する変数
関数`Select_Setup_folder_path`
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|Setup_folder_path_textbox|tkinter.Entry|テキストボックス|構築先パスを入力|
|Setup_folder_path|テキスト|なし|`Filedialog`で取得した内容の格納|
|Setup_folder_path_button|tkinter.Button|ボタン|関数`Select_Setup_folder_path`を実行|

### 実行関数に関する変数
関数`Execute`
|変数名|型|外観|内容|
|:---:|:---:|:---:|:---:|
|path|テキスト|なし|`Setup_folder_path_textbox`の内容を格納|
|URL_json|テキスト|なし|`DownloadLinks.json`からURLを格納|
|Cache_Check|Yes OR No|なし|`Cache`フォルダの上書き確認|
|plugins_path|テキスト|なし|`Plugins`フォルダのパスを格納|
|Exceute_button|tkinter.Button|ボタン|関数`Execute`を実行|


## 参考
[【Python】tkinterでファイル&フォルダパス指定画面を作成する](https://qiita.com/dgkmtu/items/2367a73f7e2d498e6075)（採録日2022年12月26日）

[【Python tkinter】Entry（エントリー）の使い方：オプション一覧（サイズ・外観）](https://office54.net/python/tkinter/python-tkinter-entry)（採録日2022年12月26日）

[TypeError: insert() missing 1 required positional argument: 'string'](https://stackoverflow.com/questions/36946334/typeerror-insert-missing-1-required-positional-argument-string)（採録日2022年12月26日

[PythonでJSON 読み込み](https://qiita.com/kikuchiTakuya/items/53990fca06fb9ba1d8a7)（採録日2022年12月27日）

[Pythonでエスケープシーケンスを無視（無効化）するraw文字列](https://note.nkmk.me/python-raw-string-escape/)（採録日2022年12月27日）

[pythonでの文字列の扱い（採録日2022年12月27日）](https://qiita.com/hiroyuki_mrp/items/1504645ab6eb1a6a4103)
