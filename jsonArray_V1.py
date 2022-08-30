#!/usr/bin/env python
# coding: utf-8

# In[11]:

import os
import json
def getArray(e):
    listObj = {}
    try:
        with open(os.getcwd() + "\\resrc\\details.json") as fp:
            listObj = json.load(fp)
    except:
        listObj = {}
    print(listObj)
    a = list(listObj)
    b = list(listObj[e])
    courseOutcomes = []
    courseOutcomesNo = []
    f = len(b)
    key_list = list(listObj[e].keys())
    for i in range(2,7):
        courseOutcomes.append(listObj[e][b[i]])
        courseOutcomesNo.append(key_list[i])
    courseObjectives = []
    for i in range(7, f):
        courseObjectives.append(listObj[e][b[i]])
    print(courseOutcomes, courseOutcomesNo, courseObjectives)
    return courseOutcomes, courseOutcomesNo, courseObjectives

# getArray('cs8888')


# In[ ]:




