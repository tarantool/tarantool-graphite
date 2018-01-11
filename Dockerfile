FROM tarantool/tarantool:1.7

RUN set -x \
    && apk add --no-cache git

COPY . /opt/tarantool/

WORKDIR /opt/tarantool

RUN tarantoolctl rocks make rockspecs/graphite-scm-1.rockspec

CMD ["tarantool", "/opt/tarantool/example.lua"]
