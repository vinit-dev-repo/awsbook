package com.awsbook.customer;

import java.util.List;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

@Service
public class MovieClient {
    private final RestClient client;

    public MovieClient(RestClient.Builder builder, @Value("${movie.service.url}") String baseUrl) {
        this.client = builder.baseUrl(baseUrl).build();
    }

    public List<MovieDto> getMovies(Genre genre) {
        return client.get().uri("/api/movies/{genre}", genre).retrieve()
                .body(new ParameterizedTypeReference<List<MovieDto>>() { });
    }
}
