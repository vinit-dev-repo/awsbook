package com.awsbook.movie;

import java.util.List;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.resttestclient.autoconfigure.AutoConfigureRestTestClient;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.annotation.Import;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.test.web.servlet.client.RestTestClient;

@Import(TestContainersConfiguration.class)
@AutoConfigureRestTestClient
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class MovieServiceApplicationTests {
    @Autowired
    private RestTestClient client;

    @Test
    void health() {
        client.get().uri("/actuator/health").exchange().expectStatus().is2xxSuccessful();
    }

    @Test
    void allMovies() {
        Assertions.assertEquals(9, movies("/api/movies").size());
    }

    @Test
    void actionMovies() {
        var action = movies("/api/movies/ACTION");
        Assertions.assertEquals(3, action.size());
        Assertions.assertTrue(action.stream().allMatch(m -> m.genre() == Genre.ACTION));
    }

    private List<MovieDto> movies(String uri) {
        return client.get().uri(uri).exchange().expectStatus().is2xxSuccessful()
                .expectBody(new ParameterizedTypeReference<List<MovieDto>>() { }).returnResult().getResponseBody();
    }
}
