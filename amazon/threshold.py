"""
INPUT
4
1 2 50
1 7 70
1 3 20
2 2 17
2
"""

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def add_transaction(obj, user):
    if obj.get(user):
        obj[user]+= 1
    else:
        obj[user] = 1
    return obj
    
def processLogs(logs, threshold):
    """
    logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
    threshold = 2
    """
    transactions = {}
    for log in logs:
        sender, recipient, amount = log.split(" ")
        if sender == recipient:
            transactions = add_transaction(transactions, sender)
        else:
            transactions = add_transaction(transactions, sender)
            transactions = add_transaction(transactions, recipient)
    response = ""
    for k, v in transactions.items():
        if v >= threshold:
            response = f"{response}{k}\n"
            
    return response.strip()
    
    # Write your code here

if __name__ == '__main__':
    """
    4
    1 2 50
    1 7 70
    1 3 20
    2 2 17
    2
    """

    logs = ["1 2 50","1 7 70",  "1 3 20", "2 2 17"]

    threshold = 2

    result = processLogs(logs, threshold)

    print(result)