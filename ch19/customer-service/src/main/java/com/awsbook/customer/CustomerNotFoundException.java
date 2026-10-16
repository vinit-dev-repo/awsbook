package com.awsbook.customer;

public class CustomerNotFoundException extends RuntimeException {
    public CustomerNotFoundException(Integer id) {
        super("Customer [id=%d] is not found".formatted(id));
    }
}
