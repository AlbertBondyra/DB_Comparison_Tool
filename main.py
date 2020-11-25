import sys
import cx_Oracle
from PyQt5 import Qt

import config
import properties_conn_queries
import pymysql
import timer
import os
import mysql.connector
import pyodbc
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QMessageBox, QDialog, QVBoxLayout)
from PyQt5.QtGui import QIcon

class WindowMSSQL(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MSSQL")
        self.setWindowIcon(QIcon('C:\\Users\\alber\\Downloads\\mssql_icon.png'))
        self.setFixedSize(480, 480)

        # runquery1
        self.MSSQLbuttonRunQuery1 = QPushButton('RUN QUERY 1', self)
        self.MSSQLbuttonRunQuery1.setGeometry(10, 25, 200, 50)
        self.MSSQLbuttonRunQuery1.setToolTip(properties_conn_queries.sql1MSSQL)
        self.MSSQLbuttonRunQuery1.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.MSSQLbuttonRunQuery1.clicked.connect(lambda: timer.setEnabled(self.MSSQLbuttonRunQuery1))
        self.MSSQLbuttonRunQuery1.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql1MSSQL, properties_conn_queries.curMSSQL, order=1))

        # runquery2
        self.MSSQLbuttonRunQuery2 = QPushButton('RUN QUERY 2', self)
        self.MSSQLbuttonRunQuery2.setToolTip(properties_conn_queries.sql2MSSQL)
        self.MSSQLbuttonRunQuery2.setGeometry(10, 100, 200, 50)
        self.MSSQLbuttonRunQuery2.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.MSSQLbuttonRunQuery2.clicked.connect(lambda: timer.setEnabled(self.MSSQLbuttonRunQuery2))
        self.MSSQLbuttonRunQuery2.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql2MSSQL, properties_conn_queries.curMSSQL, order=2))


        # runquery3
        self.MSSQLbuttonRunQuery3 = QPushButton('RUN QUERY 3', self)
        self.MSSQLbuttonRunQuery3.setToolTip(properties_conn_queries.sql3MSSQL)
        self.MSSQLbuttonRunQuery3.setGeometry(10, 175, 200, 50)
        self.MSSQLbuttonRunQuery3.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.MSSQLbuttonRunQuery3.clicked.connect(lambda: timer.setEnabled(self.MSSQLbuttonRunQuery3))
        self.MSSQLbuttonRunQuery3.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql3MSSQL, properties_conn_queries.curMSSQL, order=3))

        # runquery4
        self.MSSQLbuttonRunQuery4 = QPushButton('RUN QUERY 4', self)
        self.MSSQLbuttonRunQuery4.setToolTip(properties_conn_queries.sql4MSSQL)
        self.MSSQLbuttonRunQuery4.setGeometry(250, 25, 200, 50)
        self.MSSQLbuttonRunQuery4.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.MSSQLbuttonRunQuery4.clicked.connect(lambda: timer.setEnabled(self.MSSQLbuttonRunQuery4))
        self.MSSQLbuttonRunQuery4.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql4MSSQL, properties_conn_queries.curMSSQL, order=4))

        # runquery5
        self.MSSQLbuttonRunQuery5 = QPushButton('RUN QUERY 5', self)
        self.MSSQLbuttonRunQuery5.setToolTip(properties_conn_queries.sql5MSSQL)
        self.MSSQLbuttonRunQuery5.setGeometry(250, 100, 200, 50)
        self.MSSQLbuttonRunQuery5.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.MSSQLbuttonRunQuery5.clicked.connect(lambda: timer.setEnabled(self.MSSQLbuttonRunQuery5))
        self.MSSQLbuttonRunQuery5.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql5MSSQL, properties_conn_queries.curMSSQL, order=5))


        # runquery6
        self.MSSQLbuttonRunQuery6 = QPushButton('RUN QUERY 6', self)
        self.MSSQLbuttonRunQuery6.setToolTip(properties_conn_queries.sql6MSSQL)
        self.MSSQLbuttonRunQuery6.setGeometry(250, 175, 200, 50)
        self.MSSQLbuttonRunQuery6.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.MSSQLbuttonRunQuery6.clicked.connect(lambda: timer.setEnabled(self.MSSQLbuttonRunQuery6))
        self.MSSQLbuttonRunQuery6.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql6MSSQL, properties_conn_queries.curMSSQL, order=6))


        # reset_button
        self.ResetButton = QPushButton('RESET', self)
        self.ResetButton.setToolTip("Reset all buttons and content of file")
        self.ResetButton.setGeometry(250, 400, 200, 50)
        self.ResetButton.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MSSQLbuttonRunQuery1))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MSSQLbuttonRunQuery2))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MSSQLbuttonRunQuery3))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MSSQLbuttonRunQuery4))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MSSQLbuttonRunQuery5))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MSSQLbuttonRunQuery6))
