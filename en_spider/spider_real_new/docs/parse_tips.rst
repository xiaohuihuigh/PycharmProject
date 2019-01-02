一些解析中的要点
==============

添加步骤
-------

- 添加前，要先看下该网站，以及相同网站的页面，确认页面内文章时间，更新频率，文章页是否有效。最好将同一站点的不同页面，一起添加解析。

- 首先确认是否已有该站点，假如有，就先确认好解析文件，以便确认解析类名。

- 然后即可添加页面到数据库，随后新建parse文件，更新类名，然后将类名注册到get_parse。随后添加content_parse。

- 然后更新manage文件的测试sid，然后去调整parse文件，确保调通。

常见报错
-------

- lines直接不出来，那说明xpath语法直接报错

- lines为0，那就是解析链接列表的xpath没报错，但写的不对

- lines有了后,就可以解析具体url等信息。

- nums数目为0， 说明解析具体信息不对。尤其是nid解析，必须对。

- nums有了后，接下来就是去检验content解析。

- keyerror报错，通常是没有正确注册parse类，去get_parse找原因

- 一切都对，数据库也写入，但content却没有，很可能是没有注册content解析函数

- 还有一种错误，是数据库忘记插入网站信息，要注意

- 还要注意存入数据库的url,要带http等协议字样,末尾不要有其他字符

- TypeError: sequence item 0: expected string, lxml.etree._Element found 这个错误,是因为在写的xpath上,没有加/text()这个

- globals()[func](root, item) KeyError: u'chinabreed1' 这是没有找到解析内容的那个函数


框架细节
----------

解析细节
----------

- 解析时不要解析tbody这个标签,而是用//跳过它.否则会解析失败
