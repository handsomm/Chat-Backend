-include .env

NAME ?= chat_backend

stag:
	git checkout development
	git pull origin development
	$(MAKE) build
	$(MAKE) migrate
	$(MAKE) clean
	$(MAKE) run

build:
	docker-compose -f docker-compose.yml -p ${NAME} build

migrate:
	docker-compose -f docker-compose.yml -p ${NAME} run --rm api python manage.py migrate
	docker-compose -f docker-compose.yml -p ${NAME} run --rm api python manage.py showmigrations
	
run:
	docker-compose -f docker-compose.yml -p ${NAME} up -d

clean:
	docker-compose -f docker-compose.yml -p ${NAME} stop pg api adminer || true
	docker-compose -f docker-compose.yml -p ${NAME} rm -f pg api adminer || true
