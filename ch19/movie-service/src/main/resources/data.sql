INSERT INTO movie (id, title, release_year, genre) VALUES
  (1, 'Inception', 2010, 'ACTION'),
  (2, 'The Godfather', 1972, 'CRIME'),
  (3, 'Monty Python and the Holy Grail', 1975, 'COMEDY'),
  (4, 'The Shawshank Redemption', 1994, 'DRAMA'),
  (5, 'Mad Max: Fury Road', 2015, 'ACTION'),
  (6, 'Die Hard', 1988, 'ACTION'),
  (7, 'Pulp Fiction', 1994, 'CRIME'),
  (8, 'Superbad', 2007, 'COMEDY'),
  (9, 'Forrest Gump', 1994, 'DRAMA')
ON CONFLICT (id) DO NOTHING;
