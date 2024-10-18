-- Creates a stored procedure ComputeAverageScoreForUser that computes
-- and stores the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
  DECLARE avg_score FLOAT DEFAULT 0;

  select avg(score) into avg_score from corrections where corrections.user_id = 2;

  UPDATE users
  SET users.average_score = avg_score
  WHERE users.id = user_id;
END |
DELIMITER ;
