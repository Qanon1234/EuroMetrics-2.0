GET_PPS_DATA = """
    SELECT geography.country_name,
           geography.region,
           observation.year,
           observation.value AS pps_index,
           observation.quality_flag
    FROM observation
    JOIN geography
        ON observation.country_code = geography.country_code
    WHERE observation.indicator_id = 1
"""