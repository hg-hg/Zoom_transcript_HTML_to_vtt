import re


def GetMiddleStr(content, startStr, endStr):
    patternStr = r'%s(.+?)%s' % (startStr, endStr)
    p = re.compile(patternStr, re.IGNORECASE)
    m = re.match(p, content)
    if m:
        return m.group(1)


def filter_tags(htmlstr):
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    blank_line = re.compile('\n+')

    # 过滤匹配内容
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # s = blank_line.sub('\n', s)  # 去掉多余的空行

    return s


fi = open("transcript.txt", "r+", encoding='utf-8')
try:
    file_context = fi.read()
    # file_context是一个string，读取完后，就失去了对test.txt的文件引用
    # file_context = open(file).read().splitlines()
    # file_context是一个list，每行文本内容是list中的一个元素
finally:
    fi.close()

data_str = GetMiddleStr(file_context, "<ul data", "aria-label")

i = 1
while file_context.find("<span data" + data_str + "class=\"time\">") != -1:
    file_context = file_context.replace("<span data" + data_str + "class=\"time\">", str("\n\n" + str(i) + "\n"), 1)
    i = i + 1
file_context = file_context.replace("<span data" + data_str + "class=\"text\">", "\n")
file_context = filter_tags(file_context)

fo = open("formatted_transcript.transcript.vtt", "w+", encoding='utf-8')
fo.write(file_context)
fo.close()

fo_c = open("formatted_transcript.transcript.vtt", "r+", encoding='utf-8')
fo_list = fo_c.readlines()
fo_c.close()

fo_list[0] = "WEBVTT\n"
i = 3
while i + 4 < len(fo_list):
    fo_list[i] = fo_list[i].replace('\n', '') + ".500 --> " + fo_list[i + 4].replace('\n', '') + ".499\n"
    i = i + 4

fo_list[i] = fo_list[i].replace('\n', '') + ".500 --> 01:30:00.499\n"

fo_c = open("formatted_transcript.transcript.vtt", "w+", encoding='utf-8')
fo_c.writelines(fo_list)
fo_c.close()
