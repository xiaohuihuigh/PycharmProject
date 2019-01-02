
LOCK TABLES `spider_site` WRITE;
/*!40000 ALTER TABLE `spider_site` DISABLE KEYS */;
INSERT INTO `spider_site` VALUES (6,'财联社','www\\.cailianpress\\.com','https://www.cailianpress.com/','http://www.cailianpress.com/',3,'Cailianpress1','cailianpress1','20,21600,82800,2',1),(27,'网易','money\\.163\\.com','http://data.live.126.net/liveAll/83946.json?callback=alldata','http://money.163.com/special/stock{date_Ymd}/',3,NULL,NULL,NULL,-3);
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
