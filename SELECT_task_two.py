import sqlalchemy


def sql_select (ask, fetch='all'):
    if fetch =='all':
        result = connection.execute(f"""{ask}""").fetchall()
    elif fetch == '1':
        result = connection.execute(f"""{ask}""").fetchone()
    else :
        result = connection.execute(f"""{ask}""").fetchmany(int(fetch))

    return result


engine = sqlalchemy.create_engine('postgresql://neto:123456@localhost:5432/netol_db')
connection = engine.connect()
# print("Состав БАЗЫ")
# res = connection.execute(""" SELECT table_name FROM information_schema.tables
#                              WHERE table_schema='public'; """"").fetchall()
# print(res)
#
# _tab = "tune"
# # print("Состав таблицы")
# res = connection.execute(f"""SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS
#                             WHERE table_name = '{_tab}'""").fetchall()
# print(res)
print("АЛЬБОМ 2018 года")

res = sql_select("""SELECT name_album,year_create FROM albums
                    WHERE year_create = 2018""")
print(res)

print("САМЫЙ дЛИННЫЙ трек ")
res = sql_select("""SELECT name_tune, lenght_tune FROM tune
                    ORDER BY lenght_tune DESC""", 1)
print(res)

print("ТРЕКИ меньше 3.5 мин")
res = sql_select("""SELECT name_tune, lenght_tune FROM tune
                    WHERE lenght_tune < 330
                    ORDER BY lenght_tune DESC""")
print(res)

print("СБОРНИКИ 2018 - 2020")
res = sql_select("""SELECT name_collection FROM collection
                    WHERE create_year BETWEEN 2018 and 2020
                    ORDER BY create_year""")
print(res)

print("ИМЕНА ПЕВЦОВ СОСТОЯЩИЕ ИЗ ОДНОГО ИМЕНИ ")
res = sql_select("""SELECT name_singer FROM singers
                    WHERE name_singer  NOT LIKE'%% %%' """)
print(res)
res = sql_select("""SELECT name_tune FROM tune
                   WHERE name_tune iLIKE'%%my%%' """)
print(res)

