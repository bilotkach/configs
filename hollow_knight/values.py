bosses_url = 'https://hollowknight.fandom.com/wiki/Category:Bosses_(Hollow_Knight)'
url = 'https://hollowknight.fandom.com'
create_db = 'CREATE DATABASE IF NOT EXISTS hollow_knight;'
create_table = """
CREATE TABLE IF NOT EXISTS bosses(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    hp_nail_lvl0 FLOAT,
    hp_nail_lvl1 FLOAT,
    hp_nail_lvl2 FLOAT,
    hp_nail_lvl3 FLOAT,
    hp_nail_lvl4 FLOAT,
    PRIMARY KEY (id),
    UNIQUE KEY (name)
)"""
