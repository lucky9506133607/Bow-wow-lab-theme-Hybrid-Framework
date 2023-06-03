import openpyxl

import mysql.connector
from utilities.customLogger import LogGen

def readData(db_name, query):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=3306,
        database=db_name
    )
    logger = LogGen.loggen()
    logger.info("******* readdata function started **********")
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute(query)
    table_data = mycursor.fetchall()
    table_date_1 = ["ls2170184@gmail.com"]
     # Logger
    logger.info("******* readdata function working **********")
    mycursor.close()
    mydb.close()

    return table_data

#getdata = readData('bowwowlabdb', "select * from customers where email = 'ls2170184@gmail.com'")







