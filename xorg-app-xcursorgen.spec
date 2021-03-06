Summary:	xcursorgen application - create an X cursor file from a collection of PNG images
Summary(pl.UTF-8):	Aplikacja xcursorgen do tworzenia pliku kursora X ze zbioru obrazów PNG
Name:		xorg-app-xcursorgen
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xcursorgen-%{version}.tar.bz2
# Source0-md5:	25cc7ca1ce5dcbb61c2b471c55e686b5
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcursorgen creates an X cursor file from a collection of PNG images.

%description -l pl.UTF-8
xcursorgen tworzy plik kursora X ze zbioru obrazów PNG.

%prep
%setup -q -n xcursorgen-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xcursorgen
%{_mandir}/man1/xcursorgen.1*
