#!/usr/bin/env python
#coding:utf-8
###################################################
#### check string seriation(检测字符串顺序排列)####
#### 待测字符串存在 example20150914.txt ###########
###################################################

str_file_PATH = 'example20150914.txt'

def str_seriation_check(str):
#       "-*-检测字符串顺序排列-*-"
#       print str_seriation_check.__doc__
        print "-*-检测字符串顺序排列-*-{0}".format(str).strip('\n')
        if len(str) < 2:
                return "字符串太短"
        for i in xrange(len(str)):
                if i >= 1:
                        if str[i-1] <= str[i]:
                                continue
                        else:
                                return "Fail,字符串不是按顺序排列的. 第 {} 位大于第 {} 位.".format(i, i+1)
        return "OK,字符串是按顺序排列的."

def read_file(file_str):
        fr = open(file_str)
        for read_line in fr:
                print str_seriation_check(read_line)

if __name__ == "__main__":
        read_file(str_file_PATH)
