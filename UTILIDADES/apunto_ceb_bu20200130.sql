-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 192.168.100.20    Database: apunto_ceb
-- ------------------------------------------------------
-- Server version	5.7.28-log

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
-- Table structure for table `centro_acopio`
--

DROP TABLE IF EXISTS `centro_acopio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `centro_acopio` (
  `cac_codigo` smallint(4) NOT NULL,
  `cac_nombre` varchar(45) DEFAULT NULL,
  `cac_ruc` bigint(13) unsigned zerofill DEFAULT NULL,
  `cac_coord` point DEFAULT NULL,
  `cac_correo` varchar(45) DEFAULT NULL,
  `cac_telf` varchar(45) DEFAULT NULL,
  `cac_direccion` varchar(60) DEFAULT NULL,
  `cac_fecreg` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cac_estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`cac_codigo`),
  UNIQUE KEY `cac_ruc_UNIQUE` (`cac_ruc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `centro_acopio`
--

LOCK TABLES `centro_acopio` WRITE;
/*!40000 ALTER TABLE `centro_acopio` DISABLE KEYS */;
INSERT INTO `centro_acopio` VALUES (1000,'COMUNA LOTE 3',1792826548001,_binary '\0\0\0\0\0\0\0ù>LWπø\√\‚&Y=ãS¿','lote3@elordeno.ec','0996665552','Lote 3','2020-01-25 02:23:16',1);
/*!40000 ALTER TABLE `centro_acopio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operador`
--

DROP TABLE IF EXISTS `operador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operador` (
  `ope_codigo` smallint(3) NOT NULL,
  `ope_nombre` varchar(45) DEFAULT NULL,
  `ope_cedula` bigint(10) unsigned zerofill NOT NULL,
  `cac_codigo` smallint(4) NOT NULL,
  `ope_clave` smallint(4) DEFAULT NULL,
  `ope_estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ope_codigo`),
  UNIQUE KEY `ope_cedula_UNIQUE` (`ope_cedula`),
  KEY `cac_codigo_idx` (`cac_codigo`),
  CONSTRAINT `cac_codigo_1` FOREIGN KEY (`cac_codigo`) REFERENCES `centro_acopio` (`cac_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operador`
--

LOCK TABLES `operador` WRITE;
/*!40000 ALTER TABLE `operador` DISABLE KEYS */;
INSERT INTO `operador` VALUES (711,'Moya Dobronski JuanFernando',1710217520,1000,0,1);
/*!40000 ALTER TABLE `operador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `prd_codigo` varchar(6) NOT NULL,
  `prd_nombre` varchar(45) DEFAULT NULL,
  `prd_preciokg` decimal(8,4) DEFAULT NULL,
  `prd_taragaveta` decimal(6,3) DEFAULT NULL,
  `prd_merma` decimal(4,3) DEFAULT '0.000',
  `prd_estado` tinyint(1) DEFAULT NULL,
  `prd_sap` varchar(45) DEFAULT NULL,
  `prd_ fecreg` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ope_codigo` smallint(3) DEFAULT NULL,
  PRIMARY KEY (`prd_codigo`),
  KEY `ope_codigo_idx` (`ope_codigo`),
  CONSTRAINT `ope_codigo_2` FOREIGN KEY (`ope_codigo`) REFERENCES `operador` (`ope_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES ('100001','Cebolla Blanca Larga',1.5738,1.478,0.072,1,'100100001','2020-01-31 01:55:56',711);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `pro_codigo` smallint(3) NOT NULL,
  `pro_cacreg` smallint(4) NOT NULL,
  `pro_cedula` bigint(10) unsigned zerofill DEFAULT NULL,
  `pro_nombre` varchar(45) DEFAULT NULL,
  `pro_ruc` bigint(13) unsigned zerofill DEFAULT NULL,
  `pro_fecnac` date DEFAULT NULL,
  `pro_genero` char(1) DEFAULT NULL,
  `pro_fecreg` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `pro_estado` tinyint(1) DEFAULT NULL,
  `pro_sap` varchar(45) DEFAULT NULL,
  `ope_codigo` smallint(3) DEFAULT NULL,
  PRIMARY KEY (`pro_codigo`,`pro_cacreg`),
  UNIQUE KEY `pro_cedula_UNIQUE` (`pro_cedula`),
  UNIQUE KEY `pro_ruc_UNIQUE` (`pro_ruc`),
  KEY `ope_codigo_idx` (`ope_codigo`),
  CONSTRAINT `ope_codigo_1` FOREIGN KEY (`ope_codigo`) REFERENCES `operador` (`ope_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (29,1000,1714852801,'Catucuamba Andrango Ernestina',1714852801001,'1950-01-12','F','2020-01-13 02:01:07',1,'100000029',711),(39,1000,1720988524,'Catucuamba Tuquerres Luis Alejandro',1720988524001,'1987-01-15','M','2020-01-13 01:37:37',1,'100000039',711),(43,1000,1786596182,'Colimba Lech√≥n Mar√≠a Laste√±a',1786596182001,'1959-09-07','F','2020-01-13 02:01:07',1,'100000043',711),(49,1000,1737175677,'Andrango Tabango Laura',1737175677001,'1966-01-14','F','2020-01-13 02:01:07',1,'100000049',711),(51,1000,1767579550,'Cholca Andrango Aparicio',1767579550001,'1962-04-02','M','2020-01-13 02:01:07',1,'100000051',711),(56,1000,1735095696,'Neppas Nepas Jorge Ren√©',1735095696001,'1995-10-01','M','2020-01-13 02:01:07',1,'100000056',711),(68,1000,1705425263,'Escola Quilo Mar√≠a Lucrecia',1705425263001,'1994-08-30','F','2020-01-13 01:37:38',1,'100000068',711),(80,1000,1787129324,'Lech√≥n Campu√©s Luis Hern√°n',1787129324001,'1959-04-09','M','2020-01-13 02:01:07',1,'100000080',711),(86,1000,1703288739,'Necpas Alba Joel Gonzalo',1703288739001,'1991-01-02','M','2020-01-13 01:37:38',1,'100000086',711),(91,1000,1728658038,'Necpas Campu√©s Jaime Rodrigo',1728658038001,'1959-05-02','M','2020-01-13 01:37:38',1,'100000091',711),(100,1000,0910200681,'Neppas Nepas Ana Luisa',0910200681001,'1951-02-20','F','2020-01-13 02:01:07',1,'100000100',711),(134,1000,1703028686,'Nepas Guatemal Jorge Alfonso',1703028686001,'1993-09-16','M','2020-01-13 01:37:38',1,'100000134',711),(145,1000,1748428542,'Neppas Alba Diana Carolina',1748428542001,'1993-10-04','F','2020-01-13 02:01:07',1,'100000145',711),(179,1000,1786266393,'Quilo Colcha Luis Vinicio',1786266393001,'1964-12-30','M','2020-01-13 02:01:07',1,'100000179',711),(182,1000,1713526500,'Colimba Andrango Juan Carlos',1713526500001,'1981-11-29','M','2020-01-13 01:37:38',1,'100000182',711),(260,1000,1796869712,'Cholca Colimba Elisabeth Rocio',1796869712001,'1988-07-29','F','2020-01-13 02:01:07',1,'100000260',711);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaccion` (
  `tra_codigo` int(8) NOT NULL AUTO_INCREMENT,
  `pro_codigo` smallint(3) DEFAULT NULL,
  `pro_cacreg` smallint(4) DEFAULT NULL,
  `cac_codigo` smallint(4) DEFAULT NULL,
  `prd_codigo` varchar(6) DEFAULT NULL,
  `tra_fecreg` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `tra_pesobruto` decimal(6,2) DEFAULT NULL,
  `tra_merma` decimal(6,2) DEFAULT NULL,
  `tra_numgavetas` smallint(3) DEFAULT NULL,
  `tra_tara` decimal(6,2) DEFAULT NULL,
  `tra_pesoneto` decimal(6,2) DEFAULT NULL,
  `tra_valor` decimal(7,4) DEFAULT NULL,
  `tra_estado` tinyint(1) DEFAULT NULL,
  `tra_fecmod` timestamp NULL DEFAULT NULL,
  `tra_liquidado` tinyint(1) DEFAULT NULL,
  `tra_visual` tinyint(1) DEFAULT NULL,
  `tra_insectos` tinyint(1) DEFAULT NULL,
  `tra_limpieza` tinyint(1) DEFAULT NULL,
  `tra_aceptado` tinyint(1) DEFAULT NULL,
  `ope_codigo` smallint(3) DEFAULT NULL,
  PRIMARY KEY (`tra_codigo`),
  KEY `pro_codigo_cacreg_idx` (`pro_codigo`,`pro_cacreg`),
  KEY `cac_codigo_2_idx` (`cac_codigo`),
  KEY `prd_codigo_1_idx` (`prd_codigo`),
  KEY `ope_codigo_3_idx` (`ope_codigo`),
  CONSTRAINT `cac_codigo_2` FOREIGN KEY (`cac_codigo`) REFERENCES `centro_acopio` (`cac_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ope_codigo_3` FOREIGN KEY (`ope_codigo`) REFERENCES `operador` (`ope_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `prd_codigo_1` FOREIGN KEY (`prd_codigo`) REFERENCES `producto` (`prd_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `pro_codigo_cacreg_1` FOREIGN KEY (`pro_codigo`, `pro_cacreg`) REFERENCES `proveedor` (`pro_codigo`, `pro_cacreg`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
INSERT INTO `transaccion` VALUES (1,80,1000,1000,'100001','2020-01-22 00:32:50',10.00,NULL,2,3.86,6.14,9.6631,1,NULL,0,1,1,1,1,711),(2,56,1000,1000,'100001','2020-01-22 03:47:48',10.00,NULL,2,5.79,4.21,6.6257,1,NULL,0,1,1,1,1,711),(3,134,1000,1000,'100001','2020-01-22 03:49:24',21.00,NULL,2,9.65,11.35,17.8626,1,NULL,0,1,1,1,1,711),(4,39,1000,1000,'100001','2020-01-23 15:40:42',10.00,NULL,2,3.86,6.14,9.6631,1,NULL,0,1,1,1,1,711),(5,39,1000,1000,'100001','2020-01-23 18:02:05',10.00,NULL,2,5.79,4.21,6.6257,1,NULL,0,1,1,1,1,711),(6,91,1000,1000,'100001','2020-01-23 18:21:34',10.00,NULL,2,5.79,4.21,6.6257,1,NULL,0,1,1,1,1,711),(7,260,1000,1000,'100001','2020-01-23 18:22:54',10.00,NULL,2,7.72,2.28,3.5883,1,NULL,0,1,1,1,1,711),(8,260,1000,1000,'100001','2020-01-23 18:27:51',21.00,NULL,2,1.93,19.07,30.0124,1,NULL,0,1,1,1,1,711),(9,260,1000,1000,'100001','2020-01-23 18:32:08',32.00,NULL,2,11.58,20.42,32.1370,1,NULL,0,1,1,1,1,711),(10,260,1000,1000,'100001','2020-01-23 18:37:30',21.00,NULL,2,13.51,7.49,11.7878,1,NULL,0,1,1,1,1,711),(11,43,1000,1000,'100001','2020-01-23 18:48:24',43.00,NULL,5,9.65,33.35,52.4862,1,NULL,0,1,1,1,1,711),(12,145,1000,1000,'100001','2020-01-23 19:39:16',26.50,NULL,2,3.86,22.64,35.6308,1,NULL,0,1,1,1,1,711),(13,86,1000,1000,'100001','2020-01-23 20:13:15',10.00,NULL,1,1.93,8.07,12.7006,1,NULL,0,1,1,1,1,711),(14,182,1000,1000,'100001','2020-01-23 20:18:05',37.50,NULL,5,9.65,27.85,43.8303,1,NULL,0,1,1,1,1,711),(15,80,1000,1000,'100001','2020-01-23 20:19:28',26.50,NULL,8,15.44,11.06,17.4062,1,NULL,0,1,1,1,1,711),(16,43,1000,1000,'100001','2020-01-23 20:19:57',10.00,NULL,1,1.93,8.07,12.7006,1,NULL,0,1,1,1,1,711),(17,179,1000,1000,'100001','2020-01-23 20:20:25',10.00,NULL,3,5.79,4.21,6.6257,1,NULL,0,1,1,1,1,711),(18,51,1000,1000,'100001','2020-01-23 20:21:01',26.50,NULL,4,7.72,18.78,29.5560,1,NULL,0,1,1,1,1,711),(19,134,1000,1000,'100001','2020-01-23 20:21:20',10.00,NULL,1,1.93,8.07,12.7006,1,NULL,0,1,1,1,1,711),(20,68,1000,1000,'100001','2020-01-23 20:29:37',54.00,NULL,3,5.79,48.21,75.8729,1,NULL,0,1,1,1,1,711),(21,91,1000,1000,'100001','2020-01-23 20:39:48',10.00,NULL,1,1.93,8.07,12.7006,1,NULL,0,1,1,1,1,711),(22,260,1000,1000,'100001','2020-01-23 20:45:28',10.00,NULL,1,1.93,8.07,12.7006,1,NULL,0,1,1,1,1,711),(23,39,1000,1000,'100001','2020-01-23 20:46:46',32.00,NULL,3,5.79,26.21,41.2493,1,NULL,0,1,1,1,1,711),(24,91,1000,1000,'100001','2020-01-24 14:02:14',5.90,NULL,1,1.93,3.97,6.2480,1,NULL,0,1,1,1,1,711),(25,260,1000,1000,'100001','2020-01-24 14:03:39',49.58,NULL,7,13.51,36.07,56.7670,1,NULL,0,1,1,1,1,711),(26,179,1000,1000,'100001','2020-01-24 14:04:40',111.93,NULL,3,5.79,106.14,167.0431,1,NULL,0,1,1,1,1,711),(27,39,1000,1000,'100001','2020-01-24 23:56:34',8.31,NULL,1,1.93,6.38,10.0408,1,NULL,0,1,1,1,1,711),(28,91,1000,1000,'100001','2020-01-25 00:00:17',8.62,NULL,2,3.86,4.76,7.4913,1,NULL,0,1,1,1,1,711),(29,91,1000,1000,'100001','2020-01-25 00:01:54',9.07,NULL,1,1.93,7.14,11.2369,1,NULL,0,1,1,1,1,711),(30,91,1000,1000,'100001','2020-01-25 00:03:58',8.73,NULL,1,1.93,6.80,10.7018,1,NULL,0,1,1,1,1,711),(31,91,1000,1000,'100001','2020-01-25 00:07:22',13.92,NULL,1,1.93,11.99,18.8699,1,NULL,0,1,1,1,1,711),(32,39,1000,1000,'100001','2020-01-25 00:56:14',5.20,NULL,1,1.93,3.27,5.1463,1,NULL,0,1,1,1,1,711),(33,179,1000,1000,'100001','2020-01-25 00:56:59',5.01,NULL,1,1.93,3.08,4.8473,1,NULL,0,1,1,1,1,711),(34,91,1000,1000,'100001','2020-01-25 00:58:17',7.73,NULL,1,1.93,5.80,9.1280,1,NULL,0,1,1,1,1,711),(35,39,1000,1000,'100001','2020-01-25 00:59:36',9.84,NULL,1,1.93,7.91,12.4488,1,NULL,0,1,1,1,1,711),(36,91,1000,1000,'100001','2020-01-25 01:12:20',5.61,NULL,1,1.93,3.68,5.7916,1,NULL,0,1,1,1,1,711),(37,91,1000,1000,'100001','2020-01-25 01:38:17',6.17,NULL,1,1.93,4.24,6.6700,1,NULL,0,1,1,1,1,711),(38,91,1000,1000,'100001','2020-01-25 23:50:12',9.61,NULL,3,5.79,3.82,6.0100,1,NULL,0,1,1,1,1,711),(39,39,1000,1000,'100001','2020-01-25 23:51:12',62.35,NULL,3,5.79,56.56,89.0100,1,NULL,0,1,1,1,1,711),(40,39,1000,1000,'100001','2020-01-25 23:52:04',111.66,NULL,3,5.79,105.87,166.6200,1,NULL,0,1,1,1,1,711),(41,39,1000,1000,'100001','2020-01-25 23:54:12',10.24,NULL,1,1.93,8.31,13.0800,1,NULL,0,1,1,1,1,711),(42,91,1000,1000,'100001','2020-01-26 00:08:07',8.78,NULL,3,5.79,2.99,4.7100,1,NULL,0,1,1,1,1,711),(43,91,1000,1000,'100001','2020-01-26 00:18:34',13.65,NULL,1,1.93,11.72,18.4400,1,NULL,0,1,1,1,1,711),(44,91,1000,1000,'100001','2020-01-28 06:40:47',6.12,NULL,1,1.93,4.19,6.5900,1,NULL,0,1,1,1,1,711),(45,91,1000,1000,'100001','2020-01-28 07:08:14',0.00,NULL,1,1.93,-1.93,-3.0400,1,NULL,0,1,1,1,1,711),(46,91,1000,1000,'100001','2020-01-31 02:59:47',10.00,NULL,1,1.48,8.52,13.4100,1,NULL,0,1,1,1,1,711),(47,91,1000,1000,'100001','2020-01-31 03:27:22',10.00,0.61,1,1.48,7.91,12.4500,1,NULL,0,1,1,1,1,711),(48,39,1000,1000,'100001','2020-01-31 03:29:02',26.50,1.80,1,1.48,23.22,36.5400,1,NULL,0,1,1,1,1,711),(49,91,1000,1000,'100001','2020-01-31 03:37:29',48.50,3.28,2,2.96,42.26,66.5200,1,NULL,0,1,1,1,1,711),(50,91,1000,1000,'100001','2020-01-31 03:42:27',65.00,4.36,3,4.43,56.21,88.4600,1,NULL,0,1,1,1,1,711),(51,91,1000,1000,'100001','2020-01-31 03:54:12',26.50,1.70,2,2.96,21.85,34.3900,1,NULL,0,1,1,1,1,711),(52,91,1000,1000,'100001','2020-01-31 03:55:48',10.00,0.61,1,1.48,7.91,12.4500,1,NULL,0,1,1,1,1,711),(53,39,1000,1000,'100001','2020-01-31 03:56:28',37.50,1.10,15,22.17,14.23,22.3900,1,NULL,0,1,1,1,1,711),(54,91,1000,1000,'100001','2020-01-31 04:01:34',10.00,0.61,1,1.48,7.91,12.4500,1,NULL,0,1,1,1,1,711),(55,39,1000,1000,'100001','2020-01-31 04:02:23',15.50,0.90,2,2.96,11.64,18.3200,1,NULL,0,1,1,1,1,711);
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'apunto_ceb'
--
/*!50003 DROP FUNCTION IF EXISTS `last_monday` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`jfmoya`@`%` FUNCTION `last_monday`() RETURNS datetime
RETURN DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY) ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-30 23:32:04
