USE ds_prj;

CREATE TABLE ticket_order(
  ticket_id INT PRIMARY KEY AUTO_INCREMENT,
  phone_num INT NOT NULL,
  show_name VARCHAR(64) NOT NULL,
  ticket_num INT NOT NULL,
  ticket_price INT NOT NULL,
  total_price INT NOT NULL,
  order_date DATE NOT NULL
);
