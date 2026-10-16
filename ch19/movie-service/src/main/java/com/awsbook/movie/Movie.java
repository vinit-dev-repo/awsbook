package com.awsbook.movie;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.Id;

@Entity
public class Movie {
    @Id
    private Integer id;
    private String title;
    private Integer releaseYear;
    @Enumerated(EnumType.STRING)
    private Genre genre;

    public MovieDto toDto() {
        return new MovieDto(id, title, releaseYear, genre);
    }
}
