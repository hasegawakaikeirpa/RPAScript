import tomli, tomli_w


def create_toml_sample(self, path: str):
    """
    tomlファイルを作成する
    出力内容を辞書でロジックに定義
    """
    toml_data = {}
    toml_data["DEFINITION"] = {
        "セクション1": {
            "key1": ["key1の説明", "bool"],
            "key2": ["key2の説明", "str"],
            "key3": ["key3の説明", "int"],
        },
        "セクション2": {
            "key4": ["key4の説明", "bool"],
            "key5": ["key5の説明", "str"],
            "key6": ["key6の説明", "str"],
        },
        "セクション3": {"key7": ["key7の説明", "bool"], "key8": ["key8の説明", "str"]},
    }
    toml_data["DEFAULT"] = {
        "セクション1": {"key1": True, "key2": "文字列2", "key3": 800},
        "セクション2": {"key4": False, "key5": "文字列5", "key6": "文字列6"},
        "セクション3": {"key7": True, "key8": "文字列8"},
    }
    toml_data["USER"] = {
        "セクション1": {"key1": True, "key2": "文字列2", "key3": 800},
        "セクション2": {"key4": False, "key5": "文字列5", "key6": "文字列6"},
        "セクション3": {"key7": True, "key8": "文字列8"},
    }

    self.tomlu.dump_toml(toml_data, path)


def dump_toml(self, toml_dict: dict, path: str):
    """
    tomlで読み込んだ辞書をtomlファイルに出力する
    Args:
        dict:   tomlで読み込んだ辞書
        str:    保存先ファイル名
    """
    try:
        with open(path, "wb") as configfile:
            tomli_w.dump(toml_dict, configfile)
    except exception as e:
        print(e)
