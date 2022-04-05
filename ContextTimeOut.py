from threading import Thread
import functools
import camelot.io as camelot

def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print ('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

@timeout(10)
def camelotTimeOut(URL,Page,flv):
    if flv == 'stream':
        CRP = camelot.read_pdf(URL, pages=Page,flavor=flv)
        return CRP
    else:
        CRP = camelot.read_pdf(URL, pages=Page)
        return CRP

# try:
#     pg = camelotTimeOut('//Sv05121a/e/電子ファイル/メッセージボックス/TEST/1011/ミロク送信分/1011_西村 英亨.pdf', '1','stream')
#     PDFdf = pg[0].df# PDFテーブルをdf化
#     print(PDFdf)
# except:#TimeOut処理を記述
#     pass