class WindowMySQL(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MySQL")
        self.setWindowIcon(QIcon('C:\\Users\\alber\\Downloads\\mysql_icon.png'))
        self.setFixedSize(480, 480)
        # runquery1
        self.MySQLbuttonRunQuery1 = QPushButton('RUN QUERY 1', self)
        self.MySQLbuttonRunQuery1.setGeometry(10, 25, 200, 50)
        self.MySQLbuttonRunQuery1.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")

        self.MySQLbuttonRunQuery1.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql1MySQL, properties_conn_queries.curMySQL, order=1))
        self.MySQLbuttonRunQuery1.clicked.connect(lambda: timer.setEnabled(self.MySQLbuttonRunQuery1))
        self.MySQLbuttonRunQuery1.setToolTip(properties_conn_queries.sql1MySQL)

        self.MySQLbuttonRunQuery2 = QPushButton('RUN QUERY 2', self)
        self.MySQLbuttonRunQuery2.setGeometry(10, 100, 200, 50)
        self.MySQLbuttonRunQuery2.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.MySQLbuttonRunQuery2.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql2MySQL, properties_conn_queries.curMySQL, order=2))
        self.MySQLbuttonRunQuery2.clicked.connect(lambda: timer.setEnabled(self.MySQLbuttonRunQuery2))
        self.MySQLbuttonRunQuery2.setToolTip(properties_conn_queries.sql1MySQL)
        # runquery3
        self.MySQLbuttonRunQuery3 = QPushButton('RUN QUERY 3', self)
        self.MySQLbuttonRunQuery3.setGeometry(10, 175, 200, 50)
        self.MySQLbuttonRunQuery3.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.MySQLbuttonRunQuery3.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql3MySQL, properties_conn_queries.curMySQL, order=3))
        self.MySQLbuttonRunQuery3.clicked.connect(lambda: timer.setEnabled(self.MySQLbuttonRunQuery3))
        self.MySQLbuttonRunQuery3.setToolTip(properties_conn_queries.sql3MySQL)

        # runquery4
        self.MySQLbuttonRunQuery4 = QPushButton('RUN QUERY 4', self)
        self.MySQLbuttonRunQuery4.setGeometry(250, 25, 200, 50)
        self.MySQLbuttonRunQuery4.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.MySQLbuttonRunQuery4.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql4MySQL, properties_conn_queries.curMySQL, order=4))
        self.MySQLbuttonRunQuery4.clicked.connect(lambda: timer.setEnabled(self.MySQLbuttonRunQuery4))
        self.MySQLbuttonRunQuery4.setToolTip(properties_conn_queries.sql4MySQL)
        # runquery5
        self.MySQLbuttonRunQuery5 = QPushButton('RUN QUERY 5', self)
        self.MySQLbuttonRunQuery5.setGeometry(250, 100, 200, 50)
        self.MySQLbuttonRunQuery5.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.MySQLbuttonRunQuery5.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql5MySQL, properties_conn_queries.curMySQL, order=5))
        self.MySQLbuttonRunQuery5.clicked.connect(lambda: timer.setEnabled(self.MySQLbuttonRunQuery5))
        self.MySQLbuttonRunQuery5.setToolTip(properties_conn_queries.sql5MySQL)
        #runquery6
        self.MySQLbuttonRunQuery6 = QPushButton('RUN QUERY 6', self)
        self.MySQLbuttonRunQuery6.setGeometry(250, 175, 200, 50)
        self.MySQLbuttonRunQuery6.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.MySQLbuttonRunQuery6.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql6MySQL, properties_conn_queries.curMySQL, order=6))
        self.MySQLbuttonRunQuery6.clicked.connect(lambda: timer.setEnabled(self.MySQLbuttonRunQuery6))
        self.MySQLbuttonRunQuery6.setToolTip(properties_conn_queries.sql6MySQL)
        # reset button
        self.ResetButton = QPushButton('RESET', self)
        self.ResetButton.setGeometry(250, 400, 200, 50)
        self.ResetButton.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MySQLbuttonRunQuery1))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MySQLbuttonRunQuery2))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MySQLbuttonRunQuery3))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MySQLbuttonRunQuery4))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MySQLbuttonRunQuery5))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.MySQLbuttonRunQuery6))
        self.ResetButton.setToolTip("Reset all buttons and content of file")
