#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Generate and parse RFC 3339 timestamps
Summary(pl.UTF-8):	Generowanie i analiza znaczników czasu RFC 3339
Name:		python-pyrfc3339
Version:	1.1
Release:	7
License:	MIT
#Source0Download: https://pypi.org/simple/pyRFC3339/
Source0:	https://files.pythonhosted.org/packages/source/p/pyRFC3339/pyRFC3339-%{version}.tar.gz
# Source0-md5:	c829980738b8271b0179ffd0c41187b0
Group:		Libraries/Python
URL:		https://pypi.org/project/pyRFC3339/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-pytz
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
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

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę Pythona 2 do analizy i generowania
znaczników czasu zgodnych z RFC 3339 przy użyciu obiektów Pythona
datetime.datetime.

%package -n python3-pyrfc3339
Summary:	Generate and parse RFC 3339 timestamps
Summary(pl.UTF-8):	Generowanie i analiza znaczników czasu RFC 3339
Group:		Libraries/Python

%description -n python3-pyrfc3339
This package contains a Python 3 library to parse and generate RFC
3339-compliant timestamps using Python datetime.datetime objects.

%description -n python3-pyrfc3339 -l pl.UTF-8
Ten pakiet zawiera bibliotekę Pythona 2 do analizy i generowania
znaczników czasu zgodnych z RFC 3339 przy użyciu obiektów Pythona
datetime.datetime.

%prep
%setup -q -n pyRFC3339-%{version}

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
%{py_sitescriptdir}/pyRFC3339-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyrfc3339
%defattr(644,root,root,755)
%doc README.rst LICENSE.txt
%{py3_sitescriptdir}/pyrfc3339
%{py3_sitescriptdir}/pyRFC3339-%{version}-py*.egg-info
%endif
