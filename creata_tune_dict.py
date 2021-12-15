
"""Данная функция на вход принимает имя файла ,в котором находятся данные с параметрами
   песни (id_album,name_tune,lenght_tune). СМОТРИ фаил tune.txt
    В результате мы получим dict {id_album:[[name_tune,lenght_tune],....,....]}"""

def _dict_tunes (list_name):
    _data = ''
    dict_albums = {}
    with open(list_name, encoding="utf-8") as file:
        for line in file:
            _data += line

    tune_param = (_data.split('\n\n'))
    for i in range(len(tune_param)):
        album_param = (tune_param[i].split('\n'))
        tunes = []
        key_ = album_param[0]
        if key_ == "":
            break
        for k in range(1, len(album_param)):
            tune = album_param[k].split("=")
            tunes.append(tune)
            if tunes[-1] == ['']:
                del tunes[-1]
        dict_albums[key_] = tunes
    return dict_albums




