class WindowOracle(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Oracle")
        self.setFixedSize(480, 480)
        self.setWindowIcon(QIcon('C:\\Users\\alber\\Downloads\\oracle_icon.png'))
        # runquery1
        self.OraclebuttonRunQuery1 = QPushButton('RUN QUERY 1', self)
        self.OraclebuttonRunQuery1.setGeometry(10, 25, 200, 50)
        self.OraclebuttonRunQuery1.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.OraclebuttonRunQuery1.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql1ORACLE, properties_conn_queries.curOracle, order=1))
        self.OraclebuttonRunQuery1.clicked.connect(lambda: timer.setEnabled(self.OraclebuttonRunQuery1))
        self.OraclebuttonRunQuery1.setToolTip(properties_conn_queries.sql1ORACLE)
        #runquery2
        self.OraclebuttonRunQuery2 = QPushButton('RUN QUERY 2', self)
        self.OraclebuttonRunQuery2.setGeometry(10, 100, 200, 50)
        self.OraclebuttonRunQuery2.setStyleSheet(
             "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.OraclebuttonRunQuery2.clicked.connect(
             lambda: timer.runQuery(properties_conn_queries.sql2ORACLE, properties_conn_queries.curOracle, order=2))
        self.OraclebuttonRunQuery2.clicked.connect(lambda: timer.setEnabled(self.OraclebuttonRunQuery2))
        self.OraclebuttonRunQuery2.setToolTip(properties_conn_queries.sql2ORACLE)
        # runquery3
        self.OraclebuttonRunQuery3 = QPushButton('RUN QUERY 3', self)
        self.OraclebuttonRunQuery3.setGeometry(10, 175, 200, 50)
        self.OraclebuttonRunQuery3.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.OraclebuttonRunQuery3.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql3ORACLE, properties_conn_queries.curOracle, order=3))
        self.OraclebuttonRunQuery3.clicked.connect(lambda: timer.setEnabled(self.OraclebuttonRunQuery3))
        self.OraclebuttonRunQuery3.setToolTip(properties_conn_queries.sql3ORACLE)
        # runquery4
        self.OraclebuttonRunQuery4 = QPushButton('RUN QUERY 4', self)
        self.OraclebuttonRunQuery4.setGeometry(250, 25, 200, 50)
        self.OraclebuttonRunQuery4.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.OraclebuttonRunQuery4.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql4ORACLE, properties_conn_queries.curOracle, order=4))
        self.OraclebuttonRunQuery4.clicked.connect(lambda: timer.setEnabled(self.OraclebuttonRunQuery4))
        self.OraclebuttonRunQuery4.setToolTip(properties_conn_queries.sql4ORACLE)
        # runquery5
        self.OraclebuttonRunQuery5 = QPushButton('RUN QUERY 5', self)
        self.OraclebuttonRunQuery5.setGeometry(250, 100, 200, 50)
        self.OraclebuttonRunQuery5.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.OraclebuttonRunQuery5.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql5ORACLE, properties_conn_queries.curOracle, order=5))
        self.OraclebuttonRunQuery5.clicked.connect(lambda: timer.setEnabled(self.OraclebuttonRunQuery5))
        self.OraclebuttonRunQuery5.setToolTip(properties_conn_queries.sql5ORACLE)
        # runquery6
        self.OraclebuttonRunQuery6 = QPushButton('RUN QUERY 6', self)
        self.OraclebuttonRunQuery6.setGeometry(250, 175, 200, 50)
        self.OraclebuttonRunQuery6.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.OraclebuttonRunQuery6.clicked.connect(
            lambda: timer.runQuery(properties_conn_queries.sql6ORACLE, properties_conn_queries.curOracle, order=6))
        self.OraclebuttonRunQuery6.clicked.connect(lambda: timer.setEnabled(self.OraclebuttonRunQuery6))
        self.OraclebuttonRunQuery6.setToolTip(properties_conn_queries.sql6ORACLE)
        # # reset button
        self.ResetButton = QPushButton('RESET', self)
        self.ResetButton.setGeometry(250, 400, 200, 50)
        self.ResetButton.setStyleSheet(
            "QPushButton::hover { background-color: lightgreen }""QPushButton:pressed { background-color: red }")
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.OraclebuttonRunQuery1))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.OraclebuttonRunQuery2))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.OraclebuttonRunQuery3))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.OraclebuttonRunQuery4))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.OraclebuttonRunQuery5))
        self.ResetButton.clicked.connect(lambda: timer.resetButtons(self.OraclebuttonRunQuery6))
        self.ResetButton.setToolTip("Reset all buttons and content of file")





