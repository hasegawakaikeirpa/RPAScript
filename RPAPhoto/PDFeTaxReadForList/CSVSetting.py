# ------------------------------------------------------------------------------------
eTaxSyotkuList = []  # eTax源泉所得税及復興特別所得税
eTaxSyotku2List = []  # eTax源泉所得税及復興特別所得税2
eTaxSyouhiList = []  # eTax消費税中間申告用
MJSSyotkuList = []  # MJS所得税
MJSSyotku2List = []  # MJS所得税2
MJSSyouhiList = []  # MJS消費税
MJSSyouhi2List = []  # MJS消費税2
# 関数の引数様にDict格納-------------------------------------------------------------------------
CSVIndexSortFuncArray = {
    "eTax源泉所得税及復興特別所得税": eTaxSyotkuList,
    "eTax源泉所得税及復興特別所得税2": eTaxSyotku2List,
    "eTax消費税中間申告用": eTaxSyouhiList,
    "MJS所得税": MJSSyotkuList,
    "MJS所得税2": MJSSyotku2List,
    "MJS消費税": MJSSyouhiList,
    "MJS消費税2": MJSSyouhi2List,
}
