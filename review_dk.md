Overall:
  + good readme
  + use logging rather than prints
  + use DB as a storage (MySQL)
  + using SQLAlchemy
  + using JWT token for auth (though it was not required)
  + using recent Poetry (1.8.2) rather than requirements.txt
  + using Makefile
  + having "clean" target in the Makefile is very nice (pointing that separately)
  + few tests (anyway, they were not even required)

Code:
  + type hinting
  + linting
  + ./src/ and ./tests/ separated at the root level
  + nice main entrypoints (run_consumer & run_propagator) doing only main run things
  * config as dedicated constants
  * it would be nice to have some unified prefix set to configure via env vars
  * sync propagator
  + "ready" only when the DB connection is fine for propagator
  * DatabaseConnection() gets re-initialized on each request
  * DB calls a sync and they are called from an async function (FastAPI)
  * some logics seems to fit better in some class rather than be in utils.py


Unit tests:
  + could be more tests (sure, it was not required)


Questions / topics to discuss:
  * architecture choice
