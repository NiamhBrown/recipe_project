-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    avg_cooking_time_min numeric(5,1),
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, avg_cooking_time_min, rating) VALUES ('pizza', 30, 5);
INSERT INTO recipes (name, avg_cooking_time_min, rating) VALUES ('spagetti', 35, 4);
INSERT INTO recipes (name, avg_cooking_time_min, rating) VALUES ('toast', 5, 2);
INSERT INTO recipes (name, avg_cooking_time_min, rating) VALUES ('noodles', 20, 5);
INSERT INTO recipes (name, avg_cooking_time_min, rating) VALUES ('soup', 45, 3);

