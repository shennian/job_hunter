# encoding=utf-8
import jieba
import os
import json


__author__ = 'sen'


class SearchEngine():
    def __init__(self, json_files_path):
        self.path = json_files_path
        self.pages_info = self.init_json_data()

    def init_json_data(self):
        def list_filename(path):
            for filename in os.listdir(self.path):
                yield filename

        file_names = list_filename(self.path)
        pages_info = []
        for filename in file_names:
            if '.json' not in filename:
                continue
            page_info = [filename]
            with open(self.path + filename) as data_file:
                data = json.load(data_file)
                page_info.append(data)
            pages_info.append(page_info)
        return pages_info

    # return: list
    def cut_words(self, content):
        words_list = []
        segments = jieba.cut(content)
        for segment in segments:
            words_list.append(segment)
        for i in words_list:
            print i
        return words_list

    def search_keywords(self, words_list):
        pages_keywords_list = []
        for info in self.pages_info:
            keywords_list = [info[0]]
            for k, v in info[1].items():
                for i in words_list:
                    if i == k:
                        keywords_list.append((k, v))
            pages_keywords_list.append(keywords_list)
        return pages_keywords_list

    def search(self, page_keywords_list, words_list):
        target_pages = []
        words_list_length = len(words_list)
        for info in page_keywords_list:
            # searching rules
            if words_list_length + 1 == len(info):
                target_pages.append(info)
            elif float(words_list_length)/len(info) > 0.5 and \
                                    float(words_list_length) / len(info) < 1:
                target_pages.append(info)
        return target_pages

    # simple rule is according to frequency
    def rank(self, target_pages):
        frequencys = []
        for page in target_pages:
            f = 0
            for num in page[1:]:
                f += num[1]
            frequencys.append(f)

        def rank_max(nums):
            max_index = 0
            for i in range(1, len(nums)):
                if nums[i] > nums[max_index]:
                    max_index = i
            nums[max_index] = -1
            return max_index

        pages_rank_list = []
        for k in target_pages:
            i = rank_max(frequencys)
            pages_rank_list.append(target_pages[i])
        return pages_rank_list

    def run(self, content):
        words_list = self.cut_words(content)
        keywords_list = self.search_keywords(words_list)
        target_pages = self.search(keywords_list, words_list)
        rank_pages = self.rank(target_pages)
        self.display(rank_pages)
        return rank_pages

    def display(self, rank):
        for i in rank:
            print i[0],
            for v in i[1:]:
                print v[0], v[1],
            print ""






