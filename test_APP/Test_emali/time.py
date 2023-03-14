import http.client
import time


def get_webserver_datetime(website):
    try:
        conn = http.client.HTTPConnection(website)
        conn.request("GET", "/")
        # 获取响应
        rsp = conn.getresponse()
        # 获取http头date部分
        timestamp = rsp.getheader('date')

        # 将GMT时间转换成北京时间
        ltime = time.strptime(timestamp[5:25], "%d %b %Y %H:%M:%S")
        bjtime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)

        # date = "%u-%02u-%02u" % (bjtime.tm_year, bjtime.tm_mon, bjtime.tm_mday)
        date = "%02u-%02u" % (bjtime.tm_mon, bjtime.tm_mday)

        tm = "%02u_%02u_%02u" % (bjtime.tm_hour, bjtime.tm_min, bjtime.tm_sec)
        dt = date + "_" + tm
        rrr = 'D:/zhaoyu/Test_pythonProject/test_APP/reports/2023-'
        f = rrr + dt + '.report.html'
        h = rrr + dt + '.report.html'
        return f
    except:
        return None



if __name__ == '__main__':
    get_webserver_datetime('www.baidu.com')
    print(get_webserver_datetime('www.baidu.com'))