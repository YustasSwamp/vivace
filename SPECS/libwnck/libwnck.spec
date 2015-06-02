Summary:	Window Navigator Construction Kit.
Name:		libwnck
Version:	2.30.7
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.30/%{name}-%{version}.tar.xz
BuildRequires:	intltool gtk2-devel glib-devel gdk-pixbuf-devel cairo-devel libX11-devel pango-devel atk-devel pixman-devel libpng-devel libXrender-devel libXext-devel harfbuzz-devel
#intltool glib-devel gtk2-devel menu-cache-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel harfbuzz-devel libpng-devel libXrender-devel libXext-devel libX11-devel libfm-devel
Requires:	gtk2
#glib gtk2 menu-cache cairo pango gdk-pixbuf atk pixman harfbuzz libpng libXrender libfm
%description
The libwnck package contains a Window Navigator Construction Kit.
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
            --disable-static \
	    --program-suffix=-1
make %{?_smp_mflags} GETTEXT_PACKAGE=libwnck-1
%install
make DESTDIR=%{buildroot} GETTEXT_PACKAGE=libwnck-1 install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 2.30.7-1
-	initial version
