#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-hatch_vcs
Version  : 0.2.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/ac/13/b3d83564c0cc0f1d45b4ea2a78b87b383a8165797613fedf11f1a7e49b48/hatch_vcs-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/13/b3d83564c0cc0f1d45b4ea2a78b87b383a8165797613fedf11f1a7e49b48/hatch_vcs-0.2.0.tar.gz
Summary  : Hatch plugin for versioning with your preferred VCS
Group    : Development/Tools
License  : MIT
Requires: pypi-hatch_vcs-license = %{version}-%{release}
Requires: pypi-hatch_vcs-python = %{version}-%{release}
Requires: pypi-hatch_vcs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)

%description
# hatch-vcs
| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/ofek/hatch-vcs/actions/workflows/test.yml/badge.svg)](https://github.com/ofek/hatch-vcs/actions/workflows/test.yml) [![CD - Build](https://github.com/ofek/hatch-vcs/actions/workflows/build.yml/badge.svg)](https://github.com/ofek/hatch-vcs/actions/workflows/build.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/hatch-vcs.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/hatch-vcs/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-vcs.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/hatch-vcs/) |
| Meta | [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/ambv/black) [![imports - isort](https://img.shields.io/badge/imports-isort-ef8336.svg)](https://github.com/pycqa/isort) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/ofek?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/ofek) |

%package license
Summary: license components for the pypi-hatch_vcs package.
Group: Default

%description license
license components for the pypi-hatch_vcs package.


%package python
Summary: python components for the pypi-hatch_vcs package.
Group: Default
Requires: pypi-hatch_vcs-python3 = %{version}-%{release}

%description python
python components for the pypi-hatch_vcs package.


%package python3
Summary: python3 components for the pypi-hatch_vcs package.
Group: Default
Requires: python3-core
Provides: pypi(hatch_vcs)
Requires: pypi(hatchling)
Requires: pypi(setuptools_scm)

%description python3
python3 components for the pypi-hatch_vcs package.


%prep
%setup -q -n hatch_vcs-0.2.0
cd %{_builddir}/hatch_vcs-0.2.0
pushd ..
cp -a hatch_vcs-0.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401710
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hatch_vcs
cp %{_builddir}/hatch_vcs-0.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-hatch_vcs/b3936813743ef137cd182296341f43e3365b9a67
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hatch_vcs/b3936813743ef137cd182296341f43e3365b9a67

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
