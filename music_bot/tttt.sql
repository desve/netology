BEGIN TRANSACTION;
CREATE TABLE `music` (
	`id`	INTEGER NOT NULL,
	`file_id`	TEXT NOT NULL,
	`right_answer`	TEXT NOT NULL,
	`wrong_answer`	TEXT NOT NULL,
	PRIMARY KEY(`id`,`file_id`,`right_answer`,`wrong_answer`)
);
INSERT INTO `music` VALUES (1,'AwADAgADJwAD82eXEZPCMpy6j80dAg','Бременские музыканты','Чебурашка');
INSERT INTO `music` VALUES (2,'AwADAgADIwAD82eXEe9EcNjtheRPAg','В мире животных','Программа Врнмя');
INSERT INTO `music` VALUES (3,'AwADAgADKAAD82eXEQn7Fkjh3bGNAg','Звездные войны','Операция Ы');
INSERT INTO `music` VALUES (4,'AwADAgADKgAD82eXEeaUMCOsOlqQAg','Кавказкая пленница','Ирония судьбы');
INSERT INTO `music` VALUES (5,'AwADAgADKwAD82eXEZvI9ONdgn1JAg','Каникулы строгого режима','Терминатор');
COMMIT;
