Name:		python-dotenv
Version:	1.0.1
Release:	1
Group:		Development/Python
Summary:	Python module for adding key-value pairs from .env files to the environment
License:	BSD-3-Clause
URL:		https://pypi.org/project/python-dotenv/
Source0:	https://pypi.python.org/packages/source/p/python-dotenv/python-dotenv-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Reads the key-value pair from .env file and adds them to environment variable.
It is great for managing app settings during development and in production
using 12-factor principles.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/dotenv
%{python_sitelib}/*
%license LICENSE
%doc README.md