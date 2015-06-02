Summary:	X keyboard shortcuts.
Name:		keybinder
Version:	0.3.0
Release:	1
License:	MIT
URL:		http://kaizer.se/wiki/keybinder
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/%{name}/%{name}-%{version}.tar.gz/2a0aed62ba14d1bf5c79707e20cb4059/%{name}-%{version}.tar.gz
BuildRequires:	intltool gtk2-devel glib-devel gdk-pixbuf-devel cairo-devel libX11-devel pango-devel atk-devel pixman-devel libpng-devel libXrender-devel libXext-devel harfbuzz-devel python2-libs python2-devel pygtk
#intltool glib-devel gtk2-devel menu-cache-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel harfbuzz-devel libpng-devel libXrender-devel libXext-devel libX11-devel libfm-devel
Requires:	gtk2 pygtk
#glib gtk2 menu-cache cairo pango gdk-pixbuf atk pixman harfbuzz libpng libXrender libfm
%description
The keybinder2 package contains a utility library registering global X keyboard shortcuts.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --disable-lua
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.3.0-1
-	initial version
