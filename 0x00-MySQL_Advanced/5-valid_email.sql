-- Creates trigger that resets the attribute valid_email
-- only when the email has been changed
DROP TRIGGER IF EXISTS update_valid_email;
DELIMITER |
CREATE TRIGGER update_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
  	SET NEW.valid_email = 0;
  END IF;
END |
DELIMITER ;
