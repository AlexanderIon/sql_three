import sqlalchemy
import data_for_table
from creata_tune_dict import _dict_tunes
"""в модуле data_for_table находятся данны для заполнения таблиц (singers, ganers, albums....)
   фаил tune.txt содержит id_album, название песен в альбоме и их продолжительность
    модул creata_tune_dict содержит функцию для чтения файла tune.txt """

engine = sqlalchemy.create_engine('postgresql://neto:123456@localhost:5432/netol_db')

connection = engine.connect()


def fill_in_table(list_data, name_table, name_column):
    for i in range(len(list_data)):
        element = list_data[i]
        connection.execute(f"""INSERT INTO {name_table} ({name_column})
                      VALUES ('{element}'); """)


def fill_in_table_two_column (data_list, name_table, column1, column2):
    for i in range(len(data_list)):
        element = data_list[i]
        connection.execute(f"""INSERT INTO {name_table} ({column1},{column2})
                                VALUES ('{element[0]}','{element[1]}')""")


def sql_select(ask):
    result = connection.execute(f""" {ask} """"").fetchall()
    return result


# print("Состав БАЗЫ")
# res = connection.execute(""" SELECT table_name FROM information_schema.tables
#                              WHERE table_schema='public'; """"").fetchall()
# print(res)
# _tab = "tune"
# print("Состав таблицы")
# res = connection.execute(f"""SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS
#                             WHERE table_name = '{_tab}'""").fetchall()
# print(res)

""" ЗАПОЛНяем таблицу ПЕСНИ(tunes) для этого воспользуемся функцией _dict_tunes из файла creata_tune_dict"""
dict_for_table_tune = _dict_tunes('tune.txt')
for key, means in dict_for_table_tune.items():
    id_album = key
    for q in range(len(means)):
        tunes_name = means[q][0]
        tunes_lenght = means[q][1]
        connection.execute(f"""INSERT INTO tune (id_album,lenght_tune,name_tune)
                                        VALUES ({id_album},{tunes_lenght},'{tunes_name}')""")
"""ЗАПОЛНЯЕМ ОТСТАВШИЕСЯ ТАБЛИЦЫ """
fill_in_table(data_for_table.singers, 'singers', 'name_singer')
fill_in_table(data_for_table.genars, 'genars', 'name_genar')
fill_in_table_two_column(data_for_table.album_and_singer, 'album_and_singer', 'id_album', 'id_singer')
fill_in_table_two_column(data_for_table.singer_and_genar, 'singer_and_genar', 'id_singer', 'id_genar')
fill_in_table_two_column(data_for_table.collection, 'collection', 'create_year', 'name_collection')
fill_in_table_two_column(data_for_table.tune_in_collection, 'tune_in_collection', "id_tune", 'id_collection')


for i in range(len(data_for_table.albums)):
    element = data_for_table.albums[i]
    connection.execute(f"""INSERT INTO albums (year_create,name_album)
                            VALUES ({int(element[1])},'{element[0]}')""")



# print(connection.execute("""SELECT* FROM singers""").fetchall())
# connection.execute("""DELETE FROM tune_in_collection; """)
# connection.execute(""" ALTER SEQUENCE collection_id_collection_seq RESTART WITH 1;""")

# print(sql_select(f'SELECT * FROM {_tab};'))






