# SMLab Worklog
Инструмент для простого логирования времени работы

# Предусловия
Должен быть уставнолен `python3` и `pip3`

Инструкция для Windows: https://phoenixnap.com/kb/how-to-install-python-3-windows

Инструкция для Mac: https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3

# Установка
Скачиваем последний архив во вкладке "Релизы" https://github.com/tiomat/smlab_worklog/releases

Переходим в папку, открываем консоль и дальше выполняем:

```pip3 install -r requirements.txt```

# Использование
```python3 worklog.py -l login -p password -t 2 -k DRIVEN-3953 DRIVEN-3954 -c "Comment"```

```python3 worklog.py -l login -p password -t 0.5 -m daily -c "Comment"```

## Доступные ключи
* ```-l``` логин от Jira
* ```-p``` пароль от Jira
* ```-t``` общее количество времени, которое нужно списать, например `0.5`,`1`,`2`
* ```-s``` дата, за которую нужно списать время в формате ГГГГ-ММ-ДД
* ```-k``` ключ задач(и) в Jire разделенные пробелами, например, `DRIVEN-3953 DRIVEN-3954`
* ```-m``` вместо ключей задач и ключа `-k`, можно использовать ключ `-m` который может принять одно из следующих значений: `daily`, `retro`, `backlog`, `other`
