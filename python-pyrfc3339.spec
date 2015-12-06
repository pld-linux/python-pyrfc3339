#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyRFC3339
Summary:	Generate and parse RFC 3339 timestamps
Name:		python-pyrfc3339
Version:	1.0
Release:	1
License:	MIT
Source0:	https://pypi.python.org/packages/source/p/pyRFC3339/pyRFC3339-%{version}.tar.gz
# Source0-md5:	0f7edd7ffd756a582eeef9282fecb60d
Group:		Libraries/Python
URL:		https://pypi.python.org/pypi/pyRFC3339
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
%if %{with python2}
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-pytz
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
BuildRequires:	python3-pytz
%endif
%endif
BuildArch:	noarch

%description
This package contains a Python 2 library to parse and generate RFC
3339-compliant timestamps using Python datetime.datetime objects.

%package -n python3-pyrfc3339
Summary:	Generate and parse RFC 3339 timestamps
Group:		Libraries/Python

%description -n python3-pyrfc3339
This package contains a Python 3 library to parse and generate RFC
3339-compliant timestamps using Python datetime.datetime objects.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE.txt
%{py_sitescriptdir}/pyrfc3339
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyrfc3339
%defattr(644,root,root,755)
%doc README.rst LICENSE.txt
%{py3_sitescriptdir}/pyrfc3339
%{py3_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
