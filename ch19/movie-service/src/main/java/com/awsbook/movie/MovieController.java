package com.awsbook.movie;

import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/movies")
public class MovieController {
    private final MovieRepository repository;

    public MovieController(MovieRepository repository) {
        this.repository = repository;
    }

    @GetMapping
    public List<MovieDto> all() {
        return repository.findAll().stream().map(Movie::toDto).toList();
    }

    @GetMapping("/{genre}")
    public List<MovieDto> byGenre(@PathVariable Genre genre) {
        return repository.findByGenre(genre).stream().map(Movie::toDto).toList();
    }
}
