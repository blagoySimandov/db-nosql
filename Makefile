.PHONY: start-db stop-db clean-db

start-db:
	docker compose up -d

stop-db:
	docker compose down

clean-db:
	docker compose down -v
