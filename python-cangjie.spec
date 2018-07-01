#
# Conditional build:
%bcond_with	python2 # CPython 2.x module [not supported as of 1.2]
%bcond_without	python3 # CPython 3.x module

Summary:	Python wrapper for libcangjie, the library implementing the Cangjie input method
Summary(pl.UTF-8):	Interfejs Pythona do libcangjie - biblioteki implementującej metodę wprowadzania Cangjie
Name:		python-cangjie
Version:	1.2
Release:	4
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/Cangjians/pycangjie/releases
Source0:	https://github.com/Cangjians/pycangjie/releases/download/v%{version}/cangjie-%{version}.tar.xz
# Source0-md5:	bcdd86b5cc9c2deef95214e0852a1ee0
Patch0:		%{name}-cython.patch
URL:		https://github.com/Cangjians/pycangjie
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	libcangjie-devel >= 1.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-Cython >= 0.14
BuildRequires:	python-devel >= 2.0
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.14
BuildRequires:	python3-devel >= 1:3.2.3
%endif
Requires:	libcangjie >= 1.0
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python wrapper to libcangjie, the library implementing the
Cangjie input method (for Chinese).

%description -l pl.UTF-8
Ten pakiet zawiera interfejs Pythona do libcangjie - biblioteki
implementującej metodę wprowadzania znaków chińskich Cangjie.

%package -n python3-cangjie
Summary:	Python 3 wrapper for libcangjie, the library implementing the Cangjie input method
Summary(pl.UTF-8):	Interfejs Pythona 3 do libcangjie - biblioteki implementującej metodę wprowadzania Cangjie
Group:		Libraries/Python
Requires:	libcangjie >= 1.0
Requires:	python3-libs >= 1:3.2.3

%description -n python3-cangjie
This is a Python 3 wrapper to libcangjie, the library implementing the
Cangjie input method (for Chinese).

%description -n python3-cangjie -l pl.UTF-8
Ten pakiet zawiera interfejs Pythona 3 do libcangjie - biblioteki
implementującej metodę wprowadzania znaków chińskich Cangjie.

%prep
%setup -q -n cangjie-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/cangjie/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS README.md docs/*.md
%dir %{py_sitedir}/cangjie
%endif

%if %{with python3}
%files -n python3-cangjie
%defattr(644,root,root,755)
%doc AUTHORS README.md docs/*.md
%dir %{py3_sitedir}/cangjie
%attr(755,root,root) %{py3_sitedir}/cangjie/_core.so
%attr(755,root,root) %{py3_sitedir}/cangjie/errors.so
%attr(755,root,root) %{py3_sitedir}/cangjie/filters.so
%attr(755,root,root) %{py3_sitedir}/cangjie/versions.so
%{py3_sitedir}/cangjie/__init__.py
%{py3_sitedir}/cangjie/__pycache__
%endif
