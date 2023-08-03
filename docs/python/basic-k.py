"""
Dictionary testing
"""

d = dict()

print(d.keys(), len(d.keys()))

if len(d.keys()) <= 0:
    d['start'] = 0
else:
    d['end'] = 1

print(d.keys(), len(d.keys()))
