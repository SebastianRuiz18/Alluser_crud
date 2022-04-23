CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);


-- Creates a vehicle_type table
CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

-- Creates a vehicle table
CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45) NOT NULL,
    licence_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (owner_id) REFERENCES user(id)
);

 

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Sebastian",
    "Ruiz",
    "Play Guitar"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Skiing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Playing golf"
);

-- Create dummy data fot vehicles types:

INSERT INTO vehicle_type (description) VALUES ('Car');
INSERT INTO vehicle_type (description) VALUES ('Truck');
INSERT INTO vehicle_type (description) VALUES ('SUV');
INSERT INTO vehicle_type (description) VALUES ('Motorcycle');
INSERT INTO vehicle_type (description) VALUES ('Bicycle');

--CREATE SOME DUMMY DATA FOR VEHICLES:

INSERT INTO vehicle (
    color, 
    license_plate,
    v_type,
    owner_id
) VALUES (
    "red",
    "HELLO1",
    1,
    1
);

INSERT INTO vehicle (
    color, 
    license_plate,
    v_type,
    owner_id
) VALUES (
    "purple",
    "HELLO1",
    2,
    2
);

INSERT INTO vehicle (
    color, 
    license_plate,
    v_type,
    owner_id
) VALUES (
    "black",
    "HELLO1",
    3,
    2
);

-- Join 2 tables

SELECT  user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.licence_plate,
        vehicle.color,
        vehicle_type.description
FROM user
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;