use universityclb;

ALTER TABLE DEPARTMENT
	ADD CONSTRAINT FK_DEPARTMENT_ChairID
		FOREIGN KEY (ChairID) REFERENCES FACULTY(FID);