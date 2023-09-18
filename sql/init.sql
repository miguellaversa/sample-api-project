-- Create tables

CREATE TABLE IF NOT EXISTS api_users (
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	password VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS users (
  id VARCHAR(40) NOT NULL PRIMARY KEY,
  first_name VARCHAR(25) NOT NULL,
  last_name VARCHAR(25) NOT NULL,
  email VARCHAR(50) NOT NULL,
  password VARCHAR(30) NOT NULL
);


CREATE TABLE IF NOT EXISTS address (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id VARCHAR(40) NOT NULL,
  address_1 VARCHAR(100) NOT NULL,
  address_2 VARCHAR(100) NULL,
  city VARCHAR(25) NOT NULL,
  state VARCHAR(25) NOT NULL,
  zip VARCHAR(15) NOT NULL,
  country VARCHAR(25) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
);



-- Sample data
INSERT INTO api_users (username, password)
VALUES
  ('sample', '$2b$12$hOXbfEUiL3jjIvz/qIbBNOKy86HGP1BNvNZMsbGugMw.SZ4/6kcRq');


INSERT INTO users (id, first_name, last_name, email, password)
VALUES
  ('12604b62-f50c-4fc2-933f-54c7db8e08f5', 'John', 'Doe', 'john.doe@example.com', 'password123'),
  ('f8dc0eb5-9c33-4b09-99f7-7318aeb157ea', 'Jane', 'Smith', 'jane.smith@example.com', 'securepass'),
  ('71328d4a-22fc-434c-85bf-ecf6dce68d1e', 'Michael', 'Johnson', 'michael.johnson@example.com', 'mysecret'),
  ('24e1c7f7-6863-4780-b3e3-7e9da6ce1c28', 'Emily', 'Williams', 'emily.williams@example.com', 'test123'),
  ('a5f50dc9-e7f0-4e58-ba3c-40e8eb56f946', 'David', 'Brown', 'david.brown@example.com', 'qwerty456'),
  ('91db2e7b-8c45-4da4-bd8d-4684998c0676', 'Sarah', 'Davis', 'sarah.davis@example.com', '12345678'),
  ('9f3cf840-3a9e-4d44-8b1e-c1b5b7a8508f', 'Daniel', 'Miller', 'daniel.miller@example.com', 'letmein'),
  ('6c2a8d14-b8a4-47f5-9c4d-9a2f0de76e6b', 'Olivia', 'Wilson', 'olivia.wilson@example.com', 'p@ssw0rd'),
  ('e8650d53-75c9-4a01-9b32-14f6cf2fb9c9', 'James', 'Martinez', 'james.martinez@example.com', 'welcome123'),
  ('b243907d-09e7-4c65-b937-9d1aee704ee7', 'Sophia', 'Taylor', 'sophia.taylor@example.com', 'password!'),
  ('61f1c1f7-85a7-4e2b-b0d0-07b12dbf05d1', 'Liam', 'Anderson', 'liam.anderson@example.com', 's3cur3'),
  ('f4e9e731-8aa7-4c63-8be7-bb49ac9d5b6d', 'Ava', 'Thomas', 'ava.thomas@example.com', 'myPa$$word'),
  ('4c6ea72c-975d-40db-9b7e-297c998c9149', 'Noah', 'Jackson', 'noah.jackson@example.com', '123abc'),
  ('ac26d1c1-1d4c-42f8-a3eb-8f0c5b31b77e', 'Emma', 'White', 'emma.white@example.com', 'p@ss123'),
  ('1c4f9d12-5ac1-4a6b-8e44-9fbaa6cb0d26', 'Ethan', 'Harris', 'ethan.harris@example.com', 'secure123'),
  ('b86b5891-0be0-49b0-99c9-05d0d4c43aa9', 'Mia', 'Martin', 'mia.martin@example.com', 'qwerty123'),
  ('6fc43b9a-56c1-4c63-8a67-5c2a93f17ff0', 'Alexander', 'Thompson', 'alexander.thompson@example.com', 'testpass'),
  ('8cfd098a-8f87-488b-90c6-c72c52739d5d', 'Isabella', 'Garcia', 'isabella.garcia@example.com', 'mypass'),
  ('3ae6a4c7-c444-44d3-bdcf-9e09c2bf7f5f', 'William', 'Robinson', 'william.robinson@example.com', 'pass1234'),
  ('1c4d95a3-e246-4f36-8d86-b528c944c858', 'Sofia', 'Lopez', 'sofia.lopez@example.com', 'hello123');


INSERT INTO address (user_id, address_1, address_2, city, state, zip, country)
VALUES
  ('12604b62-f50c-4fc2-933f-54c7db8e08f5', '123 Main St', 'Apt 456', 'Springfield', 'IL', '12345', 'United States'),
  ('12604b62-f50c-4fc2-933f-54c7db8e08f5', '789 Elm St', NULL, 'Riverside', 'CA', '67890', 'United States'),
  ('f8dc0eb5-9c33-4b09-99f7-7318aeb157ea', '456 Oak Ave', 'Suite 789', 'New York', 'NY', '54321', 'United States'),
  ('f8dc0eb5-9c33-4b09-99f7-7318aeb157ea', '987 Pine St', NULL, 'Los Angeles', 'CA', '45678', 'United States'),
  ('1c4d95a3-e246-4f36-8d86-b528c944c858', '555 Maple Dr', 'Unit 123', 'Chicago', 'IL', '98765', 'United States'),
  ('1c4d95a3-e246-4f36-8d86-b528c944c858', '222 Cedar Ln', NULL, 'Houston', 'TX', '34567', 'United States'),
  ('b243907d-09e7-4c65-b937-9d1aee704ee7', '789 Oak St', 'Suite 456', 'San Francisco', 'CA', '98765', 'United States'),
  ('b243907d-09e7-4c65-b937-9d1aee704ee7', '456 Pine Ave', NULL, 'Seattle', 'WA', '65432', 'United States'),
  ('71328d4a-22fc-434c-85bf-ecf6dce68d1e', '321 Pine St', 'Suite 789', 'Houston', 'TX', '98765', 'United States'),
  ('24e1c7f7-6863-4780-b3e3-7e9da6ce1c28', '555 Elm Ave', NULL, 'Chicago', 'IL', '54321', 'United States'),
  ('a5f50dc9-e7f0-4e58-ba3c-40e8eb56f946', '789 Oak St', 'Unit 456', 'Los Angeles', 'CA', '12345', 'United States'),
  ('91db2e7b-8c45-4da4-bd8d-4684998c0676', '456 Maple Dr', NULL, 'New York', 'NY', '67890', 'United States'),
  ('6c2a8d14-b8a4-47f5-9c4d-9a2f0de76e6b', '123 Oak St', NULL, 'San Francisco', 'CA', '23456', 'United States');