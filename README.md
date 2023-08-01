# SMLab Worklog
Инструмент для простого логирования времени работы

# Предусловия
Должен быть уставнолен `python3` и `pip3`

Инструкция для Windows: https://phoenixnap.com/kb/how-to-install-python-3-windows

Инструкция для Mac: https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3

# Install
```pip3 install requirements.txt```

# Use
```python3 worlog.py -l login -p password -t 2 -k DRIVEN-3953 DRIVEN-3954 -c "Comment"```

```python3 worlog.py -l login -p password -t 0.5 -m daily -c "Comment"```

## keys
* ```-l``` логин от Jira
* ```-p``` пароль от Jira
* ```-t``` общее количество времени, которое нужно списать, например `0.5`,`1`,`2` 
* ```-k``` ключ задач(и) в Jire разделенные пробелами, например, `DRIVEN-3953 DRIVEN-3954`
* ```-m``` вместо ключей задач и ключа `-k`, можно использовать ключ `-m` который может принять одно из следующих значений: `daily`, `retro`, `backlog`, `other`
