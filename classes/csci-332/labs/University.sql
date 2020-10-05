-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: college
-- ------------------------------------------------------
-- Server version	5.5.5-10.2.17-MariaDB

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
-- Table structure for table `class`
--
CREATE DATABASE IF NOT EXISTS university;
USE university;

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `CID` char(7) NOT NULL,
  `FID` char(4) DEFAULT NULL,
  `SCHED` varchar(15) DEFAULT NULL,
  `ROOM` char(4) DEFAULT NULL,
  PRIMARY KEY (`CID`),
  KEY `FID` (`FID`),
  CONSTRAINT `class_ibfk_1` FOREIGN KEY (`FID`) REFERENCES `faculty` (`FID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES ('ART103A','F101','MWF9','H221'),('CSC201A','F105','TUTH10','M110'),('CSC203A','F105','MTHF12','M110'),('HST205A','F202','MWF11','H221'),('MTH101B','F110','MTUTH9','H225'),('MTH103C','F110','MWF11','H225');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enroll`
--

DROP TABLE IF EXISTS `enroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enroll` (
  `COURSENO` char(7) NOT NULL,
  `STID` char(5) NOT NULL,
  `GRADE` char(2) DEFAULT NULL,
  PRIMARY KEY (`COURSENO`,`STID`),
  KEY `STID` (`STID`),
  CONSTRAINT `enroll_ibfk_1` FOREIGN KEY (`STID`) REFERENCES `student` (`STID`),
  CONSTRAINT `enroll_ibfk_2` FOREIGN KEY (`COURSENO`) REFERENCES `class` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enroll`
--

LOCK TABLES `enroll` WRITE;
/*!40000 ALTER TABLE `enroll` DISABLE KEYS */;
INSERT INTO `enroll` VALUES ('ART103A','S1001','A'),('ART103A','S1002','D'),('ART103A','S1010',NULL),('CSC201A','S1002','F'),('CSC201A','S1020','B'),('HST205A','S1001','C'),('MTH101B','S1020','A'),('MTH103C','S1002','B'),('MTH103C','S1010',NULL);
/*!40000 ALTER TABLE `enroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faculty` (
  `FID` char(4) NOT NULL,
  `FACNAME` varchar(20) DEFAULT NULL,
  `DEPT` varchar(15) DEFAULT NULL,
  `RANK` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`FID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES ('F101','Adams','Art','Professor'),('F105','Tanaka','CSC','Instructor'),('F110','Byrne','Math','Assistant'),('F202','Smith','History','Associate'),('F221','Smith','CSC','Professor');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `STID` char(5) NOT NULL,
  `STNAME` varchar(20) DEFAULT NULL,
  `MAJOR` varchar(15) DEFAULT NULL,
  `CREDITS` int(11) DEFAULT NULL,
  PRIMARY KEY (`STID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('S1001','Smith, Tom','History',90),('S1002','Chin, Ann','Math',36),('S1010','Burns, Edward','Art',63),('S1013','McCarthy, Owen','Math',9),('S1015','Jones, Mary','Math',42),('S1020','Rivera, Jane','CSC',15);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'college'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-01 10:44:42
