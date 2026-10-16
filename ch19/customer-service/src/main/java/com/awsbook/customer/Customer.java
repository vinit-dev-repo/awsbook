package com.awsbook.customer;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.Id;
import java.util.List;

@Entity
public class Customer {
    @Id
    private Integer id;
    private String name;
    @Enumerated(EnumType.STRING)
    private Genre favoriteGenre;

    public Genre getFavoriteGenre() {
        return favoriteGenre;
    }

    public void setFavoriteGenre(Genre genre) {
        this.favoriteGenre = genre;
    }

    public CustomerDto toDto(List<MovieDto> movies) {
        return new CustomerDto(id, name, favoriteGenre, movies);
    }
}
