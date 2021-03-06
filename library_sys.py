#!/usr/bin/env python
# coding:utf-8
### 图书馆系统
### 添加书籍、删除书籍、检索书库、检索用户借阅、借阅书籍(后续将完善书架)
### library_sys.py

class library(object):
	def __init__(self):
		self.SN_dict = {123:'python', 234:'python'}	#唯一性SN编号与书名
		self.user_dict = {'zhangsan':[123, 234]}	#借阅者与借阅列表

	def add_book(self, sn, new_book):	#添加书籍
		self.SN_dict[sn] = new_book
	
	def del_book(self, old_sn):	#删除书籍
		self.SN_dict.pop(old_sn)
	
	def find_book(self, index):	#检索书库，按索引条件
		if isinstance(index, int) == True:	#按 SN编号 检索
			if index not in self.SN_dict.keys():
				return "SN编号不存在"
			result = self.SN_dict[index]
			return "SN编号:{0} 的书籍:《{1}》".format(index, result)
		book_num = self.SN_dict.values().count(index)	#按 书名 检索
		if book_num == 0:
			return "没有《{0}》".format(index)
		else:
			tmp_sn = []
			for key,value in self.SN_dict.iteritems():	#根据书名 检索 SN编号
				if value == index:
					tmp_sn.append(key)
			return "《{0}》的SN编号列表:{1}".format(index, tmp_sn)

	def find_user(self, name):	#检索用户借阅
		if (name in self.user_dict.keys()) == True:
			tmp_sn_book = {}
			tmp_sn = self.user_dict[name]
			for sn in tmp_sn:
				tmp_sn_book[sn] = self.SN_dict[sn]
			return "{0} 已借阅 {1}".format(name, tmp_sn_book)
		return "{0} 没有借书".format(name)
	
	def borrow_book(self, sn, name):	#借阅书籍
		self.user_dict[name].append(sn)
		tmp_sn_book = {}
		tmp_sn_book[sn] = self.SN_dict[sn]
		return "{0} 成功借阅《{1}》".format(name, tmp_sn_book)

library_example = library()	#实例化对象
print library_example.find_book("python")
print library_example.find_user("zhangsan")
library_example.add_book(1234,'shell')
print library_example.find_book(1234)
library_example.del_book(1234)
print library_example.find_book(1234)
