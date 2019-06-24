# DEPRECATED

### Please note, this project is deprecated and no longer being maintained, please use [metrics/graphite](https://github.com/tarantool/metrics/tree/master/metrics/plugins/graphite).

[![Build Status](https://travis-ci.org/tarantool/graphite.svg?branch=master)](https://travis-ci.org/tarantool/graphite)

# Tarantool 1.6+ graphite module

## Usage examples

```lua
local graphite = require('graphite')

-- initialize standard metrics, transmit them to graphite @ 192.168.1.2:3010
graphite.init('localhost.1_instance.', '192.168.1.2', 3010)
```

## API

### Configuration

```lua
--- Defaults are:
--- send_interval = 60
--- collect_interval = 1
graphite.configure({collect_interval = 5, send_interval = 30})
```

### Metrics

```lua
-- adds new metric, values are probed every second by calling metric_fn, aggregated by calling aggr_fn on the series
graphite.add_sec_metric(name, metric_fn, aggr_fn)

graphite.sum_per_min(name, value)
graphite.sum_per_sec(name, value)
graphite.avg_per_min(name, value)
graphite.min_per_min(name, value)
graphite.max_per_min(name, value)
graphite.add(name, value) -- adds to current graphite metric value
graphite.inc(name) -- alias for graphite.add(name, 1)
```

### Aggregation functions

Builtin aggregation functions to be used with add_sec_metric

```lua
graphite.sum
graphite.sum_per_sec
graphite.max
graphite.min
graphite.last
```

### Transmission functions

``` lua
-- transmits metric value to graphite
graphite.send(name, res, timestamp)
```

## Usage examples

```lua
graphite.add_sec_metric('delete_rps_max', function() return box.stat().DELETE.rps end, graphite.max)
graphite.add('requests', 1)
graphite.max_per_min('max_mysql_query_time', query_time)
```
