# Microservices

- https://microservices.io/

Architect software and divide it into parts called service, so that these services are

- independently deployable
- loosely coupled

## how to launch services?

- use docker `containers` to deploy services

## communication in microservices

- synchronous communication
    - using direct `http` protocol
- asynchronous communication
    - using message brokers
        - `kafka`
        - `rabbitmq`
        - `sqs/sns`  - simple queue service and simple notification service