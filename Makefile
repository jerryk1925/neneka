PROJECT_NAME=neneka

# Common

migrations:
	@docker exec -it neneka alembic -n alembic:dev revision --autogenerate;

migrate:
	@docker exec -it neneka alembic -n alembic:dev upgrade head;
