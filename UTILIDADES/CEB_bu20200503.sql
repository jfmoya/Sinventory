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
INSERT INTO `centro_acopio` VALUES (1000,'COMUNA LOTE 3',1234567890001,_binary '\0\0\0\0\0\0\0z6�>�S�\���N]��','','','','2020-05-04 04:34:17',1);
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
INSERT INTO `producto` VALUES ('100001','Cebolla Blanca Larga',0.4200,1.475,0.000,1,'100100001','2020-05-04 04:29:11',711);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `pro_codigo` smallint(3) NOT NULL AUTO_INCREMENT,
  `pro_cacreg` smallint(5) NOT NULL,
  `pro_cedula` bigint(10) unsigned zerofill DEFAULT NULL,
  `pro_nombre` varchar(45) DEFAULT NULL,
  `pro_ruc` bigint(13) unsigned zerofill DEFAULT NULL,
  `pro_fecnac` date DEFAULT NULL,
  `pro_genero` char(1) DEFAULT NULL,
  `pro_direccion` varchar(50) DEFAULT NULL,
  `pro_telf` varchar(45) DEFAULT NULL,
  `pro_correo` varchar(45) DEFAULT NULL,
  `pro_fecreg` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `pro_estado` tinyint(1) DEFAULT NULL,
  `pro_sap` int(9) unsigned zerofill DEFAULT NULL,
  `ope_codigo` smallint(3) DEFAULT NULL,
  PRIMARY KEY (`pro_codigo`,`pro_cacreg`),
  UNIQUE KEY `pro_cedula_UNIQUE` (`pro_cedula`),
  UNIQUE KEY `pro_ruc_UNIQUE` (`pro_ruc`),
  UNIQUE KEY `pro_sap_UNIQUE` (`pro_sap`),
  KEY `ope_codigo_idx` (`ope_codigo`),
  CONSTRAINT `ope_codigo_1` FOREIGN KEY (`ope_codigo`) REFERENCES `operador` (`ope_codigo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,1000,1711078210,'Andrango Aules Maria Delfina',1711078210001,NULL,NULL,NULL,'0997258797','None','2020-05-04 05:50:41',NULL,100004137,NULL),(2,1000,1711803286,'Aules Aules Daniel Arturo',1711803286001,NULL,NULL,NULL,'0938323301','None','2020-05-04 05:50:41',NULL,100004142,NULL),(3,1000,1753336997,'Aules Coyago Wilmer Fabian',1753336997001,NULL,NULL,NULL,'0967822356',NULL,'2020-05-04 06:16:55',NULL,100004105,NULL),(4,1000,1714597034,'Aules Coyago Jose Carlos',1714597034001,NULL,NULL,NULL,'0988111740',NULL,'2020-05-04 06:16:55',NULL,100004145,NULL),(5,1000,1719292177,'Aules Farinango Rosa Graciela',1719292177001,NULL,NULL,NULL,'0939277103',NULL,'2020-05-04 06:16:55',NULL,100004139,NULL),(6,1000,1712952413,'Coyago Tonta Maria Gloria',1712952413001,NULL,NULL,NULL,'0988534663',NULL,'2020-05-04 06:16:55',NULL,100004146,NULL),(7,1000,1721547741,'Farinango Acero Segundo Asciencio',1721547741001,NULL,NULL,NULL,'0997743391',NULL,'2020-05-04 06:16:55',NULL,100004144,NULL),(8,1000,1718897281,'Farinango Collago Jose Virgilio',1718897281001,NULL,NULL,NULL,'0997454081',NULL,'2020-05-04 06:16:55',NULL,100004116,NULL),(9,1000,1716481575,'Farinango Coyago Juan Ramón',1716481575001,NULL,NULL,NULL,'0993671387',NULL,'2020-05-04 06:16:56',NULL,100004112,NULL),(10,1000,1754520094,'Farinango Coyago Nestor Claudio',1754520094001,NULL,NULL,NULL,'0985322572',NULL,'2020-05-04 06:16:56',NULL,100004109,NULL),(11,1000,1712952561,'Farinango Farinango Segungo Miguel',1712952561001,NULL,NULL,NULL,'',NULL,'2020-05-04 06:16:56',NULL,100004106,NULL),(12,1000,1709906414,'Farinango Farinango Concepcion',1709906414001,NULL,NULL,NULL,'0939530903',NULL,'2020-05-04 06:16:56',NULL,100004118,NULL),(13,1000,1704333481,'Farinango Pilca José Miguel',1704333481001,NULL,NULL,NULL,'0999939532',NULL,'2020-05-04 06:16:56',NULL,100004104,NULL),(14,1000,1710104728,'Farinango Tipanluisa Segundo',1710104728001,NULL,NULL,NULL,'0979797274',NULL,'2020-05-04 06:16:56',NULL,100004111,NULL),(15,1000,1720432119,'Pillajo Farinango Maria Sebastiana',1720432119001,NULL,NULL,NULL,'0991459438',NULL,'2020-05-04 06:16:56',NULL,100004143,NULL),(16,1000,1713759973,'Pillajo Farinango Rosa Carmen',1713759973001,NULL,NULL,NULL,'0988584659',NULL,'2020-05-04 06:16:56',NULL,100004141,NULL),(17,1000,1711505097,'Toapanta Aules Jose Pascual',1711505097001,NULL,NULL,NULL,'0980933701',NULL,'2020-05-04 06:16:56',NULL,100004113,NULL),(18,1000,1707474324,'Tugulinago Aules Aurora',1707474324001,NULL,NULL,NULL,'0999939532',NULL,'2020-05-04 06:16:56',NULL,100004108,NULL),(19,1000,1721163630,'Tugulinago Aules Manuel Carlos',1721163630001,NULL,NULL,NULL,'0985771156',NULL,'2020-05-04 06:16:56',NULL,100004140,NULL),(20,1000,1717857377,'Tugulinago Pilca María Narciza',1717857377001,NULL,NULL,NULL,'0994218613',NULL,'2020-05-04 06:16:56',NULL,100004107,NULL),(21,1000,1715110464,'Ulcuango Tipanluisa Segundo Esteban',1715110464001,NULL,NULL,NULL,'0968281710',NULL,'2020-05-04 06:16:56',NULL,100004114,NULL),(22,1000,1723442388,'Ulcuango Tipanluisa Rosa Verónica',1723442388001,NULL,NULL,NULL,'0968417258',NULL,'2020-05-04 06:16:56',NULL,100004115,NULL),(23,1000,1721183562,'Ulcuango Tipanluisa Segundo Ramon',1721183562001,NULL,NULL,NULL,'',NULL,'2020-05-04 06:16:56',NULL,100004117,NULL),(24,1000,1754808101,'Farinango Tontag Nancy Fabiola',1754808101001,NULL,NULL,NULL,'0982561076',NULL,'2020-05-04 05:22:48',NULL,100004291,NULL),(25,1000,1727238485,'Sopalo Andrango Edison Ramiro',1727238485001,NULL,NULL,NULL,'0993854960',NULL,'2020-05-04 05:22:49',NULL,100004293,NULL),(26,1000,1726807892,'Coyago Tipanluisa Rosa Elvira',1726807892001,NULL,NULL,NULL,'0990109690',NULL,'2020-05-04 05:22:50',NULL,100004292,NULL),(27,1000,1717577900,'Aules Andrango Maria Carmen',1717577900001,NULL,NULL,NULL,'0967075050',NULL,'2020-05-04 05:22:51',NULL,100004290,NULL),(28,1000,1752081925,'Aules Caiza Fanny Marcela',1752081925001,NULL,NULL,NULL,'0985994906',NULL,'2020-05-04 05:22:51',NULL,100004289,NULL),(29,1000,1709780074,'Farinango Coyago Antonio Feliciano',1709780074001,NULL,NULL,NULL,'0963012047',NULL,'2020-05-04 05:22:52',NULL,100004287,NULL),(30,1000,1727187617,'Sopalo Andrango Ricardo Isaias',1727187617001,NULL,NULL,NULL,'0981958601',NULL,'2020-05-04 05:23:49',NULL,NULL,NULL);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'apunto_ceb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-04  1:42:57
