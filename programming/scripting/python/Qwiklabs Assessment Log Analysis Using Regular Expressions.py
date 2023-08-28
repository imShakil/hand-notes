#!/usr/bin/env python3
import re
import csv
import operator


errors = {}
stats = {}

logs = open("syslog.log", "r").readlines()
logs = [log.strip() for log in logs]


def sortResult(res, k=None, rev=False):
   sortedResult = sorted(res.items(), key=k, reverse=rev)
   return sortedResult


def collect_logs():
    pattern = r"(ERROR|INFO)\s([\w \']*).*\(([\w\.\w ]*)\)"
    for log in logs:
        res = re.search(pattern, log) # find 3 groups, 1: ERROR | INFO, 2: Message, 3: username
        if res:
            logLevel, logMessage, userName = res.groups()

            # count logMessage
            if logLevel == 'ERROR':
                if logMessage in errors.keys():
                    errors[logMessage] += 1
                else:
                    errors[logMessage] = 1

            # count user statistics
            if userName in stats.keys():
                stats[userName][logLevel] += 1
            else:
                stats[userName] = {}
                stats[userName]["INFO"] = stats[userName]["ERROR"] = 0
                stats[userName][logLevel] += 1


if __name__ == "__main__":
    
    collect_logs()

    errors = sortResult(errors, k=operator.itemgetter(1), rev=True)
    stats = sortResult(stats)

    #print(errors)
    #print(stats)

    # create error_message.csv
    def create_error_message_csv():
        with open("error_message.csv", "w") as file:
            csv_file = csv.writer(file)
            csv_file.writerow(['Error', 'Count'])
            for item in errors:
                csv_file.writerow(item)
        file.close()


    def create_user_statics_csv():
        with open("user_statistics.csv", "w") as file:
            csv_file = csv.writer(file)
            csv_file.writerow(['Username', 'INFO', "ERROR"])
            for user, item in stats:
                csv_file.writerow([user, item['INFO'], item['ERROR']])
            
        file.close()
    
    create_error_message_csv()
    create_user_statics_csv()