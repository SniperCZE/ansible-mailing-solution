CREATE TABLE `spam_autolearn_queue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class` ENUM('SPAM', 'HAM') NOT NULL,
  `email_source` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
