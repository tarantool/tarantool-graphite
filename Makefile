DOCKER_IMAGE:=document_test

clean:
	rm -rf .test

docker_test:
	docker build -t ${DOCKER_IMAGE} -f Dockerfile.test .
	docker run \
		--rm=true --tty=true \
		${DOCKER_IMAGE} \
		tarantool /opt/tarantool/test/graphite.test.lua

test:
	tarantool test/graphite.test.lua
