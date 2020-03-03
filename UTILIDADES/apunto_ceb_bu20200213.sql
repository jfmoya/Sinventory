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
  `pro_telf` varchar(45) DEFAULT NULL,
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
INSERT INTO `proveedor` VALUES (1,1000,1711078210,'Andrango Aules Maria Delfina',NULL,NULL,NULL,'0997258797\r','2020-02-13 05:37:05',NULL,NULL,NULL),(2,1000,1711803286,'Aules Aules Daniel Arturo',NULL,NULL,NULL,'0938323301\r','2020-02-13 05:37:05',NULL,NULL,NULL),(3,1000,1753336997,'Aules Coyago Wilmer Fabian',NULL,NULL,NULL,'0967822356\r','2020-02-13 05:37:05',NULL,NULL,NULL),(4,1000,1714597034,'Aules Coyago Jose Carlos',NULL,NULL,NULL,'0988111740\r','2020-01-31 05:11:12',NULL,NULL,NULL),(5,1000,1719292177,'Aules Farinango Rosa Graciela',NULL,NULL,NULL,'0939277103\r','2020-02-13 05:37:05',NULL,NULL,NULL),(6,1000,1712952413,'Coyago Tonta Maria Gloria',NULL,NULL,NULL,'0988534663\r','2020-02-13 05:37:05',NULL,NULL,NULL),(7,1000,1721547741,'Farinango Acero Segundo Asciencio',NULL,NULL,NULL,'0997743391\r','2020-02-13 05:37:05',NULL,NULL,NULL),(8,1000,1718897281,'Farinango Collago Jose Virgilio',NULL,NULL,NULL,'0997454081\r','2020-02-13 05:37:05',NULL,NULL,NULL),(9,1000,1716481575,'Farinango Coyago Juan Ram√≥n',NULL,NULL,NULL,'0996671384\r','2020-02-13 05:37:05',NULL,NULL,NULL),(10,1000,1754520094,'Farinango Coyago Nestor Claudio',NULL,NULL,NULL,'0985322572\r','2020-02-13 05:37:05',NULL,NULL,NULL),(11,1000,1712952561,'Farinango Farinango Segungo Miguel',NULL,NULL,NULL,'\r','2020-02-13 05:37:05',NULL,NULL,NULL),(12,1000,1709906414,'Farinango Farinango Concepcion',NULL,NULL,NULL,'0939530903\r','2020-02-13 05:37:05',NULL,NULL,NULL),(13,1000,1704333481,'Farinango Pilca Jos√© Miguel',NULL,NULL,NULL,'0999939532\r','2020-01-31 05:11:12',NULL,NULL,NULL),(14,1000,1710104728,'Farinango Tipanluisa Segundo',NULL,NULL,NULL,'0979797274\r','2020-02-13 05:37:05',NULL,NULL,NULL),(15,1000,1720432119,'Pillajo Farinango Maria Sebastiana',NULL,NULL,NULL,'0991459438\r','2020-02-13 05:37:05',NULL,NULL,NULL),(16,1000,1713759973,'Pillajo Farinango Rosa Carmen',NULL,NULL,NULL,'0988584659\r','2020-02-13 05:37:05',NULL,NULL,NULL),(17,1000,1711505097,'Toapanta Aules Jose Pascual',NULL,NULL,NULL,'0980933701\r','2020-02-13 05:37:05',NULL,NULL,NULL),(18,1000,1707474324,'Tugulinago Aules Aurora',NULL,NULL,NULL,'0999939532\r','2020-01-31 05:11:12',NULL,NULL,NULL),(19,1000,1721163630,'Tugulinago Aules Manuel Carlos',NULL,NULL,NULL,'0985771156\r','2020-01-31 05:11:12',NULL,NULL,NULL),(20,1000,1717857377,'Tugulinago Pilca Mar√≠a Narciza',NULL,NULL,NULL,'0994218613\r','2020-02-13 05:37:05',NULL,NULL,NULL),(21,1000,1715110464,'Ulcuango Tipanluisa Segundo Esteban',NULL,NULL,NULL,'0968281710\r','2020-02-13 05:37:05',NULL,NULL,NULL),(22,1000,1723442388,'Ulcuango Tipanluisa Rosa Ver√≥nica',NULL,NULL,NULL,'0968417258\r','2020-02-13 05:37:05',NULL,NULL,NULL),(23,1000,1721183562,'Ulcuango Tipanluisa Segundo Ramon',NULL,NULL,NULL,'\r','2020-02-13 05:37:05',NULL,NULL,NULL);
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
/*!50003 DROP FUNCTION IF EXISTS `last_saturday` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`jfmoya`@`%` FUNCTION `last_saturday`() RETURNS datetime
RETURN IF(WEEKDAY(CURDATE()) < 5, 
		DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) + (7 - 5) DAY),
		DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) - 5 DAY)) ;;
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

-- Dump completed on 2020-02-13  2:37:54
