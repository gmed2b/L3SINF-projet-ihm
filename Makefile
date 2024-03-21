run-api:
	docker compose up -d --build

clean-api:
	docker compose down

run-ihm: 
	python3 ihm/main.py

.PHONY: run-api clean-api run-ihm