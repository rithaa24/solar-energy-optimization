create database solar_model_database;
use solar_model_database;

create table sampling_data(id INT AUTO_INCREMENT PRIMARY KEY,
    sampling_frequency VARCHAR(50),
    polynomial_augmentation INT,
    features VARCHAR(100),
    history INT,
    nb_iter INT,
    nb_epoch FLOAT
);
CREATE TABLE model_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sampling_id INT,
    MAPE_min FLOAT,
    MAPE_med FLOAT,
    MAPE_max FLOAT,
    MAPE_std FLOAT,
    R2_max FLOAT,
    R2_std FLOAT,
    R2_CI FLOAT,
    R2_mean FLOAT,
    MBE_min FLOAT,
    MBE_med FLOAT,
    MBE_max FLOAT,
    MBE_std FLOAT,
    MBE_CI FLOAT,
    MBE_mean FLOAT,
    FOREIGN KEY (sampling_id) REFERENCES sampling_data(id) ON DELETE CASCADE
);
SHOW DATABASES;
USE solar_model;
SELECT * FROM sampling_data;
SELECT * FROM model_metrics;
INSERT INTO sampling_data (sampling_frequency, polynomial_augmentation, features, history, nb_iter, nb_epoch)
VALUES 
('7_days',4,'GHI_season',10,10,0),
('6_days',4,'GHI_season',10,10,0),
('5_days',3,'GHI_season_d1',10,10,2.5),
('4_days',1,'GHI_season_d1',5,10,0),
('72_hours',1,'GHI_d1_d2',15,10,0),
('48_hours',4,'GHI_season',5,10,43.6),
('24_hours',2,'GHI_season_d1_d2_d3',5,10,36.1),
('12_hours',1,'GHI_season_d1',5,10,34),
('6_hours',5,'GHI_season',5,10,9.3),
('4_hours',5,'GHI_season',5,10,20.7),
('2_hours',4,'GHI_season',10,10,21.6),
('1_hour',5,'GHI',5,10,0),
('45_minutes',5,'GHI_season',5,10,34.2),
('30_minutes',3,'GHI_season',5,10,18),
('15_minutes',5,'GHI',5,10,31.9);








INSERT INTO model_metrics (
    sampling_id, MAPE_min, MAPE_med, MAPE_max, MAPE_std, 
    R2_max, R2_std, R2_CI, R2_mean, 
    MBE_min, MBE_med, MBE_max, MBE_std, MBE_CI, MBE_mean
)
VALUES
(1, 0.05, 0.07, 0.12, 0.01, 0.95, 0.02, 0.03, 0.90, -0.01, 0.00, 0.02, 0.005, 0.01, 0.00),
(2, 0.06, 0.08, 0.13, 0.02, 0.94, 0.02, 0.03, 0.89, -0.01, 0.00, 0.01, 0.005, 0.01, 0.01),
(3, 0.04, 0.06, 0.11, 0.01, 0.96, 0.01, 0.02, 0.91, -0.02, 0.00, 0.02, 0.004, 0.01, 0.00),
(4, 0.07, 0.09, 0.15, 0.02, 0.92, 0.03, 0.04, 0.87, -0.01, 0.01, 0.03, 0.006, 0.01, 0.01),
(5, 0.06, 0.08, 0.14, 0.02, 0.93, 0.02, 0.03, 0.88, -0.01, 0.01, 0.02, 0.005, 0.01, 0.01),
(6, 0.05, 0.07, 0.13, 0.01, 0.94, 0.02, 0.03, 0.89, -0.01, 0.00, 0.02, 0.004, 0.01, 0.00),
(7, 0.06, 0.08, 0.14, 0.02, 0.93, 0.03, 0.04, 0.88, -0.01, 0.01, 0.03, 0.006, 0.01, 0.01),
(8, 0.04, 0.06, 0.11, 0.01, 0.96, 0.01, 0.02, 0.91, -0.02, 0.00, 0.02, 0.004, 0.01, 0.00),
(9, 0.05, 0.07, 0.12, 0.01, 0.95, 0.02, 0.03, 0.90, -0.01, 0.00, 0.02, 0.005, 0.01, 0.00),
(10, 0.06, 0.08, 0.13, 0.02, 0.94, 0.02, 0.03, 0.89, -0.01, 0.00, 0.01, 0.005, 0.01, 0.01),
(11, 0.04, 0.06, 0.11, 0.01, 0.96, 0.01, 0.02, 0.91, -0.02, 0.00, 0.02, 0.004, 0.01, 0.00),
(12, 0.07, 0.09, 0.15, 0.02, 0.92, 0.03, 0.04, 0.87, -0.01, 0.01, 0.03, 0.006, 0.01, 0.01),
(13, 0.06, 0.08, 0.14, 0.02, 0.93, 0.02, 0.03, 0.88, -0.01, 0.01, 0.02, 0.005, 0.01, 0.01),
(14, 0.05, 0.07, 0.13, 0.01, 0.94, 0.02, 0.03, 0.89, -0.01, 0.00, 0.02, 0.004, 0.01, 0.00),
(15, 0.06, 0.09, 0.14, 0.02, 0.93, 0.03, 0.04, 0.88, -0.01, 0.01, 0.03, 0.006, 0.01, 0.01);

