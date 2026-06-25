-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 08, 2026 at 09:47 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `parkinsonspiraldudiodb`
--

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(50) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Age`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', '40', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sangeeth', 'sangeeth'),
(2, 'priya', '23', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'priya', 'priya');

-- --------------------------------------------------------

--
-- Table structure for table `reporttb`
--

CREATE TABLE `reporttb` (
  `Id` bigint(10) NOT NULL auto_increment,
  `user` varchar(250) NOT NULL,
  `Type` varchar(250) NOT NULL,
  `Result` varchar(250) NOT NULL,
  `Score` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `reporttb`
--

INSERT INTO `reporttb` (`Id`, `user`, `Type`, `Result`, `Score`, `Date`) VALUES
(1, 'priya', 'Image', 'healthy', '99.54', '08-03-2026'),
(2, 'priya', 'Audio', 'parkinson', '99.83', '08-03-2026');
