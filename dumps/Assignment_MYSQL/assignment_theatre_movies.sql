-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: assignment
-- ------------------------------------------------------
-- Server version	5.7.23

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
-- Table structure for table `theatre_movies`
--

DROP TABLE IF EXISTS `theatre_movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `theatre_movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `releaseYear` varchar(255) DEFAULT NULL,
  `genres` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `theatre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theatre_movies`
--

LOCK TABLES `theatre_movies` WRITE;
/*!40000 ALTER TABLE `theatre_movies` DISABLE KEYS */;
INSERT INTO `theatre_movies` VALUES (1,'The Nightmare Before Christmas','1993','Fantasy,Comedy,Animated,Children,Holiday','The Pumpkin King of Halloweentown plans to kidnap Santa Claus and deliver chills instead of joy.','AMC Barton Creek Square 14'),(2,'The Addams Family','2019','Comedy,Animated,Children','The Addams family encounter a shady TV personality who despises their eerie hilltop mansion.','AMC Barton Creek Square 14'),(3,'Tenet','2020','Action,Science fiction,Thriller','A secret agent embarks on a dangerous, time-bending mission to prevent the start of World War III.','AMC Barton Creek Square 14'),(4,'The War With Grandpa','2020','Comedy','A scheming boy devises a series of outrageous pranks to win back his room from his grandfather.','AMC Barton Creek Square 14'),(5,'2 Hearts','2020','Romance,Drama','A college student falls in love with a classmate, while a Cuban exile falls for a flight attendant.','AMC Barton Creek Square 14'),(6,'The Empty Man','2020','Horror,Thriller','A retired cop links mysterious disappearances to a mystical urban legend known as the Empty Man.','AMC Barton Creek Square 14'),(7,'Synchronic','2019','Science fiction,Thriller','A paramedic encounters a psychedelic drug that changes reality and the flow of time itself.','AMC Barton Creek Square 14'),(8,'Honest Thief','2020','Action,Thriller','A professional bank robber goes on the run to clear his name and bring two crooked cops to justice.','AMC Barton Creek Square 14'),(9,'Monsters, Inc.','2001','Comedy,Fantasy,Adventure,Animated,Children','A blue behemoth (John Goodman) and his one-eyed pal (Billy Crystal) scare children.','AMC Barton Creek Square 14'),(10,'The Boss Baby','2017','Comedy,Adventure,Animated,Children','A wildly imaginative boy discovers that his new brother is actually a spy on a secret mission.','AMC Barton Creek Square 14'),(11,'Yellow Rose','2019','Drama,Music,Country','A teen must decide whether to stay with her family or leave town to become a country music singer.','AMC Barton Creek Square 14'),(12,'Kajillionaire','2020','Comedy drama','A family of con artists encounter a stranger who turns their entire world upside down.','AMC Barton Creek Square 14'),(13,'The Kid Detective','2020','Dark comedy','A down-and-out detective teams up with a teenager to solve the mysterious murder of her boyfriend.','AMC Barton Creek Square 14'),(14,'The Curse of La Llorona','2019','Horror,Thriller','A disillusioned priest helps a social worker and her children battle the legendary ghost La Llorona.','AMC Barton Creek Square 14');
/*!40000 ALTER TABLE `theatre_movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-26 13:03:59
