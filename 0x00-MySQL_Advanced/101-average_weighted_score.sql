-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  -- Note: could've user cursor with a control flow stmt
  UPDATE users
  JOIN (
    SELECT user_id, SUM(score * weight) / SUM(weight) AS new_average
    FROM corrections
    INNER JOIN projects
    ON corrections.project_id = projects.id
    GROUP BY user_id
  ) AS user_scores ON users.id = user_scores.user_id
  SET users.average_score = user_scores.new_average;
END |
DELIMITER ;
