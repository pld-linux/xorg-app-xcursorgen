Summary:	xcursorgen application
Summary(pl):	Aplikacja xcursorgen
Name:		xorg-app-xcursorgen
Version:	0.99.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xcursorgen-%{version}.tar.bz2
# Source0-md5:	88cdcc6c2e9e0a1e6cc67f02fd3f626a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcursorgen application.

%description -l pl
Aplikacja xcursorgen.

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
%attr(755,root,root) %{_bindir}/*
