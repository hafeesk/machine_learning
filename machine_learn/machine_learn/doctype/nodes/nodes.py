# -*- coding: utf-8 -*-
# Copyright (c) 2015, hafees and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from textblob import TextBlob
from nltk.stem.porter import *

class Nodes(Document):
	def create_words(self):
		wiki = TextBlob(self.paragraph)
		tag_words= wiki.tags
		filter_this_tags = ['DT','VBZ','CC','IN','PRP$','PDT','MD','WDT']
		words = []
		for i in tag_words:
			if i[1] in filter_this_tags:
				continue
			else:
				words.append(i[0])

		word_data = ",".join(words)
		#creating stem
		stem_word = []
		stemmer = PorterStemmer()

		for i in words:
			stem_word.append(stemmer.stem(i))

		lemming_words = ",".join(stem_word)

		return {'words':word_data,'stem_word':lemming_words}


	
