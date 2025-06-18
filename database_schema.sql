-- Table to store information about different varieties of produce
CREATE TABLE varieties (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the variety
    name VARCHAR(255) NOT NULL, -- Name of the variety
    description TEXT, -- Detailed description of the variety
    image_url VARCHAR(255), -- URL of an image of the variety
    video_url VARCHAR(255) -- URL of a video about the variety
);

-- Table to store information about production areas
CREATE TABLE production_areas (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the production area
    name VARCHAR(255) NOT NULL, -- Name of the production area
    latitude DECIMAL(10, 8) NOT NULL, -- Latitude of the production area
    longitude DECIMAL(11, 8) NOT NULL, -- Longitude of the production area
    variety_id INT, -- Foreign key referencing the variety grown in this area
    FOREIGN KEY (variety_id) REFERENCES varieties(id)
);

-- Table to store information about farmers
CREATE TABLE farmers (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the farmer
    name VARCHAR(255) NOT NULL, -- Name of the farmer
    brand_name VARCHAR(255), -- Brand name of the farmer (if any)
    contact_info VARCHAR(255), -- Contact information for the farmer
    image_url VARCHAR(255), -- URL of an image of the farmer or their farm
    area_id INT, -- Foreign key referencing the production area of the farmer
    FOREIGN KEY (area_id) REFERENCES production_areas(id)
);

-- Table to store user comments about varieties
CREATE TABLE comments (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the comment
    user_name VARCHAR(255) NOT NULL, -- Name of the user who made the comment
    comment_text TEXT NOT NULL, -- The text of the comment
    variety_id INT, -- Foreign key referencing the variety commented on
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the comment was created
    FOREIGN KEY (variety_id) REFERENCES varieties(id)
);

-- Table to store likes for varieties
CREATE TABLE likes (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the like
    variety_id INT, -- Foreign key referencing the variety liked
    user_identifier VARCHAR(255) NOT NULL, -- Unique identifier for the user (e.g., IP address or user ID)
    UNIQUE(variety_id, user_identifier), -- Ensures a user can only like a variety once
    FOREIGN KEY (variety_id) REFERENCES varieties(id)
);
