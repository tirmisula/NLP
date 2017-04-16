#!/usr/bin/python
# -*- coding: UTF-8 -*-
import operator

nKeyword = 10
d = 0.85
max_iter = 200;
min_diff = 0.001;

def getKeyword(wordList):
    words = dict()
    queue = list()
    entryList = list()
    for w in wordList:
        if w not in words:
            words[w] = set()
        queue.append(w)
        if len(queue) > 5:
            if len(queue) > 0:
                queue.pop(0)
        for w1 in queue:
            for w2 in queue:
                if w1 == w2:
                    continue
                words.get(w1).add(w2)
                words.get(w2).add(w1)
    score = dict()
    for i in range(0, max_iter):
        m = dict()
        max_diff = 0
        for key, value in words.items():
            m[key] = 1-d
            for other in value:
                size = len(words.get(other))
                if key == other and size == 0:
                    continue;
                if not score.get(other):
                    m[key] = m.get(key) + d / size * 0
                else:
                    m[key] = m.get(key) + d / size * score.get(other)
            if not score.get(key):
                max_diff = max(max_diff, abs(m.get(key) - 0))
            else:
                max_diff = max(max_diff, abs(m.get(key) - score.get(key)))
        score = m
        if max_diff <= min_diff:
            break;
    entryList = score
    entryList = sorted(entryList.items(), key=operator.itemgetter(1))
    return entryList;