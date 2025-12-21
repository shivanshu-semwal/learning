# System Design

- as the name suggestion designing a system
- we'll be given our problem statement
    - functional requirements
    - non functional requirements
        - how much is the acceptable downtime
        - cost considerations

- There are two levels to system design:
    - HLD - high level design - we talk about the overall structure of the design
    - LLD - low level design - we go deep and talk about the code components, some specific properties and less generic
    - Also this is a spectrum

## HLD vs LLD

- HLD
    - Architecture Patterns
    - e.g. Microservice, Monolith, Serverless
    - Building blocks - services, servers, databases
    - Communications - http, grpc, message queues
    - Rules - CAP Theorem, PACELC Theorem (for distributed systems)
- LLD
    - Design Patterns
    - e.g. Singleton, Factory, Observer, Strategy
    - Building blocks - Classes, Interfaces, Objects
    - Communication - Method calls, events, callbacks
    - Rules - SOLD Principles (for OOP), DRY, OOD

