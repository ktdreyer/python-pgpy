%global pypi_name pgpy
%global pypi_version 0.6.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Pretty Good Privacy for Python

License:        BSD-3-Clause
URL:            https://github.com/SecurityInnovation/PGPy
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/PGPy-%{pypi_version}.tar.gz
Patch0001:      cryptography-min-version.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyasn1)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
PGPy: Pretty Good Privacy for Python :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PGPy: Pretty Good Privacy for Python :target:

%prep
%autosetup -n PGPy-%{pypi_version}

%build
%py3_build

%install
%py3_install

%check
# Tests fail on RHEL 9 due to sha1 deprecation:
# https://github.com/SecurityInnovation/PGPy/issues/438
%if 0%{?el9}
py.test-%{python3_version} -v tests/ || :
%else
py.test-%{python3_version} -v tests/
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Fri May 26 2023 Ken Dreyer <kdreyer@redhat.com> - 0.6.0-1
- Initial package.
