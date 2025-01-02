-- CREATE DATABASE facebook;

-- CREATE TABLE users(
--     gmail VARCHAR(100) primary key,
--     user_password VARCHAR(100)
-- );

-- CREATE TABLE profiles(
--     gmail VARCHAR(100) primary key,
--     username VARCHAR(100),
--     profile_image_path VARCHAR(100),
--     gender VARCHAR(100),
--     education VARCHAR(100),
--     phone VARCHAR(100),
--     birthday VARCHAR(100)
-- );

-- CREATE TABLE posts(
--     post_id INT primary key,
--     sender_gmail VARCHAR(100),
--     send_date VARCHAR(100),
--     content VARCHAR(1000),
--     react_number INT
-- );

-- CREATE TABLE reacted_posts(
--     post_id INT,
--     gmail VARCHAR(100)
-- );

-- CREATE TABLE followers(
--     follower_gmail VARCHAR(100),
--     followed_gmail VARCHAR(100)
-- );

-- CREATE TABLE variables(
--     id INT primary key,
--     post_number INT
-- );

-- INSERT INTO variables VALUES(1, 0);

SELECT * FROM users;
SELECT * FROM profiles;
SELECT * FROM posts;
SELECT * FROM reacted_posts;
SELECT * FROM followers;
SELECT * FROM variables;