class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: darkolivegreen; border: 2px solid black;")
        self.title = "DB Comparison Tool"
        self.setGeometry(0, 0, 230, 230)
        self.InitWindow1()
        self.MSSQLButton.clicked.connect(self.windowMSSQL)
        self.MySQLbutton.clicked.connect(self.windowMySQL)
        self.Oraclebutton.clicked.connect(self.windowOracle)



    def InitWindow1(self):
        self.setWindowIcon(QIcon('C:\\Users\\alber\\OneDrive\\Dokumenty\\database.png'))
        # first button
        self.MySQLbutton = QPushButton('MySQL Connection', self)
        self.MySQLbutton.setGeometry(10, 25, 200, 50)
        self.MySQLbutton.setToolTip("Click to connect with MySQL DB")
        self.MySQLbutton.clicked.connect(self.dbConnectionMySQL)
        self.MySQLbutton.setStyleSheet(
            "QPushButton { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton {border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.setWindowTitle(self.title)


        # second button
        self.Oraclebutton = QPushButton('Oracle Connection', self)
        self.Oraclebutton.setGeometry(10, 80, 200, 50)
        self.Oraclebutton.setToolTip("Click to connect with Oracle DB")
        self.Oraclebutton.clicked.connect(self.dbConnectionORACLE)
        self.Oraclebutton.setStyleSheet(
            "QPushButton:pressed { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton { background-color: #3cbaa2; border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.setWindowTitle(self.title)


        # third button
        self.MSSQLButton = QPushButton('MSSQL Connection', self)
        self.MSSQLButton.setGeometry(10, 135, 200, 50)
        self.MSSQLButton.setToolTip("Click to connect with MSSQL DB")
        self.MSSQLButton.clicked.connect(self.dbConnectionMSSQL)
        self.MSSQLButton.setStyleSheet(
            "QPushButton:pressed { background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))}"
            "QPushButton { background-color: #3cbaa2; border: 1px solid black;border-radius: 5px;}"
            "QPushButton::hover { background-color: rgb(152,251,152) }""QPushButton:pressed { background-color: rgb(143,188,143)}")
        self.setWindowTitle(self.title)

        if os.path.exists(properties_conn_queries.filepath):
            os.remove(properties_conn_queries.filepath)

        self.show()

    def dbConnectionMySQL(self):
        try:
            # dbMySQL = pymysql.connect('localhost', 'bondya', 'pfizer', 'Dyplomowa_DB')
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
        except pymysql.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)

    def dbConnectionORACLE(self):
        dbOracle = None
        try:
            # cx_Oracle.init_oracle_client(lib_dir=r"C:\app\alber\product\18.0.0\dbhomeXE\instantclient\instantclient_19_8")
            dbOracle = cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding)

            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
        except cx_Oracle.Error as error:
            print(error)
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
        finally:
            # release the connection
            if dbOracle:
                dbOracle.close()

    def dbConnectionMSSQL(self):
        try:

            # dbMSSQL = pyodbc.connect('Driver={SQL Server};'
            #                          'Server=DESKTOP-M7HC7EL;'
            #                          'Database=MSSQL;'
            #                          'Trusted_Connection=yes;')
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')



        except cx_Oracle.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            sys.exit(1)

    def windowOracle(self):
        self.w = WindowOracle()
        self.w.show()

    def windowMSSQL(self):
        self.j = WindowMSSQL()
        self.j.show()

    def windowMySQL(self):
        self.k = WindowMySQL()
        self.k.show()


App = QApplication(sys.argv)

window = Window()
App.setStyle('Fusion')
sys.exit(App.exec())
