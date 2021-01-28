

filename = r'D:\prcomaintran_DSZH\Logs\Log(2021-01-28)@7777-7777.log'

fp = open(filename)
for line in fp.readlines():  # 遍历每一行
    if "错误" in line:
        print(line)

fp.close()