-- accuracy chart --
create table model_accuracy_chart(  id INT AUTO_INCREMENT PRIMARY KEY,
sample_frequency varchar(50),
R2_max float,
MAPE_min float
);

INSERT INTO model_accuracy_chart(sample_frequency, R2_max, MAPE_min)
VALUES 
("15_minutes", 0.93, 22.15),
("30_minutes", 0.91, 26.59),
("45_minutes", 0.91, 31.41),
("1_hour", 0.90, 33.45),
("2_hours", 0.88, 37.75),
("4_hours", 0.82, 41.25),
("6_hours", 0.79, 54.79),
("12_hours", 0.32, 46.12),
("6_days", 0.31, 19.85),
("7_days", 0.27, 17.85),
("5_days", 0.26, 19.00),
("4_days", 0.23, 21.83),
("48_hours", 0.22, 27.74),
("72_hours", 0.18, 25.31),
("24_hours", 0.17, 46.66);



select*from model_accuracy_chart;

-- cost efficiency --
create table cost_efficiency( id INT AUTO_INCREMENT PRIMARY KEY,
sample_frequency varchar(50),
costefficiencyscore float);

INSERT INTO cost_efficiency(sample_frequency,costefficiencyscore)
VALUES 
("15_minutes", 0.04),
("30_minutes", 0.03),
("45_minutes", 0.03),
("1_hour", 0.03),
("2_hours", 0.02),
("4_hours", 0.02),
("6_days", 0.02),
("7_days", 0.02),
("6_hours", 0.01),
("5_days", 0.01),
("4_days", 0.01),
("48_hours", 0.01),
("72_hours", 0.01),
("12_hours", 0.01),
("24_hours",0.00);

select* from cost_efficiency;
-- sampling frequency --
create table sampling_frequency( id INT AUTO_INCREMENT PRIMARY KEY,
sample_frequency varchar(50),
R2 float);

INSERT INTO sampling_frequency(sample_frequency,R2)
VALUES 
("24_hours", 0.17),
("72_hours", 0.18),
("48_hours", 0.22),
("1_hour", 0.23),
("4_days", 0.26),
("5_days", 0.27),
("7_days", 0.31),
("6_days", 0.32),
("12_hours", 0.79),
("4_hours", 0.82),
("2_hours", 0.88),
("1_hour", 0.90),
("45 minutes", 0.91),
("30 minutes", 0.91),
("15_minutes",0.93);
select*from sampling_frequency;

-- model efficiency --

