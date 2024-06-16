CREATE DATABASE IF NOT EXISTS Booking;

USE Booking;

CREATE TABLE IF NOT EXISTS PersonBook (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50), 
    email VARCHAR(50), 
    checkinDate VARCHAR(50), 
    checkoutDate VARCHAR(50), 
    roomType VARCHAR(50), 
    location VARCHAR(50)
);

