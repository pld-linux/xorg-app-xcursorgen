Summary:	xcursorgen application - create an X cursor file from a collection of PNG images
Summary(pl.UTF-8):	Aplikacja xcursorgen do tworzenia pliku kursora X ze zbioru obrazów PNG
Name:		xorg-app-xcursorgen
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xcursorgen-%{version}.tar.bz2
# Source0-md5:	6fc90896b8c786cb1a2100b4167f7874
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
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
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xcursorgen
%{_mandir}/man1/xcursorgen.1x*
