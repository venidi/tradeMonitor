import pymssql


def conn():
    connect = pymssql.connect('192.168.16.41', 'sa', 'sczqtest', 'hswinrun2')  # 服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    return connect


if __name__ == '__main__':
    conn = conn()
