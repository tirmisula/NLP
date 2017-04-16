#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import Parser
import IOUtil
import TextRank

def readPDFFolder(dir):
    output = open('res/results.txt', 'a')
    list = os.listdir(dir)
    for file in list:
        path = "res/pdf/" + file
        text = IOUtil.readPDF(path)
        wordsList = Parser.remove_noise(text)
        keywords = TextRank.getKeyword(wordsList)
        for i in keywords:
            print i
            print str(i)
            output.write(str(i))
            output.write("\n")
        print "Passage is Over."
        print "********************************"
        output.write("Passage is Over.")
        output.write("\n")
        output.write("********************************")
        output.write("\n")
    output.close()
readPDFFolder("res/pdf/")
# text = IOUtil.readTXT("res/txt/1.txt")

