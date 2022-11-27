-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Erstellungszeit: 06. Nov 2022 um 02:19
-- Server-Version: 8.0.31
-- PHP-Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `php_docker`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `php_docker_table`
--

CREATE TABLE `php_docker_table` (
  `USR_ID` int NOT NULL,
  `User` text NOT NULL,
  `Password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Daten für Tabelle `php_docker_table`
--

INSERT INTO `php_docker_table` (`USR_ID`, `User`, `Password`) VALUES
(1, 'Admin', 'password'),
(2, 'Ali', 'passwd');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `php_docker_table`
--
ALTER TABLE `php_docker_table`
  ADD PRIMARY KEY (`USR_ID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `php_docker_table`
--
ALTER TABLE `php_docker_table`
  MODIFY `USR_ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
