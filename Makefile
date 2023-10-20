.PHONY: build
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
up:
	docker-compose -f docker-compose.yml up

.PHONY: bash
bash:
	docker exec -it healthcheck-decorator bash

.PHONY: instal_package
instal_package:
	docker exec -it healthcheck-decorator pip install .

.PHONY: test
test:
	docker exec -it healthcheck-decorator pytest