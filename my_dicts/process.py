import os
import hashlib

class Counter(dict):

    def __missing__(self, key):
        return None
        
current_path = os.path.split(os.path.realpath(__file__))[0]

reult_file = open("f_myphrases.dict.yaml", 'w')
word_dict = Counter()

yaml_header = """
# Rime dictionary
# encoding: utf-8
#
# f_myphrases.dict.yaml
#

---
name: f_myphrases
version: "2018.02.08"
sort: by_weight
use_preset_vocabulary: true
...

"""


## 如果使用 rime_dict_manager 工具,dic格式文件请注释下面一行
reult_file.write(yaml_header)


        
files = []
for (dirpath, dirnames, filenames) in os.walk(current_path):
    filenames = list(filter(lambda i:os.path.splitext(i)[1] == '.txt', filenames))
    full_names = ["%s/%s" % (dirpath, f) for f in filenames]
    files.extend(full_names)
    break
lines = []
for filename in files:    
    with open(filename) as f:
        for content in f.readlines():
            # format 阿魏,a'wei -> 阿魏<tab>a<space>wei<tab>1
            word = hashlib.md5(content.split(',')[0].encode('utf-8')).hexdigest()
            if not word_dict[word]:
                word_dict[word] = 1
                content = content.replace(',','\t').replace('\'', ' ').replace('\n', '')+'\n'
                #reult_file.write(content)
                lines.append(content)
for line in sorted(lines):
    reult_file.write(line)
reult_file.close()
        
