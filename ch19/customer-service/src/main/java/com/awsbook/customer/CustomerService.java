package com.awsbook.customer;

import org.springframework.stereotype.Service;

@Service
public class CustomerService {
    private final MovieClient movieClient;
    private final CustomerRepository repository;

    public CustomerService(MovieClient movieClient, CustomerRepository repository) {
        this.movieClient = movieClient;
        this.repository = repository;
    }

    public CustomerDto getCustomer(Integer id) {
        var customer = repository.findById(id).orElseThrow(() -> new CustomerNotFoundException(id));
        return customer.toDto(movieClient.getMovies(customer.getFavoriteGenre()));
    }

    public void updateGenre(Integer id, GenreUpdateRequest request) {
        var customer = repository.findById(id).orElseThrow(() -> new CustomerNotFoundException(id));
        customer.setFavoriteGenre(request.favoriteGenre());
        repository.save(customer);
    }
}
