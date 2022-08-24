# TKINTERCV2Setting

* [機能](#機能)
* [利用ライブラリ](#利用ライブラリ)
* [モジュール関数](#モジュール関数)

# 機能
#### OCR読取ウィンドウ
#### 軸設定や、出力列・変換対象列の設定
<br>

# 利用ライブラリ

#### import tkinter as tk
#### ・Gui作成ライブラリ
<br>

#### import csv
#### ・CSVファイル操作ライブラリ
<br>

#### from PIL import Image, ImageTk
#### ・画像編集ライブラリ
<br>

#### from tkinter import messagebox
#### ・Gui作成ライブラリメッセージボックス
<br>

#### import os
#### ・ファイル・フォルダ操作ライブラリ
<br>

#### import OCRFlow as OCRF
#### ・OCR抽出後の配列操作ライブラリ
<br>

#### import toml
#### ・tomlファイル操作ライブラリ
<br>

#### from tkinter import ttk
#### ・Gui作成ライブラリ(後継版)
<br>

#### import CV2Setting as CV2S
#### ・OCR抽出準備ライブラリ
<br>

#### import DataGrid as DG
#### ・自動仕訳ウィンドウライブラリ
<br>

#### import ScrollableFrame as SF
#### ・ScrollableFrame作成ライブラリ
<br>

# モジュール関数
* [Main](#Main)
#### Main
    Main(MUI, US)
    MUI = 全画面のインスタンス
    US = 対象画像のURL