-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 22, 2018 at 08:28 AM
-- Server version: 5.7.24-0ubuntu0.18.04.1
-- PHP Version: 7.2.10-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskemail`
--

-- --------------------------------------------------------

--
-- Table structure for table `email`
--

CREATE TABLE `email` (
  `event_id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `email_subject` varchar(50) NOT NULL,
  `email_content` varchar(500) NOT NULL,
  `time_stamp` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `email`
--

INSERT INTO `email` (`event_id`, `email`, `email_subject`, `email_content`, `time_stamp`) VALUES
(1, 'arydwimarta@gmail.com', 'email subject', 'this is the content information of email', '2018-11-19 03:13:11'),
(3, 'test@gmail.com', 'subject test', 'content test', '2018-11-19 03:13:15'),
(4, 'test2@mail.com', 'test2', 'test2', '2018-11-19 03:23:15'),
(5, 'test3@mail.com', 'test3', 'test3', '2018-11-20 09:33:10'),
(7, 'test4@mail.com', 'test4', 'test4', '2018-11-20 09:39:51'),
(9, 'test6@mail.com', 'test6', 'test6', '2018-11-20 14:02:14'),
(10, 'test7@mail.com', 'test7', 'test7', '2018-11-20 14:02:25'),
(11, 'test8@mail.com', 'test8', 'test8', '2018-11-20 14:02:34'),
(12, 'test5@mail.com', 'test5', 'test5', '2018-11-20 06:16:44'),
(13, 'test9@mail.com', 'test9', 'test9', '2018-11-20 16:06:12.520270+08:00'),
(14, 'test10@gmail.com', 'test10', 'test10', '20 November, 2018 16 07'),
(15, 'fix@mail.com', 'fix', 'fix', '20 November 2018 20:15'),
(16, 'fix1@mail.com', 'fix1', 'fix1', '21 Nov 2018 12:22'),
(17, 'fix2@mail.com', 'fix2', 'fix2', '21 Nov 2018 12:22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `email`
--
ALTER TABLE `email`
  ADD PRIMARY KEY (`event_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `email`
--
ALTER TABLE `email`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
