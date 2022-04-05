import time
from Function.utils.logging import logput as _logput
from Function.utils.logging import logging_function_decorator as _logging_function_decorator
from Function.utils.logging import DEBUG, init_logging, LOPT_NO_RETUEN_VALUES
from Function.utils.canceler import time_limit
import camelot.io as camelot
#------------------------------------------------------------------------------------------------------------------------
MYLOGGER = 'sample.time_limit'
def logput(msg, **kargs):
    return _logput(msg, logger=MYLOGGER, wrapper_depth=1, **kargs)
#------------------------------------------------------------------------------------------------------------------------
def logging_function_decorator(**kargs):
    # 返値は今回確認したい情報ではないので出力しない
    return _logging_function_decorator(logger=MYLOGGER, logput_options=LOPT_NO_RETUEN_VALUES, **kargs)
#------------------------------------------------------------------------------------------------------------------------
@logging_function_decorator(level=DEBUG)
def time_limit_example(timeout_secs=3, real_process_time_secs=0, post_process_time_secs=0, repeat_nums=1):
    with time_limit(timeout_secs) as timeout_event:
        i = 0
        while not timeout_event.wait(0):
            try:
                # 以下が本処理の想定
                time.sleep(real_process_time_secs)
            finally:
                # 以下が後処理の想定
                if post_process_time_secs > 0:
                    logput('post process start.')
                    time.sleep(post_process_time_secs)
                    logput('post process end.')

            # 一定回数繰り返したら終了
            i += 1
            if i > repeat_nums:
                break

        else:
            # ここにタイムアウト処理
            logput('timeout.')
#------------------------------------------------------------------------------------------------------------------------
@logging_function_decorator(level=DEBUG)
def PDFReadTimeOut(timeout_secs, real_process_time_secs, post_process_time_secs, repeat_nums,path_pdf,PageVol,flv):#タイムアウト時間,実行,ポストプロセス,ループ回数,ファイルパス,ページ番号,エンジン
    with time_limit(timeout_secs) as timeout_event:
        i = 0
        while not timeout_event.wait(0):
            try:
                # 以下が本処理の想定
                if flv == "stream":
                    camelot.read_pdf(path_pdf, pages=PageVol,flavor=flv)
                    time.sleep(real_process_time_secs)
                else:
                    camelot.read_pdf(path_pdf, pages=PageVol)
                    time.sleep(real_process_time_secs)                    
            finally:
                # 以下が後処理の想定
                if post_process_time_secs > 0:
                    logput('post process start.')
                    time.sleep(post_process_time_secs)
                    logput('post process end.')

            # 一定回数繰り返したら終了
            i += 1
            if i > repeat_nums:
                break

        else:
            # ここにタイムアウト処理
            logput('timeout.')
#------------------------------------------------------------------------------------------------------------------------
# if __name__ == '__main__':
#     init_logging()

#     # タイムアウトしない場合
#     time_limit_example(timeout_secs=3, real_process_time_secs=1, post_process_time_secs=0, repeat_nums=1)

#     # タイムアウトする場合
#     time_limit_example(timeout_secs=3, real_process_time_secs=1, post_process_time_secs=0, repeat_nums=10)

#     # 後処理実行中にタイムアウトが発生した場合
#     time_limit_example(timeout_secs=3, real_process_time_secs=1, post_process_time_secs=5, repeat_nums=10)