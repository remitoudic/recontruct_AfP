-- Extracted database schema from legacy AfP pawnshop software

CREATE TABLE `einaus` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `datum` date NOT NULL,
  `betrag` decimal(12,6) NOT NULL,
  `posten` varchar(255) NOT NULL,
  `dmbetrag` decimal(10,2) default NULL,
  `konto` int(10) unsigned default NULL,
  `status` int(10) unsigned NOT NULL default '0',
  `pfand` int(10) unsigned default NULL,
  PRIMARY KEY (`id`),
  KEY `datum` (`datum`),
  KEY `pfand` (`pfand`)
) ENGINE=InnoDB COMMENT='Einnahmen, Ausgaben (Cashbook Ledger)';

CREATE TABLE `kunden` (
  `id` int(10) unsigned NOT NULL,
  `name` varchar(30) default NULL,
  `vorname` varchar(30) default NULL,
  `geburtstag` date default NULL,
  `geburtsort` varchar(40) default NULL,
  `wohnort` varchar(40) default NULL,
  `strasse` varchar(40) default NULL,
  `personr` varchar(15) default NULL,
  `legitimation` varchar(30) default NULL,
  `behörde` varchar(25) default NULL,
  `erstervertrag` int(10) signed default NULL,
  `sperre` tinyint(1) NOT NULL default '0',
  PRIMARY KEY (`id`),
  KEY `namevornamegeburtstag` (`name`,`vorname`,`geburtstag`)
) ENGINE=InnoDB COMMENT='Customers';

CREATE TABLE `pfand` (
  `id` int(10) unsigned NOT NULL,
  `kunde` int(10) unsigned NOT NULL,
  `datum` date NOT NULL,
  `betrag` decimal(12,6) NOT NULL,
  `unkosten` decimal(12,6) NOT NULL,
  `Status` int(10) unsigned NOT NULL,
  `enddatum` date default NULL,
  `vorgänger` int(10) default NULL,
  `nachfolger` int(10) default NULL,
  `next` int(10) default NULL,
  `versart` int(10) unsigned NOT NULL,
  `gegenstand` text NOT NULL,
  `lager` varchar(45) default NULL,
  `dmbetrag` decimal(10,2) default NULL,
  `dmunkosten` decimal(10,2) default NULL,
  PRIMARY KEY (`id`),
  KEY `datum` (`datum`),
  KEY `enddatum` (`enddatum`)
) ENGINE=InnoDB COMMENT='Pawn items / Pledges';
