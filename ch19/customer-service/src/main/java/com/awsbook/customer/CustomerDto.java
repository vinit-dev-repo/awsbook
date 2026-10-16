package com.awsbook.customer;

import java.util.List;

public record CustomerDto(Integer id, String name, Genre favoriteGenre, List<MovieDto> recommendedMovies) { }
