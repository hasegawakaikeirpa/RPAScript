import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# from sklearn import cross_validation
import sklearn.model_selection as cross_validation
from sklearn.svm import LinearSVC, SVC
import joblib
import datetime

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


def LearnJournal(csvurl, columns, Key, ind, tests):
    """
    重回帰分析
    csvurl:解析するCSVURL
    columns:抽出する列名
    Key:摘要欄列名
    ind:抽出時検索として利用する列名
    tests:予測したい文字列が入ったリスト
    """
    # Pandasデータセット
    df = pd.read_csv(csvurl, encoding="cp932")
    df = df[columns].fillna(9999999999999999)

    X = df.drop(ind, 1)  # 説明変数
    X = pd.get_dummies(X, drop_first=True)  # 説明変数

    Y = df[ind]  # 目的変数
    Y = pd.get_dummies(Y, drop_first=True)  # 説明変数

    df = pd.get_dummies(df, drop_first=True)  # ダミー変数の最初のものを除く
    # ohe = OneHotEncoder()
    # ohe.fit(df)
    # ct = ColumnTransformer([("category", ohe, [0])], remainder="passthrough")
    # cdf = ct.fit_transform(df)
    # print(cdf)
    # df = cdf
    # df = df.fillna("文字無")
    # 利用データの絞り込み

    # df_counts = df[columns].dropna()
    # df_counts.head()
    # 重回帰分析モデルを作成
    df_model = LinearRegression()
    # X = df.drop(ind, 1)  # 説明変数
    # Y = df[ind]  # 目的変数
    # X = df[:, 0]  # 説明変数
    # Y = df[:, 1:]  # 目的変数
    # 重回帰分析開始
    df_model.fit(X, Y)
    print(df_model.coef_)
    coefficient["f_names"] = pd.DataFrame(columns)
    coefficient["coefficient"] = DataFrame(linear_regression.coef_)
    # 学習結果の保存
    LearnSave(vect, clf, df_rs)


def resultSplit(result):
    print("")
    K = 3
    rs = []
    for r_r in range(len(result)):
        resRow = result[r_r, :]
        # ソートはされていない上位k件のインデックス
        # unsorted_min_indices = np.argpartition(-resRow, K)  # [:K]

        # # 上位k件の値
        # y = resRow[unsorted_max_indices]

        # 昇順
        # indices = np.argsort(-y)
        # 降順
        indices = np.argsort(resRow)

        # 類似度上位k件のインデックス
        # max_k_indices = resRow[indices]
        rs.append(indices)
    return np.array(rs)


# pddata = pd.read_csv(r"D:\OCRTESTPDF\PDFTEST\1869\xgbTest\Test.csv", encoding="cp932")
# 目的変数列名
# TargetCol = [
#     "（借）科目ｺｰﾄﾞ",
#     "（借）科目名",
#     "（借）補助ｺｰﾄﾞ",
#     "（借）補助名",
#     "（借）金額",
#     "（借）税込区分",
#     "（借）消費税ｺｰﾄﾞ",
#     "（借）消費税率",
#     "（貸）科目ｺｰﾄﾞ",
#     "（貸）科目名",
#     "（貸）補助ｺｰﾄﾞ",
#     "（貸）補助名",
#     "（貸）金額",
#     "（貸）税込区分",
#     "（貸）消費税ｺｰﾄﾞ",
#     "（貸）消費税率",
#     "摘要",
# ]

# 説明変数列名
RefCol = ["日付", "摘要", "出金", "入金", "残高", "抽出文字列", "伝票日付"]

if __name__ == "__main__":
    csvurl = r"D:\OCRTESTPDF\PDFTEST\1869\xgbTest\Anser.csv"
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
    Key = "摘要"
    ind = "行数"
    tests = ["2022/5/26", "", "18000", "APアプラス"]
    LearnJournal(csvurl, columns, Key, ind, tests)
