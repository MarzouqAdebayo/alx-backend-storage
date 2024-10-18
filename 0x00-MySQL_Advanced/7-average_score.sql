-- Creates a stored procedure ComputeAverageScoreForUser that computes
-- and stores the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
  UPDATE users
  SET users.average_score = IFNULL((
    SELECT AVG(score)
    FROM corrections
    WHERE corrections.user_id = user_id
  ), 0)
  WHERE users.id = user_id;
END |
DELIMITER ;
