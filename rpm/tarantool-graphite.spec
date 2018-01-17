Name: tarantool-graphite
Version: 0.0.2
Release: 1%{?dist}
Summary: Tarantool module for pushing basic and custom metrics into graphite
Group: Applications/Databases
License: BSD
URL: https://github.com/tarantool/graphite
Source0: https://github.com/tarantool/graphite/archive/%{version}.tar.gz
BuildArch: noarch
BuildRequires: tarantool >= 1.6.8.0
BuildRequires: tarantool-devel >= 1.6.8.0
Requires: tarantool >= 1.6.8.0

%description
This package collects basic metrics from box.stat(), format and send it to specified graphite host.
It is also possible to add custom metrics.

%prep
%setup

%install
mkdir -p %{buildroot}%{_datadir}/tarantool/graphite/
cp -av %{_builddir}/tarantool-graphite-%{version}/graphite/*.lua %{buildroot}%{_datadir}/tarantool/graphite/

%clean
rm -rf %{buildroot}

%files
%dir %{_datadir}/tarantool/graphite/
%{_datadir}/tarantool/graphite/init.lua
%doc README.md
