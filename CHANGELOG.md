# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.0.3] - 2018-01-21

### Added
- `graphite.metrics` method to see which metrics module is currently collecting
- Ability to configure polling and pushing intervals

### Removed
- `box.stat.net().EVENTS` and `box.stat.net().LOCKS` metrics from collecting

## [0.0.2] - 2018-01-17

### Fixed
- Fix "assign to undeclared variable" runtime error
- Fix rpm spec to include initialization file

## [0.0.1] - 2018-01-11

### Added
- Support basic tarantool statistics like box.slab.info() and box.stat.net()
- Support adding custom sec metrics using **add_sec_metric** function
- Luarocks packaging
- RPM packaging
- Basic test checking module is loadable
- Travis CI configuration
