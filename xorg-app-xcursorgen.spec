Summary:	xcursorgen application - create an X cursor file from a collection of PNG images
Summary(pl.UTF-8):	Aplikacja xcursorgen do tworzenia pliku kursora X ze zbioru obrazów PNG
Name:		xorg-app-xcursorgen
Version:	1.0.3
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xcursorgen-%{version}.tar.bz2
# Source0-md5:	69df079b3950a0db4e5f4e6f0e00ddee
Patch0:		%{name}-libpng.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcursorgen creates an X cursor file from a collection of PNG images.

%description -l pl.UTF-8
xcursorgen tworzy plik kursora X ze zbioru obrazów PNG.

%prep
%setup -q -n xcursorgen-%{version}
%patch0 -p1

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xcursorgen
%{_mandir}/man1/xcursorgen.1x*
