logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

str_logs = []

num_logs = []

for log in logs:
    if log.split(' ')[1].isnumeric():
        num_logs.append(log)
    else:
        str_logs.append(log)

str_logs.sort(key=lambda log: (log.split(' ')[1], log.split(' ')[0]))


print(str_logs + num_logs)
