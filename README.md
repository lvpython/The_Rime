#鼠须管配置说明

##你为什么要这么做

	当输入法比较卡
	当输入的候选词没有你要的,
	你的专业词汇总是被靠后,总是翻篇
	你有多个要工作的电脑,输入法的配置要统一
	当你想定义你自己的词典,圈定你的专业领域输入法

前人栽树 https://segmentfault.com/a/1190000005754706

##简而言之

###备份鼠须管初始配置
鼠须管配置目录 ~/Library/Rime

	cp -a ~/Library/Rime ~/Library/Rime_ori_$(date +%Y%m%d%H%M%S)
	会得到一个类似 ~/Library/Rime_ori_20170501225630 的文件夹 即为备份

###部署配置

	把Rime里面的东西拷贝到 ~/Library/Rime ，覆盖即可。然后重新部署
	词库说明：增强包里的词库，是鼠须管原生词库的 *.dict.yaml 格式的词库


###重新部署

	点击屏幕右上处的输入法小图标，选用鼠须管输入法✓
	点击鼠须管输入法图标，选择 重新部署 (约1分钟)
	选择简体中文输入：ctrl+` 并选择 《朙月拼音·简化字》方案

###卸载办法
如何干净地卸载鼠须管输入法？

	say goodbye Squirrel && killall Squirrel
	系统偏好设置 - 键盘 - 输入源 - 鼠须管，移除
	sudo rm -rf "/Library/Input Methods/Squirrel.app"
	rm -rf ~/Library/Rime


##做的调整
我是程序员
所以这个配置的需求都是程序员的角度看的,做了这几个变化

	1.	中文状态下如何配置输入英文标点"`" ; [ ] 键换頁
	2.	# squirrel.custom.yaml 配置 应用程序里的输入法状态,比如Alfred,VSCode下默认输入英文  

我是佛教徒,我想自定义自己的词库.做了这几个变化

	1. update_scel_dict.sh 做了这个脚本, 生成自定义词典f_myphrases.dict.yaml,并copy到Rime配置目录下
	2. 在my_dicts目录下的.txt文件都会作为细胞字库原料加入

##词典来源
###传了一份在百度云盘

	链接:https://pan.baidu.com/s/1dHjgced  密码:0297

###里面内容是这样的
![](https://i.loli.net/2018/02/09/5a7cdef284744.jpg)
##我自己选的一些词库
![](https://i.loli.net/2018/02/09/5a7cdf5816d66.jpg)

然后就可以根据自己的习惯定义和维护个人词典了.
常常要做的就是
```
sh update_scel_dict.sh
```
