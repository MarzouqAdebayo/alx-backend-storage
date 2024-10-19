-- Creates an index idx_name_first on the table names
-- and the first leter of name
DROP INDEX idx_name_first if EXISTS;
CREATE INDEX idx_name_first ON names (name(1));
