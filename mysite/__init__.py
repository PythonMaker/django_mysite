import pymysql

pymysql.version_info = (1, 3, 13, "final", 0)  # 修改版本号来欺骗 django
pymysql.install_as_MySQLdb()  # 使用 pymysql 驱动来代替官方的 mysqlclient
