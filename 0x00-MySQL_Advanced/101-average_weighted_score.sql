-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
  DECLARE total_weight INT DEFAULT 0;
  DECLARE total_weighted_score INT DEFAULT 0;

  -- Fix the SELECT INTO structure
  SELECT SUM(score * weight), SUM(weight)
  INTO total_weighted_score, total_weight
  FROM corrections
  INNER JOIN projects
  ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;

  -- Update the users table
  UPDATE users
  SET users.average_score = total_weighted_score / total_weight
  WHERE users.id = user_id;
END |
DELIMITER ;
