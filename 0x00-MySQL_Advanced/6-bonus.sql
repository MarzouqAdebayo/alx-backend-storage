-- Creates a stored procedure AddBonus that adds
-- a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER |
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
  DECLARE project_exists INT DEFAULT 0;
  DECLARE project_id INT DEFAULT 0;

  -- check if project_name exists on project table
  SELECT
    COUNT(id) INTO project_exists
  FROM
    projects
  WHERE
    name = project_name;

  -- if it does not exist insert new project_name into project tabel
  IF project_exists = 0 THEN
    INSERT INTO
      projects(name)
    VALUES
      (project_name);
  END IF;

  SELECT
    id INTO project_id
  FROM
    projects
  WHERE
    name = project_name;

  INSERT INTO
    corrections(user_id, project_id, score)
  VALUES
    (user_id, project_id, score);
END |
DELIMITER ;
