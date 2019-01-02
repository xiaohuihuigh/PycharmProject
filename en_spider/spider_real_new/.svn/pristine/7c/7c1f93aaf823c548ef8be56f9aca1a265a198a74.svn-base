爬虫数据库建表
=============

网站信息表
::

    CREATE TABLE `spider_site` (
      `sid` smallint(5) unsigned NOT NULL COMMENT '站ID',
      `name` varchar(16) DEFAULT NULL COMMENT '站名',
      `re_url` varchar(64) DEFAULT NULL COMMENT '新闻地址正则，re.search()',
      `url` varchar(255) DEFAULT NULL COMMENT '爬取地址',
      `source` varchar(255) DEFAULT NULL COMMENT '源地址',
      `weight` tinyint(4) DEFAULT NULL COMMENT '基准分数',
      `main_class` varchar(64) DEFAULT NULL COMMENT '页面解析类名',
      `parse_func` varchar(32) DEFAULT NULL COMMENT '内容解析函数',
      `pbes` varchar(16) DEFAULT NULL COMMENT '>probability,>begin,<end,sleep',
      `status` tinyint(4) DEFAULT NULL COMMENT '状态',
      PRIMARY KEY (`sid`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4

新闻存储表
::

    CREATE TABLE `spider_news` (
      `sid` smallint(6) NOT NULL COMMENT '网站编码',
      `nid` bigint(20) NOT NULL COMMENT '新闻编码',
      `url` varchar(256) DEFAULT NULL COMMENT '新闻地址',
      `title` varchar(256) DEFAULT NULL COMMENT '新闻标题',
      `abstract` text COMMENT '摘要',
      `content` text COMMENT '新闻内容',
      `stocks` varchar(255) NOT NULL,
      `sectors` varchar(255) NOT NULL,
      `timestamp` int(11) unsigned DEFAULT NULL COMMENT '新闻时间戳',
      `score` tinyint(4) DEFAULT NULL COMMENT '新闻分数',
      `weight` tinyint(4) DEFAULT NULL COMMENT '权重',
      `counts` tinyint(3) unsigned DEFAULT NULL COMMENT '相似新闻数量',
      `source` int(11) unsigned DEFAULT NULL COMMENT '重复次数',
      `status` tinyint(4) DEFAULT NULL COMMENT '状态',
      `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
      PRIMARY KEY (`sid`,`nid`),
      KEY `status` (`status`),
      KEY `source` (`source`),
      KEY `ix_create_time` (`create_time`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4


全球指数表
::

    CREATE TABLE `foreign_index_price_m1_crawl` (
      `trade_time` datetime NOT NULL COMMENT '交易时间',
      `index_id` varchar(16) NOT NULL COMMENT '指数ID',
      `popen` float NOT NULL DEFAULT '0' COMMENT '开盘指数',
      `phigh` float NOT NULL DEFAULT '0' COMMENT '指数最高值',
      `plow` float NOT NULL DEFAULT '0' COMMENT '指数最低值',
      `pclose` float NOT NULL DEFAULT '0' COMMENT '收盘指数',
      `chg` float NOT NULL DEFAULT '0' COMMENT '涨幅',
      `vol` bigint(20) NOT NULL DEFAULT '0' COMMENT '成交量',
      `prefclose` float NOT NULL DEFAULT '0',
      PRIMARY KEY (`trade_time`,`index_id`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4


债券表
::

    CREATE TABLE `bond_rate_day` (
      `Date` datetime NOT NULL,
      `BondId` int(11) NOT NULL DEFAULT '0',
      `OpenPrice` decimal(19,4) DEFAULT NULL,
      `HighPrice` decimal(19,4) DEFAULT NULL,
      `LowPrice` decimal(19,4) DEFAULT NULL,
      `ClosePrice` decimal(19,4) DEFAULT NULL,
      PRIMARY KEY (`Date`,`BondId`),
      KEY `Date` (`Date`),
      KEY `BondId` (`BondId`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4

外汇表
::

    CREATE TABLE `fx_price_day` (
      `Date` datetime NOT NULL,
      `FxId` int(11) NOT NULL DEFAULT '0',
      `OpenPrice` decimal(19,4) DEFAULT NULL,
      `HighPrice` decimal(19,4) DEFAULT NULL,
      `LowPrice` decimal(19,4) DEFAULT NULL,
      `ClosePrice` decimal(19,4) DEFAULT NULL,
      `Chg` decimal(19,4) DEFAULT NULL,
      PRIMARY KEY (`Date`,`FxId`),
      KEY `Date` (`Date`),
      KEY `FxId` (`FxId`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4


华尔街见闻财经日历
::

    CREATE TABLE `finance_calendar_global` (
      `id` int(11) NOT NULL DEFAULT '0',
      `timestamp` int(11) NOT NULL COMMENT '时间',
      `level` int(11) DEFAULT NULL,
      `title` varchar(100) DEFAULT NULL COMMENT '标题',
      `country` varchar(100) DEFAULT NULL COMMENT '国家',
      `category_id` int(11) DEFAULT NULL,
      `score` float DEFAULT NULL COMMENT '事件分数',
      `sectors` varchar(100) DEFAULT NULL COMMENT '影响板块',
      `stocks` varchar(100) DEFAULT NULL COMMENT '影响股票',
      `active` tinyint(1) NOT NULL DEFAULT '1' COMMENT '是否可用 1.可用 0.不可用',
      PRIMARY KEY (`id`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4

雪球大V文章
::

    CREATE TABLE `xueqiu_blog` (
      `id` bigint(20) NOT NULL COMMENT '文章id',
      `user_id` bigint(20) NOT NULL COMMENT '用户id',
      `title` varchar(255) DEFAULT NULL COMMENT '标题',
      `created_at` bigint(20) DEFAULT NULL COMMENT '文章创建时间',
      `fav_count` int(10) DEFAULT NULL COMMENT '收藏数',
      `like_count` int(10) DEFAULT NULL COMMENT '点赞数',
      `mark` int(10) DEFAULT NULL COMMENT '标记',
      `reply_count` int(10) DEFAULT NULL COMMENT '回复数',
      `retweet_count` int(10) DEFAULT NULL COMMENT '转发数',
      `view_count` int(10) DEFAULT NULL COMMENT '阅读数',
      `type` int(10) DEFAULT NULL COMMENT '类型， 3为专栏，2为非专栏',
      `target` varchar(100) DEFAULT NULL COMMENT '网址',
      `description` text COMMENT '摘要',
      `content` text COMMENT '文章内容',
      `html` text COMMENT '原始文章内容',
      `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录插入时间',
      PRIMARY KEY (`id`) USING BTREE,
      KEY `user_id` (`user_id`),
      KEY `type` (`type`),
      KEY `created_at` (`created_at`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4

雪球大V用户
::

    CREATE TABLE `xueqiu_user` (
      `id` bigint(20) NOT NULL COMMENT '用户id',
      `gender` varchar(10) DEFAULT NULL COMMENT '性别',
      `city` varchar(20) DEFAULT NULL COMMENT '城市',
      `province` varchar(20) DEFAULT NULL COMMENT '省份',
      `description` varchar(255) DEFAULT NULL COMMENT '简介',
      `followers_count` int(10) DEFAULT NULL COMMENT '粉丝数',
      `friends_count` int(10) DEFAULT NULL COMMENT '关注数',
      `screen_name` varchar(100) DEFAULT NULL COMMENT '昵称',
      `status_count` int(10) DEFAULT NULL COMMENT '发贴数',
      `stocks_count` int(10) DEFAULT NULL COMMENT '股票数',
      `verified_description` varchar(255) DEFAULT NULL COMMENT '认证信息',
      `type` int(10) DEFAULT NULL COMMENT '用户类型',
      `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据插入时间',
      PRIMARY KEY (`id`) USING BTREE,
      KEY `type` (`type`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4

