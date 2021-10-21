-- MySQL dump 10.13  Distrib 8.0.26, for macos11.3 (x86_64)
--
-- Host: 127.0.0.1    Database: sgdb_51pwn
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ip2domain`
--

DROP TABLE IF EXISTS `ip2domain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip2domain` (
  `id1` varchar(100) NOT NULL,
  `id2` varchar(100) NOT NULL,
  KEY `NewTable_id1_IDX` (`id1`) USING BTREE,
  KEY `NewTable_id2_IDX` (`id2`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip2domain`
--

LOCK TABLES `ip2domain` WRITE;
/*!40000 ALTER TABLE `ip2domain` DISABLE KEYS */;
INSERT INTO `ip2domain` VALUES ('40.77.226.250','asimov.vortex.data.trafficmanager.net'),('199.180.115.7','51pwn.com'),('192.29.37.173','dc.oracleinfinity.io'),('120.253.253.98','clientservices.googleapis.com'),('17.57.145.171','0-courier.push.apple.com'),('17.57.145.165','0-courier.push.apple.com'),('17.57.145.172','0-courier.push.apple.com'),('17.57.145.168','0-courier.push.apple.com'),('17.57.145.167','0-courier.push.apple.com'),('17.57.145.166','0-courier.push.apple.com'),('17.57.145.164','0-courier.push.apple.com'),('17.57.145.170','0-courier.push.apple.com'),('13.107.13.93','default.exp-tas.com'),('17.253.84.253','time.asia.apple.com'),('17.253.84.251','time.asia.apple.com'),('17.253.116.253','time.asia.apple.com'),('180.222.102.199','apple-finance.query.yahoo.com'),('87.248.100.168','apple-finance.query.yahoo.com'),('67.195.204.56','apple-finance.query.yahoo.com'),('106.10.236.72','apple-finance.query.yahoo.com'),('67.195.228.56','apple-finance.query.yahoo.com'),('17.253.123.201','stocks-data-service.lb-apple.com.akadns.net'),('17.253.123.202','stocks-data-service.lb-apple.com.akadns.net'),('17.253.123.201','world-gen.g.aaplimg.com'),('17.253.123.202','world-gen.g.aaplimg.com'),('52.33.186.161','api.segment.io'),('35.155.235.224','api.segment.io'),('52.39.141.123','api.segment.io'),('54.244.34.193','api.segment.io'),('44.227.101.141','api.segment.io'),('54.70.109.173','api.segment.io'),('52.25.204.187','api.segment.io'),('54.213.130.70','api.segment.io'),('34.235.177.25','api.tabnine.com'),('3.213.215.227','api.tabnine.com'),('17.57.145.169','37-courier.push.apple.com'),('17.57.145.164','37-courier.push.apple.com'),('17.57.145.165','37-courier.push.apple.com'),('17.57.145.167','37-courier.push.apple.com'),('17.57.145.166','37-courier.push.apple.com'),('17.57.145.170','37-courier.push.apple.com'),('17.57.145.168','37-courier.push.apple.com'),('17.57.145.171','37-courier.push.apple.com'),('17.57.145.171','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.172','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.166','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.164','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.165','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.168','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.169','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.167','apac-china-courier-4.push-apple.com.akadns.net'),('52.225.255.33','ecs.office.com'),('40.77.226.250','vortex.data.microsoft.com'),('13.107.13.93','deault-exp-tas-com.e-0014.e-msedge.net'),('117.175.91.35','fanyiapp.cdn.bcebos.com'),('2409:8c62:410:5::75af:5b23','fanyiapp.cdn.bcebos.com'),('2409:8c62:410:5::75af:5b23','feedfreev6.jomodns.com'),('17.57.145.168','8.courier-push-apple.com.akadns.net'),('17.57.145.171','8.courier-push-apple.com.akadns.net'),('17.57.145.164','8.courier-push-apple.com.akadns.net'),('17.57.145.165','8.courier-push-apple.com.akadns.net'),('17.57.145.170','8.courier-push-apple.com.akadns.net'),('17.57.145.172','8.courier-push-apple.com.akadns.net'),('17.57.145.169','8.courier-push-apple.com.akadns.net'),('17.57.145.166','8.courier-push-apple.com.akadns.net'),('120.241.186.171','safebrowsing.urlsec.qq.com'),('112.60.0.199','safebrowsing.urlsec.qq.com'),('112.60.14.187','safebrowsing.urlsec.qq.com'),('112.60.14.187','qb.ias.tencent-cloud.net'),('120.241.186.171','qb.ias.tencent-cloud.net'),('112.60.0.199','qb.ias.tencent-cloud.net'),('120.253.255.161','safebrowsing.googleapis.com'),('142.251.43.10','play.googleapis.com'),('40.77.226.250','global.vortex.data.trafficmanager.net'),('17.57.145.167','39-courier.push.apple.com'),('17.57.145.170','39-courier.push.apple.com'),('17.57.145.166','39-courier.push.apple.com'),('17.57.145.164','39-courier.push.apple.com'),('17.57.145.165','39-courier.push.apple.com'),('17.57.145.168','39-courier.push.apple.com'),('17.57.145.171','39-courier.push.apple.com'),('17.57.145.172','39-courier.push.apple.com'),('17.57.145.149','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.150','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.148','apac-china-courier-4.push-apple.com.akadns.net'),('117.18.232.200','az764295.vo.msecnd.net'),('117.18.232.200','cs22.wpc.v0cdn.net'),('140.82.112.25','alive.github.com'),('67.195.228.56','geo-applefinance-cache.internal.query.g03.yahoodns.net'),('183.230.78.187','init-p01md.apple.com'),('20.205.243.160','ssh.github.com'),('221.182.23.197','ocsp2-lb.apple.com.akadns.net'),('183.230.78.187','ocsp2-lb.apple.com.akadns.net'),('17.57.145.165','41-courier.push.apple.com'),('17.57.145.167','41-courier.push.apple.com'),('17.57.145.170','41-courier.push.apple.com'),('17.57.145.172','41-courier.push.apple.com'),('17.57.145.168','41-courier.push.apple.com'),('17.57.145.164','41-courier.push.apple.com'),('17.57.145.171','41-courier.push.apple.com'),('17.57.145.166','41-courier.push.apple.com'),('17.57.145.133','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.136','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.132','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.135','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.137','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.138','apac-china-courier-4.push-apple.com.akadns.net'),('17.57.145.134','apac-china-courier-4.push-apple.com.akadns.net');
/*!40000 ALTER TABLE `ip2domain` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-21 13:57:45
