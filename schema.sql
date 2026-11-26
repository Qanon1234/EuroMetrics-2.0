CREATE TABLE geography (
    country_code VARCHAR(12) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    region VARCHAR(20),
    entity_type VARCHAR(20) NOT NULL DEFAULT 'country'
);

CREATE TABLE indicator (
    indicator_id INT PRIMARY KEY AUTO_INCREMENT,
    indicator_name VARCHAR(100) NOT NULL,
    unit VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    source_dataset VARCHAR(100) NOT NULL
);

CREATE TABLE observation (
    country_code VARCHAR(12) NOT NULL,
    indicator_id INT NOT NULL,
    year INT NOT NULL,
    value DECIMAL(20,6) NOT NULL,
    quality_flag VARCHAR(20),

    PRIMARY KEY (country_code, indicator_id, year),

    FOREIGN KEY (country_code)
        REFERENCES geography(country_code),

    FOREIGN KEY (indicator_id)
        REFERENCES indicator(indicator_id)
);