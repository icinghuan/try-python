# -*-coding:utf8-*-

import re
import requests
from bs4 import BeautifulSoup

biquge_url = "https://www.biquge.com.cn"

novel_url = "/book/11029/"

if __name__ == '__main__':
    biquge_res = requests.get(biquge_url + novel_url)
    biquge_soup = BeautifulSoup(biquge_res.content, "html.parser")
    # flag = False
    fo = open("修真聊天群" + ".txt", "w")
    for item in biquge_soup.find_all("dd"):
        # if flag:
        #     break
        # flag = True
        chapter = re.match('<dd><a href="(.*)">(.*)</a></dd>', str(item))
        if chapter is None:
            continue
        print(chapter.group(1))
        fo.write(chapter.group(2))
        fo.write("\r\n")
        novel_res = requests.get(biquge_url + chapter.group(1))
        novel_soup = BeautifulSoup(novel_res.content, "html.parser")
        # ma = re.match('<div id="content">(.*)</div>', str(novel_res.content))
        max_len = 0
        div = novel_soup.find("div", id="content")
        fo.write(div.text.replace("    ", "\r\n"))
        fo.write("\r\n")
        fo.write("\r\n")
        fo.write("\r\n")
        fo.write("\r\n")
        fo.write("\r\n")
    fo.close()


def saveToFile(str, name):
    # 打开文件
    # str = "abc"
    fo = open(name + ".txt", "w")
    # print("文件名为: ", fo.name)
    # str = ""
    fo.write(str)
    # 关闭文件
    fo.close()
