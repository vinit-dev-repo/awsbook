package com.awsbook.customer;

import java.util.List;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.resttestclient.autoconfigure.AutoConfigureRestTestClient;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.annotation.Import;
import org.springframework.http.ProblemDetail;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.web.servlet.client.RestTestClient;

@Import(TestContainersConfiguration.class)
@AutoConfigureRestTestClient
@MockitoBean(types = MovieClient.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class CustomerServiceApplicationTests {
    @Autowired
    private RestTestClient client;
    @Autowired
    private MovieClient movieClient;

    @Test
    void health() {
        client.get().uri("/actuator/health").exchange().expectStatus().is2xxSuccessful();
    }

    @Test
    void customerWithMovies() {
        Mockito.when(movieClient.getMovies(Mockito.any(Genre.class))).thenReturn(List.of(
                new MovieDto(1, "movie-1", 1990, Genre.ACTION), new MovieDto(2, "movie-2", 1991, Genre.ACTION)));
        var dto = client.get().uri("/api/customers/1").exchange().expectStatus().is2xxSuccessful()
                .returnResult(CustomerDto.class).getResponseBody();
        Assertions.assertNotNull(dto);
        Assertions.assertEquals("Sam", dto.name());
        Assertions.assertEquals(2, dto.recommendedMovies().size());
    }

    @Test
    void customerNotFound() {
        var problem = client.get().uri("/api/customers/10").exchange().expectStatus().is4xxClientError()
                .returnResult(ProblemDetail.class).getResponseBody();
        Assertions.assertNotNull(problem);
        Assertions.assertEquals("Customer Not Found", problem.getTitle());
    }

    @Test
    void updateGenre() {
        client.patch().uri("/api/customers/1/genre").body(new GenreUpdateRequest(Genre.DRAMA)).exchange()
                .expectStatus().isNoContent().expectBody().isEmpty();
    }
}
