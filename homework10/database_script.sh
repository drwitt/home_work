#Shell script to create database (db_danny) and enter 4 .csv files into
#database:

#!/usr/bin/env bash

sqlite3 /Users/dannywitt/bios821/Homework/home_work/homework10/medical_data.db << EOS

.mode csv

--File import physician.csv and make table physician:

.import ./physician.csv physician
.schema physician
     CREATE TABLE physician(
          "physicianid" REAL, PRIMARY KEY NOT NULL,
          "lastname" TEXT,
          "firstname" TEXT,
          "specialty" TEXT);

--File import patient.csv and make table patient:
.import ./patient.csv patient
.schema patient
     CREATE TABLE patient(
          "patientid" REAL PRIMARY KEY NOT NULL,
          "lastname" TEXT,
          "firstname" TEXT,
          "gender" CHARACTER(20),
          "dob" DATE);

--File import encounter.csv and make table encounter:    
.import ./encounter.csv encounter
.schema encounter
     CREATE TABLE encounter(
          "encounterid" REAL PRIMARY KEY NOT NULL,
          "patientid" REAL FOREIGN KEY NOT NULL,
          "encounterdate" DATE,
          "encounterphysician" REAL,
          "encounterreason" TEXT,
          "billingamount" DECIMAL(5));

--File import billing.csv and make table billing:
.import ./billing.csv billing
.schema billing
     CREATE TABLE billing(
          "billingid" REAL PRIMARY KEY NOT NULL,
          "encounterid" REAL FOREIGN KEY,
          "code" BLOB);
EOS