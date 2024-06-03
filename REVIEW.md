## Task review by Ignas

The task review is composed of two parts - a general overview here and comments in the code.

## Pros

1. Clean project structure in `event_consumer`.

2. Taken extra step with authentication.

3. Kudos for using type hints.

4. Good usage of Python tooling like Pydantic and Poetry.


## Cons

1. Wasn't able to run the services out of the box, since it's implied that the DB has to be setup beforehand.

2. The project structure isn't too clear, especially in the `event_propagator` service. All the event reading/sending logic is stored in a file named `utils`, which isn't 

3. Only the database submodule is covered with tests.

4. Missed some breaking edge cases, specifically in `utils.read_events`.

5. Missing validation on environment variables. Would be better to use something like `pydantic_settings.BaseSettings` instead of a plain `os.getenv`.

6. Some code was made with 4 nesting levels, which makes it hard to read and test.

7. Usage of syncrhonous I/O methods in an async context.