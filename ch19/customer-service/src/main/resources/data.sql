INSERT INTO customer (id, name, favorite_genre) VALUES
  (1, 'Sam', 'ACTION'),
  (2, 'Sara', 'COMEDY')
ON CONFLICT (id) DO NOTHING;
