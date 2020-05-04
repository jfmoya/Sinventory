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

-- Dump completed on 2020-05-04  0:36:26
