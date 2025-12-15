%define oname python_dotenv
%bcond_without tests

Name:		python-dotenv
Version:	1.2.1
Release:	1
Group:		Development/Python
Summary:	Python module for adding key-value pairs from .env files to the environment
License:	BSD-3-Clause
URL:		https://pypi.org/project/python-dotenv/
Source0:	https://pypi.python.org/packages/source/p/python-dotenv/%{oname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(ipython)
BuildRequires:	python%{pyver}dist(sh)
%endif


%description
Reads the key-value pair from .env file and adds them to environment variable.
It is great for managing app settings during development and in production
using 12-factor principles.

%prep
%autosetup -n %{oname}-%{version} -p1

# Remove upstream egg-info
rm -rf src/%{oname}.egg-info

%build
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
# CLI tests require distribution to be found, and the correct executable installed
export PATH="%{buildroot}%{_bindir}:$PATH"
export PYTHONPATH="%{buildroot}%{python_sitelib}:%{buildroot}%{python_sitelib}:${PWD}"
%{__python} -m pytest -v
%endif

%files
%{_bindir}/dotenv
%{python_sitelib}/dotenv/
%{python_sitelib}/%{oname}-%{version}*.*-info
%license LICENSE
%doc README.md
