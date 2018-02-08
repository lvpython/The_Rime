
# build 明月拼音的用户字典，该字典直接拷到Library/Rime，重置以后就生效
# ./rime_dict_manager -i luna_pinyin result.dic
python3 process.py

cp f_myphrases.dict.yaml ~/Library/Rime