create table model_efficiency( id INT AUTO_INCREMENT PRIMARY KEY,
sample_frequency varchar(50),
MAPE float,
R2 float,
Polynomial_augumentation int);
INSERT INTO model_efficiency(sample_frequency,MAPE,R2,Polynomial_augumentation)
VALUES 
("1_hour",33.45,0.90,5),
("12_hours",46.12,0.32,1),
("15_minutes",22.5,0.93,5),
('2_hours', 37.75, 0.88, 4),
('24_hours', 46.66, 0.17, 2),
('30_minutes', 26.59, 0.91, 3),
('4_days', 21.83, 0.23, 1),
('4_hours', 41.25, 0.82, 5),
('45_minutes', 31.41, 0.91, 5),
('48_hours', 27.74, 0.22, 4),
('5_days', 19.00, 0.26, 3),
('6_days', 19.85, 0.31, 3),
('6_hours', 54.79, 0.79, 5),
('7_days', 17.85, 0.27, 4),
('72_hours', 25.31, 0.18, 1);

-- performance --
create table performance( id INT AUTO_INCREMENT PRIMARY KEY,
R2_MED float,
R2_MIN float,
R2_MAX float,
R2_mean float);


INSERT INTO performance(R2_MED,R2_MIN,R2_MAX,R2_MEAN)
VALUES (8.01,7.61,8.11,7.97);

FLUSH PRIVILEGES;

ALTER USER 'root'@'localhost' IDENTIFIED BY 'Hari@123'; 
SET PASSWORD FOR 'root'@'localhost' = 'Hari@123';
CREATE TABLE cost_efficiency_persistence (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_frequency TEXT NOT NULL,
    costefficiencyscore REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cost_efficiency_persistence (sample_frequency, costefficiencyscore)
VALUES 
    ('15 Minutes', 0.90),
    ('30 Minutes', 0.87),
    ('45 Minutes', 0.81),
    ('1 Hour', 0.73),
    ('2 Hours', 0.35),
    ('12 Hours', 0.05),
    ('6 Days', -0.24),
    ('24 Hours', -0.46),
    ('4 Hours', -0.53),
    ('72 Hours', -0.88),
    ('48 Hours', -0.89),
    ('6 Hours', -0.91),
    ('7 Days', -1.25),
    ('4 Days', -1.43),
    ('5 Days', -1.44);
    
 CREATE TABLE model_accuracy_comparison (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_frequency VARCHAR(50) NOT NULL,
    persistence_accuracy FLOAT,
    lstm_accuracy FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO model_accuracy_comparison (sample_frequency, persistence_accuracy, lstm_accuracy)
VALUES 
    ('1 hour', 85.2, 91.4),
    ('12 hours', 76.4, 81.6),
    ('15 minutes', 88.1, 97.7),
    ('2 hours', 83.7, 89.5),
    ('24 hours', 72.5, 79.3),
    ('30 minutes', 89.3, 94.2),
    ('4 days', 67.8, 73.6),
    ('4 hours', 84.6, 90.7),
    ('45 minutes', 90.1, 95.0),
    ('48 hours', 70.3, 76.1),
    ('5 days', 65.9, 71.8),
    ('6 days', 68.4, 74.3),
    ('6 hours', 86.2, 91.0),
    ('7 days', 66.7, 72.2),
    ('72 hours', 69.5, 75.6);
CREATE TABLE accuracy_over_frequency (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_frequency VARCHAR(50) NOT NULL,
    persistence_model_accuracy FLOAT,
    lstm_model_accuracy FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO accuracy_over_frequency (sample_frequency, persistence_model_accuracy, lstm_model_accuracy)
VALUES 
    ('24 Hours', 60, 70),
    ('72 Hours', 62, 72),
    ('48 Hours', 63, 75),
    ('4 Days', 65, 77),
    ('5 Days', 67, 80),
    ('7 Days', 70, 82),
    ('6 Days', 72, 85),
    ('12 Hours', 75, 87),
    ('6 Hours', 77, 90),
    ('4 Hours', 80, 92),
    ('2 Hours', 82, 94),
    ('1 Hour', 85, 95),
    ('45 Minutes', 87, 97),
    ('30 Minutes', 89, 98),
    ('15 Minutes', 91, 99);

    

