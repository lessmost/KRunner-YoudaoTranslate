import urllib
import json


class YDTranslate:
    def __init__(self, apikey, keyfrom):
        self.apikey = apikey
        self.keyfrom = keyfrom

    def request(self, query):
        params = {
            "keyfrom": self.keyfrom,
            "key": self.apikey,
            "type": "data",
            "doctype": "json",
            "version": "1.1",
            "q": query.toUtf8()
        }
        f = urllib.urlopen("http://fanyi.youdao.com/openapi.do?%s" %
                           urllib.urlencode(params))
        return f.read()

    def translate(self, query):
        res = self.request(query)
        obj = json.loads(res)

        if not obj['errorCode'] == 0:
            # check erroCode
            return ""

        explains = obj['basic']['explains']
        ret = "\n".join(explains)
        return ret

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        t = YDTranslate("456472771", "zqlu-github-io")
        print t.translate(sys.argv[1])
