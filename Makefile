format:
	black src/
	ruff check --fix-only src/

lint:
	black --check src/
	ruff check src/
	mypy --install-types --non-interactive src/

rebuild:
	docker-compose up -d --build bot

logs:
	docker-compose logs -f bot

shell:
	docker-compose exec bot bash