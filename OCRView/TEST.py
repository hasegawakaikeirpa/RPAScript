from functools import wraps
import traceback


def Err_Check(*args, **kwargs):
    def _my_decorator(func):
        # _my_decorator_body() を定義する前に必要な処理があれば、ここに書く
        @wraps(func)
        def _my_decorator_body(*body_args, **body_kwargs):
            # 前処理はここで実行
            try:
                # デコレートした本体の実行
                ret = func(*body_args, **body_kwargs)
            except Exception as e:
                tp = traceback.print_exc()
                print("")
                raise
            # 後処理はここで実行
            return ret

        # デコレータが記載された時に処理が必要な場合にはここに書く #2
        return _my_decorator_body

    # デコレータが記載された時に処理が必要な場合にはここに書く #1

    if len(args) == 1 and callable(args[0]):
        # 引数無しでデコレータが呼ばれた場合はここで処理
        return _my_decorator(args[0])

    else:
        # 引数ありでデコレータが呼ばれた場合はここで処理
        return _my_decorator


@Err_Check
def main():
    win = tk.Tk()
    app = Application(win)
    app.mainloop()


if __name__ == "__main__":
    main()
