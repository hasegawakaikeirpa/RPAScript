# TKInterGUI

* [フォルダ構成](#フォルダ構成)
* [機能](#機能)

## フォルダ構成

#### ウィンドウ

* [ViewGUI.py(開始ウィンドウ)](#ViewGUI.py(開始ウィンドウ))
* [TKINTERCV2Setting.py(OCR読取ウィンドウ)](#TKINTERCV2Setting.py(OCR読取ウィンドウ))(#TKINTERCV2Setting.py)
* DataGrid.py(読取後仕訳表示ウィンドウ)

#### ウィンドウ補助

* ControlGUI.py(ViewGUI.pyサブ)
* ModelImage.py(ViewGUI.pyサブ)
* *CSVOut.py(DataGrid.pyサブ)
* OCRFlow.py(TKINTERCV2Setting.pyサブ)
*  Frame
    * DGFrame.py(DataGrid.pyサブ)
    * MyTable.py(DataGrid.pyサブ)
    * __pycache(pyファイルキャッシュ)__

#### 関数
* AutoJournal copy.py(自動変換スクリプト)
* AutoJournal.py(自動変換スクリプト)
* GCloudVision.py(GoogleVisionApiスクリプト)
* ImageChange.py(画像編集スクリプト)
* ScrollableFrame.py(Scバーフレーム作成スクリプト)
* WarekiHenkan.py(和暦変換スクリプト)
* TKEntry.py(エントリー作成スクリプト)

#### その他

* __pycache(pyファイルキャッシュ)__
* Mototyou(元帳保存ディレクトリ)
* BankSetting.toml(設定ファイル)
* cmapchange.csv(エンコード表)
* EventCheck.py(開発時のHandlerテストコード)
* ReadMe.md(このMarkdown)
* StraightListTate.csv(OCR解析時の縦軸リスト)
* StraightListYoko.csv(OCR解析時の横軸リスト)

## 機能

#### GoogleVisionApiを用いたOCR読取・自動仕訳作成機能
#### OCR対象画像に対し、縦・横の直線を挿入し、表形式としてOCR読取を実行。
#### その後、該当関与先の仕訳実績(ミロク元帳)から、指定の列のテキストを比較し、
#### 一致率の最も高い仕訳を抽出し、自動で仕訳インポートファイルを作成。
<br>

## ViewGUI.py(開始ウィンドウ)

## TKINTERCV2Setting.py(OCR読取ウィンドウ)

### ・使用モジュール
#### from appium import webdriver : Appium-Python-Client==1.3.0
#### <補足>RPAライブラリ：クラス要素へのアクション
<br>

#### import subprocess : Python3.7.8
#### <補足>組込関数：プログラム起動
<br>

#### import pyautogui as pg : PyAutoGUI==0.9.53
#### <補足>RPAライブラリ：画像要素へのアクション,キー・マウスアクション等
<br>

#### import time : Python3.7.8
#### <補足>組込関数：待機処理
<br>

#### import os : Python3.7.8
#### <補足>組込関数：ファイルチェック・作成,フォルダチェック・作成
<br>

### ・各スクリプト

#### MainFlow(BatUrl, FolURL2, ImgFolName)
#### <機能>メイン処理
#### <引数1>BatUrl：elTax(PCDESKWEB版)のURL(str)
#### <引数2>FolURL2 ：保存場所の親ディレクトリ(str)
#### <引数3>ImgFolName：未定

