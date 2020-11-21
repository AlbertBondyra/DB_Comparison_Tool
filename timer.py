from datetime import datetime
import properties_conn_queries,os


def runQuery(query, cursor, order):
    start_time = datetime.now()
    cursor.execute(query)
    end_time = datetime.now()
    f = open(properties_conn_queries.filepath, "a", encoding="utf-8")
    start_time_in_microsec = start_time.microsecond
    start_time_in_sec = start_time.second
    end_time_in_microsec = end_time.microsecond
    end_time_in_sec = end_time.second
    diff_microsec = end_time_in_microsec - start_time_in_microsec
    diff_sec = end_time_in_sec - start_time_in_sec
    if (cursor == properties_conn_queries.curMSSQL):
        print('MSSQL : Czas rozpoczęcia wykonywania query' + str(order) + ':' + str(order) + str(start_time))
        f.write('MSSQL : Czas rozpoczęcia wykonywania query' + str(order) + ':' + str(start_time) + '\n')
        print('MSSQL : Czas zakończenia wykonywania query' + str(order) + ':' + str(end_time))
        f.write('MSSQL : Czas zakończenia wykonywania query' + str(order) + ':' + str(end_time) + '\n')
        print('MSSQL: Czas trwania query numer' + str(order) + ': ' + str(abs(diff_sec)) + 's' + str((abs(diff_microsec))) + 'microsecond')
        f.write('MSSQL: Czas trwania query numer' + str(order) + ': ' + str(abs(diff_sec)) + 's' + str((abs(diff_microsec))) + 'microsecond\n')
    elif (cursor == properties_conn_queries.curMySQL):
        print('MySQL : Czas rozpoczęcia wykonywania query' + str(order) + ':' + str(order) + str(start_time))
        f.write('MySQL : Czas rozpoczęcia wykonywania query' + str(order) + ':' + str(start_time) + '\n')
        print('MySQL : Czas zakończenia wykonywania query' + str(order) + ':' + str(end_time))
        f.write('MySQL : Czas zakończenia wykonywania query' + str(order) + ':' + str(end_time) + '\n')
        print('MySQL : Czas trwania query numer' + str(order) + ': ' + str(abs(diff_sec)) + 's' + str((abs(diff_microsec))) + 'microsecond')
        f.write('MySQL: Czas trwania query numer' + str(order) + ': ' + str(abs(diff_sec)) + 's' + str((abs(diff_microsec))) + 'microsecond\n')
    elif (cursor == properties_conn_queries.curOracle):
        print('ORACLE : Czas rozpoczęcia wykonywania query' + str(order) + ':' + str(order) + str(start_time))
        f.write('ORACLE : Czas rozpoczęcia wykonywania query' + str(order) + ':' + str(start_time) + '\n')
        print('ORACLE : Czas zakończenia wykonywania query' + str(order) + ':' + str(end_time))
        f.write('ORACLE : Czas zakończenia wykonywania query' + str(order) + ':' + str(end_time) + '\n')
        print('ORACLE: Czas trwania query numer ' + str(order) + ': ' + str(abs(diff_sec)) + 's' + str((abs(diff_microsec))) + 'microsecond')
        f.write('ORACLE: Czas trwania query numer' + str(order) + ': ' + str(abs(diff_sec)) + 's' + str((abs(diff_microsec))) + 'microsecond\n')
        f.close()


def setEnabled(button):
    button.setEnabled(False)


def resetButtons(button):
    button.setEnabled(True)
    if os.path.exists(properties_conn_queries.filepath):
        os.remove(properties_conn_queries.filepath)
