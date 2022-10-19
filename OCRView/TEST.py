import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer

# from sklearn import cross_validation
import sklearn.model_selection as cross_validation
from sklearn.svm import LinearSVC, SVC
import joblib
import datetime
from sklearn.linear_model import LinearRegression

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
def LearnSave(vect, clf, df_rs):
    """
    学習データの保存
    """
    joblib.dump(vect, "./data/vect.pkl")
    joblib.dump(clf, "./data/clf.pkl")
    df_rs.to_csv("./data/code.csv")


def LearnLoad():
    """
    学習データの読込
    """
    filename = "./data/code.csv"
    df = pd.read_csv(filename, header=None)
    df.index = df.pop(0)
    df_rs = df.pop(1)
    clf = joblib.load("./data/clf.pkl")
    vect = joblib.load("./data/vect.pkl")


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
    # Pandasデータセット
    df = df.fillna("文字無")
    # 利用データの絞り込み

    df_counts = df[columns].dropna()

    # 形態素解析
    t = Tokenizer()

    notes = []
    for ix in df_counts.index:
        df_c_loc = df_counts.iloc[ix]
        note = df_c_loc[Key]
        tokens = t.tokenize(note.replace("　", " "))
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words.replace(" \u3000", ""))

    # 文字列をベクトル化
    vect = TfidfVectorizer()
    vect.fit(notes)

    X = vect.transform(notes)

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

    # 予測
    notes = []
    for note in tests:
        tokens = t.tokenize(note)
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words)

    X = vect.transform(notes)
    X_trainDF = np.array(df)
    X_trainDF = X_trainDF[y_train, :]

    result = clf.predict_proba(X)
    df_rs = df_counts[columns]

    result = resultSplit(result)

    df_rs.index = df_counts[ind].astype("int")
    df_rs = df_rs[~df_rs.index.duplicated()][columns]
    New_df = []  # 新DF
    for i in range(len(tests)):
        for res_c in range(len(result[i])):
            if res_c <= 5:
                # 上位5位まで表示
                df_rs_loc = df_rs.iloc[result[i][res_c]]
                l_words = ""
                New_df_row = []  # 新DF格納用行
                for c in range(len(df_rs_loc)):
                    New_df_row.append(str(df_rs_loc[c]))
                    l_words += "," + str(df_rs_loc[c])
                    if l_words[0] == ",":
                        l_words = l_words[1:]
                New_df.append(New_df_row)
                print(tests[i], "\t[", l_words, "]")
        New_df = pd.DataFrame(New_df, columns=columns)
    return New_df


###############################################################################
def LearnJournalDays(df, columns, Key, ind, tests):
    """
    単回帰分析
    csvurl:解析するCSVURL
    columns:抽出する列名
    Key:摘要欄列名
    ind:抽出時検索として利用する列名
    tests:予測したい文字列が入ったリスト
    """
    # Pandasデータセット
    df = df.fillna("文字無")
    # 利用データの絞り込み

    df_counts = df[columns].dropna()

    # 形態素解析
    t = Tokenizer()

    notes = []
    for ix in df_counts.index:
        df_c_loc = df_counts.iloc[ix]
        note = df_c_loc[Key]
        tokens = t.tokenize(note.replace("　", " "))
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words.replace(" \u3000", ""))

    # 文字列をベクトル化
    vect = TfidfVectorizer()
    vect.fit(notes)

    X = vect.transform(notes)

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

    # 予測
    notes = []
    for note in tests:
        tokens = t.tokenize(note)
        words = ""
        for token in tokens:
            words += " " + token.surface
        notes.append(words)

    X = vect.transform(notes)
    X_trainDF = np.array(df)
    X_trainDF = X_trainDF[y_train, :]

    result = clf.predict_proba(X)
    df_rs = df_counts[columns]

    result = resultSplit(result)

    df_rs.index = df_counts[ind].astype("int")
    df_rs = df_rs[~df_rs.index.duplicated()][columns]
    New_df = []  # 新DF
    for i in range(len(tests)):
        for res_c in range(len(result[i])):
            if res_c <= 5:
                # 上位5位まで表示
                df_rs_loc = df_rs.iloc[result[i][res_c]]
                l_words = ""
                New_df_row = []  # 新DF格納用行
                for c in range(len(df_rs_loc)):
                    New_df_row.append(str(df_rs_loc[c]))
                    l_words += "," + str(df_rs_loc[c])
                    if l_words[0] == ",":
                        l_words = l_words[1:]
                New_df.append(New_df_row)
                print(tests[i], "\t[", l_words, "]")
        New_df = pd.DataFrame(New_df, columns=columns)


###############################################################################


def resultSplit(result):
    K = 3
    rs = []
    for r_r in range(len(result)):
        resRow = result[r_r, :]
        # 昇順
        indices = np.argsort(resRow)
        # 類似度上位k件のインデックス
        rs.append(indices)
    return np.array(rs)


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
    df = pd.read_csv(csvurl, encoding="cp932")
    LJ = LearnJournal(df, columns, Key, ind, tests)
    ###########################################################################
    Key = "伝票日付"
    ind = "行数"
    LJ = LearnJournal(LJ, columns, Key, ind, days)
