-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: dblocal    Database: src_spider
-- ------------------------------------------------------
-- Server version	5.5.38-0+wheezy1-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `spider_site`
--

DROP TABLE IF EXISTS `spider_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spider_site`
--

LOCK TABLES `spider_site` WRITE;
/*!40000 ALTER TABLE `spider_site` DISABLE KEYS */;
/*INSERT INTO `spider_site` VALUES (6,'财联社','www\\.cailianpress\\.com','https://www.cailianpress.com/','http://www.cailianpress.com/',3,'Cailianpress1','cailianpress1','20,21600,82800,2',1),(4,'华尔街见闻','wallstreetcn\\.com','http://live.wallstreetcn.com/?cid[]=2','http://live.wallstreetcn.com/?cid[]=2',3,'Wallstreetcn1','wallstreetcn1',NULL,1),(5,'证券时报网','kuaixun\\.stcn\\.com','http://kuaixun.stcn.com/finance/internal/','http://kuaixun.stcn.com/finance/internal/',5,'Stcn1','stcn1',NULL,1),(1,'金融界','stock\\.jrj\\.com\\.cn','http://stock.jrj.com.cn/hotstock/gnjj.shtml','http://stock.jrj.com.cn/hotstock/gnjj.shtml',10,'Jrj1','jrj1',NULL,1),(3,'财联社','www\\.cailianpress\\.com','https://www.cailianpress.com/subject.html','http://www.cailianpress.com/subject.html',10,'Cailianpress3','cailianpress1','70,21600,82800,4',-10),(12,'新浪财经','finance\\.sina\\.com\\.cn','http://live.sina.com.cn/zt/f/v/finance/globalnews1?tag=2','http://live.sina.com.cn/zt/f/v/finance/globalnews1?tag=2',2,'Sina1','sina2',NULL,-1),(13,'同花顺','\\.10jqka\\.com\\.cn','http://comment.10jqka.com.cn/api/realtime.php?block=getnews','http://news.10jqka.com.cn/realtimenews.html',2,NULL,'tjqka1',NULL,-1),(17,'东方财富网','finance\\.eastmoney\\.com','http://kuaixun.eastmoney.com/','http://kuaixun.eastmoney.com/',2,'Eastmoney2','eastmoney1',NULL,1),(34,'证券时报网','kuaixun\\.stcn\\.com','http://kuaixun.stcn.com/finance/tzjh/','http://kuaixun.stcn.com/finance/tzjh/',15,'Stcn1','stcn1',NULL,1),(29,'全景网','www\\.p5w\\.net','http://www.p5w.net/stock/market/gng/','http://www.p5w.net/stock/market/gng/',5,NULL,NULL,NULL,-1),(28,'网易财经','money\\.163\\.com','http://money.163.com/special/00251LJV/hyyj.html','http://money.163.com/special/00251LJV/hyyj.html',4,NULL,NULL,NULL,-1),(26,'证券时报网','kuaixun\\.stcn\\.com','http://kuaixun.stcn.com/index.shtml','http://kuaixun.stcn.com/index.shtml',3,'Stcn2','stcn1',NULL,1),(24,'凤凰网','finance\\.ifeng\\.com','http://finance.ifeng.com/stock/zqyw/index.shtml','http://finance.ifeng.com/stock/zqyw/index.shtml',3,'Ifeng1','ifeng1',NULL,1),(23,'腾讯证券','stock\\.qq\\.com','http://stock.qq.com/l/stock/bk/list2015042315658.htm','http://stock.qq.com/l/stock/bk/list2015042315658.htm',3,NULL,NULL,NULL,-1),(22,'中国证券网','news\\.cnstock\\.com','http://news.cnstock.com/industry/sid_cyqb/','http://news.cnstock.com/industry/sid_cyqb/',4,NULL,'cnstock1',NULL,-1),(20,'同花顺','field\\.10jqka\\.com\\.cn','http://news.10jqka.com.cn/cjkx_list/','http://news.10jqka.com.cn/cjkx_list/',2,'Tjqka1','tjqka1',NULL,1),(19,'老钱庄','stock\\.laoqianzhuang\\.com','http://stock.laoqianzhuang.com/redianticai/','http://stock.laoqianzhuang.com/redianticai/',3,'Laoqianzhuang1','laoqianzhuang1',NULL,1),(18,'中证网','www\\.cs\\.com\\.cn','http://www.cs.com.cn/ssgs/hyzx/','http://www.cs.com.cn/ssgs/hyzx/',3,'Cs1','cs1',NULL,1),(16,'证券之星','stock\\.stockstar\\.com','http://stock.stockstar.com/list/sectors.htm','http://stock.stockstar.com/list/sectors.htm',2,'Stockstar1','stockstar1',NULL,1),(15,'同花顺','yuanchuang\\.10jqka\\.com\\.cn','http://yuanchuang.10jqka.com.cn/jhqb_list/','http://yuanchuang.10jqka.com.cn/jhqb_list/',3,'Tjqka2','tjqka1','70,21600,82800,4',1),(14,'阿思达克财经网','aastocks\\.com','http://aastocks.com/sc/stocks/analysis/china-hot-topic.aspx?catg=1','http://aastocks.com/sc/stocks/analysis/china-hot-topic.aspx?catg=1',1,NULL,NULL,NULL,-1),(11,'东方财富网','stock\\.eastmoney\\.com','http://stock.eastmoney.com/news/cbkjj.html','http://stock.eastmoney.com/news/cbkjj.html',5,'Eastmoney1','eastmoney1',NULL,1),(10,'中国证券网','\\.cnstock\\.com','http://news.cnstock.com/bwsd/index.html','http://news.cnstock.com/bwsd/',5,'Cnstock2','cnstock1',NULL,1),(9,'证券日报网','www\\.ccstock\\.cn','http://www.ccstock.cn/stock/redian/index.html','http://www.ccstock.cn/stock/redian/index.html',5,'Ccstock1','ccstock1',NULL,1),(8,'中国证券网','news\\.cnstock\\.com','http://news.cnstock.com/industry/sid_rdjj/','http://news.cnstock.com/industry/sid_rdjj/',4,'Cnstock1','cnstock1',NULL,1),(7,'中证网','www\\.cs\\.com\\.cn','http://www.cs.com.cn/sylm/cstop10/','http://www.cs.com.cn/sylm/cstop10/',3,NULL,NULL,NULL,-1),(2,'财联社','www\\.cailianpress\\.com','http://www.cailianpress.com/reference','http://www.cailianpress.com/reference',5,'Cailianpress2','cailianpress1','80,25200,28800,5',1),(30,'中国金融信息网','stock\\.xinhua08\\.com','http://stock.xinhua08.com/hydt/','http://stock.xinhua08.com/hydt/',3,'Xinhua081','xinhua081',NULL,1),(31,'丰华财经','stock\\.jfinfo\\.com','http://stock.jfinfo.com/tzfxb/','http://stock.jfinfo.com/tzfxb/',3,'Jfinfo1','jfinfo1',NULL,-2),(32,'中金在线','sc\\.stock\\.cnfol\\.com','http://sc.stock.cnfol.com/shichangjuejin/','http://sc.stock.cnfol.com/shichangjuejin/',5,'Cnfol1','cnfol2',NULL,1),(33,'同花顺','stock\\.10jqka.com\\.cn','http://stock.10jqka.com.cn/tzjh_list/','http://stock.10jqka.com.cn/tzjh_list/',2,'Tjqka2','tjqka1',NULL,1),(35,'中财网','industry\\.cfi\\.cn','http://industry.cfi.cn/BCA0A4127A4128A4144.html','http://industry.cfi.cn/BCA0A4127A4128A4144.html',4,'Cfi1','cfi1',NULL,1),(36,'慧博投研资讯','www\\.microbell\\.com','http://www.microbell.com/microns_2.html','http://www.microbell.com/microns_2.html',3,NULL,NULL,NULL,-1),(37,'中国财经','finance\\.china\\.com\\.cn','http://finance.china.com.cn/stock/bkjj/index.shtml','http://finance.china.com.cn/stock/bkjj/index.shtml',4,'China1','china1',NULL,1),(21,'第一财经','\\.yicai\\.com','http://m.yicai.com/ajax/hour/0/10/1','http://m.yicai.com/brief/',2,'Yicai1','yicai1',NULL,-1),(38,'选股宝','xuangubao\\.cn','https://xuangubao.cn/zhutiku','https://xuangubao.cn/zhutiku',10,'Xuangubao1','xuangubao1',NULL,1),(39,'财联社','www\\.cailianpress\\.com','https://www.cailianpress.com/theme','https://www.cailianpress.com/theme',10,'Cailianpress4','cailianpress1','',1),(40,'中国证券网','news\\.cnstock\\.com','http://app.cnstock.com/api/theme/get_theme_list?size=5','http://news.cnstock.com/theme/index.html',15,'Cnstock3','cnstock1',NULL,1),(41,'同花顺','stock\\.10jqka\\.com\\.cn','http://m.10jqka.com.cn/wapapi/HotTheme/getHotNews/limit/10','http://yuanchuang.10jqka.com.cn/qingbao/',5,'Tjqka3','tjqka1',NULL,1),(42,'选股宝','xuangubao\\.cn','https://xuangubao.cn/','https://xuangubao.cn/',5,'Xuangubao2','xuangubao1',NULL,1),(25,'和讯','stock\\.hexun\\.com','http://myapp.hexun.com/roll/rollAction_list.action?callback=hxbase_json{timestamp_ms}newsScroll','http://stock.hexun.com/shikuang/',3,NULL,NULL,NULL,-3),(27,'网易','money\\.163\\.com','http://data.live.126.net/liveAll/83946.json?callback=alldata','http://money.163.com/special/stock{date_Ymd}/',3,NULL,NULL,NULL,-3);*/
/*!40000 ALTER TABLE `spider_site` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-23 15:15:05
