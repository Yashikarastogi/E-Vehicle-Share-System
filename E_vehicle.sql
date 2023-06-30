-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: coolcandy.top    Database: E-vehicle
-- ------------------------------------------------------
-- Server version	8.0.30
create DATABASE E_vehicle;
use E_vehicle;

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
-- Table structure for table `cityLocations`
--

DROP TABLE IF EXISTS `cityLocations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cityLocations` (
  `cityLocationId` int NOT NULL AUTO_INCREMENT,
  `cityLocationName` varchar(50) NOT NULL,
  `Altitude` float NOT NULL,
  `Longitude` float NOT NULL,
  PRIMARY KEY (`cityLocationId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cityLocations`
--

LOCK TABLES `cityLocations` WRITE;
/*!40000 ALTER TABLE `cityLocations` DISABLE KEYS */;
INSERT INTO `cityLocations` VALUES (1,'CityCenter',23,26),(2,'University',25,27),(3,'Riverbank',23,28);
/*!40000 ALTER TABLE `cityLocations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderStatuses`
--

DROP TABLE IF EXISTS `orderStatuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderStatuses` (
  `orderStatusId` int NOT NULL,
  `orderStatusName` varchar(50) NOT NULL,
  PRIMARY KEY (`orderStatusId`),
  UNIQUE KEY `orderStatusesID_UNIQUE` (`orderStatusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderStatuses`
--

LOCK TABLES `orderStatuses` WRITE;
/*!40000 ALTER TABLE `orderStatuses` DISABLE KEYS */;
INSERT INTO `orderStatuses` VALUES (1,'OnTheWay'),(2,'ArrivedButUnpaid'),(3,'ArrivedAndPaid');
/*!40000 ALTER TABLE `orderStatuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orderId` int NOT NULL AUTO_INCREMENT,
  `vehicleId` int NOT NULL,
  `userId` int NOT NULL,
  `timeOrder` float NOT NULL,
  `priceTotal` float NOT NULL,
  `orderStatusId` int NOT NULL,
  `orderTimestamp` datetime NOT NULL,
  `rentCityLocationId` int NOT NULL,
  `returnCityLocationId` int DEFAULT NULL,
  PRIMARY KEY (`orderId`),
  UNIQUE KEY `orderID_UNIQUE` (`orderId`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,3,25.5,76.5,3,'2022-08-01 12:09:09',1,3),(2,4,3,34.6,20.3,3,'2022-10-03 08:23:09',3,2),(3,5,3,14.5,10.6,3,'2022-10-03 12:14:03',2,2),(4,3,4,10.8,7.6,2,'2022-10-06 10:34:21',1,1),(100,4,5,20.5,30.7,2,'2022-10-07 22:22:22',1,NULL),(161,5,6,30.5,60.7,3,'2022-10-11 14:22:22',1,NULL),(162,2,1,4.5,11.25,3,'2022-10-11 16:22:22',9,8);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userTypes`
--

DROP TABLE IF EXISTS `userTypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userTypes` (
  `userTypeId` int NOT NULL,
  `userTypeName` varchar(50) NOT NULL,
  PRIMARY KEY (`userTypeId`),
  UNIQUE KEY `userTypeID_UNIQUE` (`userTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userTypes`
--

LOCK TABLES `userTypes` WRITE;
/*!40000 ALTER TABLE `userTypes` DISABLE KEYS */;
INSERT INTO `userTypes` VALUES (1,'manager'),(2,'operator'),(3,'customer');
/*!40000 ALTER TABLE `userTypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(50) NOT NULL,
  `userPassword` varchar(50) NOT NULL,
  `userType` int NOT NULL,
  `balance` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`userId`),
  UNIQUE KEY `userID_UNIQUE` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Amy','111111',1,0),(2,'Bob','222222',2,0),(3,'Cindy','333333',3,47.56),(4,'David','444444',3,37.5),(5,'Sam','555555',3,100),(6,'Nancy','123456',3,0),(7,'calvin','testRegistration',3,0),(8,'david95','testRegistration2',1,0),(9,'Michael','test123',2,0),(10,'Lisa97','lisaTest',3,0),(11,'Lena92','lenaTest',2,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicleStatuses`
--

DROP TABLE IF EXISTS `vehicleStatuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicleStatuses` (
  `vehicleStatusId` int NOT NULL AUTO_INCREMENT,
  `vehicleStatusName` varchar(50) NOT NULL,
  PRIMARY KEY (`vehicleStatusId`),
  UNIQUE KEY `vehicleStatusID_UNIQUE` (`vehicleStatusId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicleStatuses`
--

LOCK TABLES `vehicleStatuses` WRITE;
/*!40000 ALTER TABLE `vehicleStatuses` DISABLE KEYS */;
INSERT INTO `vehicleStatuses` VALUES (1,'available'),(2,'damaged');
/*!40000 ALTER TABLE `vehicleStatuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicleTypes`
--

DROP TABLE IF EXISTS `vehicleTypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicleTypes` (
  `vehicleTypeId` int NOT NULL AUTO_INCREMENT,
  `vehicleTypeName` varchar(50) NOT NULL,
  PRIMARY KEY (`vehicleTypeId`),
  UNIQUE KEY `vehicleTypeID_UNIQUE` (`vehicleTypeId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicleTypes`
--

LOCK TABLES `vehicleTypes` WRITE;
/*!40000 ALTER TABLE `vehicleTypes` DISABLE KEYS */;
INSERT INTO `vehicleTypes` VALUES (1,'bike'),(2,'scooter');
/*!40000 ALTER TABLE `vehicleTypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicles`
--

DROP TABLE IF EXISTS `vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicles` (
  `vehicleId` int NOT NULL AUTO_INCREMENT,
  `vehicleTypeId` int NOT NULL,
  `vehicleStatusId` int NOT NULL,
  `pricePerMinute` float NOT NULL,
  `batterySoc` float NOT NULL,
  `cityLocationId` int DEFAULT NULL,
  PRIMARY KEY (`vehicleId`),
  UNIQUE KEY `vehicleID_UNIQUE` (`vehicleId`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicles`
--

LOCK TABLES `vehicles` WRITE;
/*!40000 ALTER TABLE `vehicles` DISABLE KEYS */;
INSERT INTO `vehicles` VALUES (1,1,1,2.5,0.98,NULL),(2,1,1,2.5,1,1),(3,1,1,2.5,1,3),(4,2,1,3.5,1,1),(5,2,1,3.5,1,3),(6,2,2,3.5,0.26,NULL),(7,1,1,2.5,0.75,3),(8,2,1,3.5,0.77,3),(9,1,1,2.5,1,2),(10,2,1,3.5,0.95,3),(11,1,1,2.5,1,1);
/*!40000 ALTER TABLE `vehicles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-13 10:48:54
