CREATE TABLE `domains` (
  `dom_id` int(11) NOT NULL AUTO_INCREMENT,
  `dom_name` varchar(100) NOT NULL,
  `dom_enabled` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`dom_id`),
  UNIQUE KEY `dom_name` (`dom_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `aliases` (
  `al_id` int(11) NOT NULL AUTO_INCREMENT,
  `dom_id` int(11) NOT NULL,
  `al_user` varchar(100) NOT NULL,
  `al_target` varchar(100) NOT NULL,
  `al_enabled` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`al_id`),
  UNIQUE KEY `dom_id` (`dom_id`,`al_user`),
  CONSTRAINT `aliases_ibfk_1` FOREIGN KEY (`dom_id`) REFERENCES `domains` (`dom_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `mailboxes` (
  `mb_id` int(11) NOT NULL AUTO_INCREMENT,
  `dom_id` int(11) NOT NULL,
  `mb_user` varchar(100) NOT NULL,
  `mb_password` varchar(255) NOT NULL,
  `mb_enabled` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`mb_id`),
  UNIQUE KEY `dom_id` (`dom_id`,`mb_user`),
  CONSTRAINT `mailboxes_ibfk_1` FOREIGN KEY (`dom_id`) REFERENCES `domains` (`dom_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;