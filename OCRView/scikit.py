import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.model_selection as cross_validation
from sklearn.svm import SVC
import joblib
import datetime
import os
from functools import wraps
import time

# デコレーター---------------------------------------------------
def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__}は{elapsed_time}秒かかりました")
        return result

    return wrapper


# 関数---------------------------------------------------------
def validate(note):
    """
    文字列日付型判定
    """
    try:
        print(datetime.strptime(note, "%Y/%m/%d"))
        return True
    except ValueError:
        return False


def TypeCheck(note):
    """
    型判定
    """
    try:
        if type(note) == str:  # 文字列なら
            # 文字列日付かチェック
            if validate(note) is True:
                return "date"
            else:
                return "str"
        elif type(note) == int:  # 数値なら
            return "int"
        elif type(note) == float:  # 数値なら
            return "float"
        else:
            return "object"
    except ValueError:
        return "false"


def WordAct(t, note, notes_row, TC):
    """
    テキスト処理
    """
    if TC == "date":  # 日付型なら
        # 日のみ抽出
        d_day = datetime.strptime(note, "%Y/%m/%d").day
        notes_row.append(d_day)
    elif TC == "str":  # 日付型なら:  # 文字列なら
        tokens = t.tokenize(note.replace("　", " "))
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes_row.append(words.replace(" \u3000", ""))
    else:  # 日付型なら:  # 文字列なら
        notes_row.append(note)


# 機械学習関数-----------------------------------------------------
# https://qiita.com/nightbaroque/items/ece42003efeefa322a0d
def dirserch(filename):
    """
    フォルダ存在✓
    """
    dir_path = os.path.dirname(filename)
    dir_path = dir_path + r"\scikit_data"
    if os.path.isdir(dir_path) is False:
        os.mkdir(dir_path)
        return dir_path
    else:
        return dir_path


def LearnSave(vect, clf, df_rs):
    """
    学習データの保存
    """
    dir_path = dirserch()
    joblib.dump(vect, dir_path + r"/vect.pkl")
    joblib.dump(clf, dir_path + r"/clf.pkl")
    df_rs.to_csv(dir_path + r"/code.csv")


def LearnLoad():
    """
    学習データの読込
    """
    dir_path = dirserch()
    filename = dir_path + r"/code.csv"
    df = pd.read_csv(filename, header=None)
    df.index = df.pop(0)
    df_rs = df.pop(1)
    clf = joblib.load(dir_path + r"/clf.pkl")
    vect = joblib.load(dir_path + r"/vect.pkl")


def LearnPrediction(vect, clf, df_rs):
    """
    予測
    """
    t = Tokenizer()
    tests = [
        "高速道路利用料",
        "パソコン部品代",
        "切手代",
    ]

    notes = []
    for note in tests:
        tokens = t.tokenize(note)
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words)

    X = vect.transform(notes)

    result = clf.predict(X)

    for i in range(len(tests)):
        print(tests[i], "\t[", df_rs.loc[result[i]], "]")


def CreateIndice(y, y_train):
    Ind = [np.where(y == y_item)[0] for y_item in y_train]
    Ind = np.array(Ind)
    return Ind
    # for y_item in y_train:
    #     ans = np.where(y == y_item)
    #     Ind.append()


# @stop_watch
# def Test(df_counts, Key, notes, t):
#     for note in df_counts[Key]:
#         tokens = t.tokenize(note.replace("　", " "))
#         words = ""
#         for token in tokens:
#             words += " " + token.surface
#         notes.append(words.replace(" \u3000", ""))


# @stop_watch
# def Test2(df_counts, Key, notes, t):
#     for ix in df_counts.index:
#         df_c_loc = df_counts.iloc[ix]
#         note = df_c_loc[Key]
#         tokens = t.tokenize(note.replace("　", " "))
#         words = ""
#         for token in tokens:
#             words += " " + token.surface
#         notes.append(words.replace(" \u3000", ""))


