# smlab_worklog
Tool for painless time logging

# Prerequisite
python3 and pip3 installed

# Install
```pip3 install requirements.txt```

# Use
```python3 worlog.py -l login -p password -t 2 -k DRIVEN-3953 DRIVEN-3954 -c "Comment"```

```python3 worlog.py -l login -p password -t 0.5 -m daily -c "Comment"```

## keys
-l login
-p password
-t total time to log, for e.g. 0.5, 1, 2.5 etc.
-k keys of Jira task separated with whitespaces for e.g. DRIVEN-3953 DRIVEN-3954
-m instead of jira keys you can use "daily", "retro", "backlog", "other"
