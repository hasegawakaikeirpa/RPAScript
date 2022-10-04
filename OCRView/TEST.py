Replist = [
    ",",
    "*",
    "'",
    "○",
    "×",
    "✓",
    "¥",
    "´",
    "=",
    "串",
    "第",
    "$",
    "〒",
    ".",
    "|",
    "-",
    "･",
    "!",
]

s = ""

Check = [True if s == i else False for i in Replist]
if True not in Check:
    print(True in Check)