@stop_watch
###############################################################################
def LearnJournal(df, columns, Key, ind, tests):
    """
    単回帰分析
    csvurl:解析するCSVURL
    columns:抽出する列名
    Key:摘要欄列名
    ind:抽出時検索として利用する列名
    tests:予測したい文字列が入ったリスト
    """
    # モデル作成################################################################
    # Pandasデータセット
    df = df.fillna("文字無")
    # nan削除
    df_counts = df[columns].dropna()
    # 形態素解析
    t = Tokenizer()
    # 対象文字列の整理
    notes = []
    # 摘要欄列の文字列形態素解析処理
    for note in df_counts[Key]:
        tokens = t.tokenize(note.replace("　", " "))
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words.replace(" \u3000", ""))

    df_counts[Key] = notes

    # 文字列をベクトル化
    vect = TfidfVectorizer()
    vect.fit(notes)

    X = vect.transform(notes)
    # print(pd.DataFrame(X.toarray(), columns=vect.get_feature_names()))

    # 教師データとして行数を使用
    y = df_counts[ind].values.astype("int").flatten()

    # 機械学習
    test_size = 0.2
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        X, y, test_size=test_size, shuffle=False
    )

    # モデルとしてLinearSVCを使用
    clf = SVC(kernel="linear", probability=True)
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)
    # 予測####################################################################
    # 入力文字列形態素解析処理
    notes = []
    for note in tests:
        tokens = t.tokenize(note)
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words)

    X = vect.transform(notes)
    X_trainDF = np.array(df_counts)
    # インダイス取得
    y_ind = CreateIndice(y, y_train)
    X_trainDF = X_trainDF[y_ind, :]
    # モデルから予想
    result = clf.predict_proba(X)
    # 予想結果をインダイスに変換
    result = resultSplit(result)
    # データ整理用のDF作成-----------------------------------
    df_rs = df_counts[columns]
    df_rs.index = df_counts[ind].astype("int")
    df_rs = df_rs[~df_rs.index.duplicated()][columns]
    # ------------------------------------------------------
    New_df = []  # 新DF
    for i in range(len(tests)):

        for res_c in range(len(result[i])):

            if res_c <= 5:
                # 上位5位まで表示
                df_rs_loc = df_rs.iloc[result[i][res_c]]
                l_words = ""

                New_df_row = []  # 新DF格納用行
                New_df_row.append(tests[i])

                for c in range(len(df_rs_loc)):
                    # 抽出文字列
                    Instr = str(df_rs_loc[c])
                    if Instr == "文字無":
                        Instr = ""

                    New_df_row.append(Instr)
                    l_words += "," + Instr
                    if l_words[0] == ",":
                        l_words = l_words[1:]

                New_df.append(New_df_row)
                print(tests[i], "\t[", l_words, "]")
        # New_df = pd.DataFrame(New_df, columns=columns)
    return New_df


###############################################################################
def resultSplit(result):
    rs = []
    for r_r in range(len(result)):
        resRow = result[r_r, :]
        # 昇順
        indices = np.argsort(resRow)
        # 類似度上位k件のインデックス
        rs.append(indices)
    return np.array(rs)


def main(model_df, li, Key, ind):
    """
    呼出関数
    model_df:学習モデル(ミロク元帳)
    li:リスト化されたOCR抽出結果摘要列
    Key:学習モデルの説明変数となる列名(検索条件)
    ind:学習モデルの目標変数となる列名(結果)
    """
    try:
        print(list(model_df[ind]))
    except:
        Ind_col = [r for r in range(len(model_df))]
        model_df.insert(0, "行数", Ind_col, True)
    LJ = LearnJournal(model_df, list(model_df.columns), Key, ind, li)
    return LJ


if __name__ == "__main__":
    ###########################################################################
    csvurl = r"D:\OCRTESTPDF\PDFTEST\1869\xgbTest\Anser.csv"
    # 目的変数列名
    columns = [
        "行数",
        "伝票日付",
        "（借）科目ｺｰﾄﾞ",
        "（借）科目名",
        "（借）補助ｺｰﾄﾞ",
        "（借）補助名",
        "（借）金額",
        "（借）税込区分",
        "（借）消費税ｺｰﾄﾞ",
        "（借）消費税率",
        "（貸）科目ｺｰﾄﾞ",
        "（貸）科目名",
        "（貸）補助ｺｰﾄﾞ",
        "（貸）補助名",
        "（貸）金額",
        "（貸）税込区分",
        "（貸）消費税ｺｰﾄﾞ",
        "（貸）消費税率",
        "摘要",
    ]
    # 説明変数列名
    RefCol = ["日付", "摘要", "出金", "入金", "残高", "抽出文字列", "伝票日付"]
    Key = "摘要"
    ind = "行数"
    tests = ["APアプラス", "三菱HBL", "長谷川会計"]
    days = ["2022/4/25", "2022/4/27", "2022/4/27"]
    moneys = ["18000", "24000", "20000"]
    ###########################################################################
    LearnLoad()  # 学習データの検索
    df = pd.read_csv(csvurl, encoding="cp932")
    LJ = LearnJournal(df, columns, Key, ind, tests)
    ###########################################################################

    # Key = "伝票日付"
    # ind = "行数"
    # LJ = LearnJournalDays(LJ, columns, Key, ind, days)
