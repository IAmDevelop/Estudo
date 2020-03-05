def ConectarSQLServer(username, password):
    try:
        import pyodbc
        server = 'DESKTOP-UN8230O\SQLSERVERMY'
        driver = '{SQL Server}'
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                              ';DATABASE=Impacta;UID='+username +
                              ';PWD='+password+';')
        cursor = cnxn.cursor()
        cursor.execute(
            'select nome, usuario from Impacta.dbo.Usuarios')
        for row in cursor:
            print(row)
    except ConnectionError:
        print("Erro")


def ConectarMySQL(username, senha):
    try:
        import MySQLdb
        conn = MySQLdb.Connect(host='185.201.10.73',
                               user=username, passwd=senha, db='u355583042_MyStudio')
        cursor = conn.cursor()
        cursor.execute("select * from Login")
        for row in cursor:
            print(row)
    except ConnectionError:
        print("Erro")


def ConectarMySQL2(username, senha):
    import mysql.connector
    try:
        connection = mysql.connector.connect(
            host='185.201.10.73', database='u355583042_MyStudio', user=username, password=senha)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select * from Login")
            for row in cursor:
                print(row)
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except ConnectionError as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
