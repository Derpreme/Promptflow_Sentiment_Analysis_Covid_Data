select * from mysqltutorial.surveytable; 
DESCRIBE mysqltutorial.surveytable;
INSERT INTO mysqltutorial.surveytable (_id, llmTask, _owner) VALUES ('000003', 'What are the biggest challenges American high school students are facing', 'ShuzhenNong');
INSERT INTO mysqltutorial.surveytable (_id, llmTask, _owner) VALUES ('000004', 'What are the biggest worries American high school students are facing', 'ShuzhenNong');
INSERT INTO mysqltutorial.surveytable (_id, llmTask, _owner) VALUES ('000005', 'What are the biggest worries male American high school students are facing', 'ShuzhenNong');

CREATE TABLE mysqltutorial.MicrosoftFormTable (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    School VARCHAR(255),
    Grade VARCHAR(50),
    Question TEXT,
    SubmissionTime DATETIME,
    ResponderEmail VARCHAR(255)
);
DESCRIBE mysqltutorial.MicrosoftFormTable;

select * from mysqltutorial.MicrosoftFormTable; 

select * from mysqltutorial.covid_data_for_sentiment_analysis;

INSERT INTO mysqltutorial.MicrosoftFormTable (School, Grade, Question, SubmissionTime, ResponderEmail) VALUES ('High School', '9th', 'What are the biggest challenges American high school students are facing', '2024-07-08', 'lyhnszk@hotmail.com');