Summary:	redglass and whiteglass animated cursor themes.
Name:		xcursor-themes
Version:	1.0.4
Release:	1
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.x.org/pub/individual/data/%{name}-%{version}.tar.bz2
BuildRequires:	util-macros xorg-applications libXcursor-devel libX11-devel libXrender-devel libXfixes-devel
Requires:	libXcursor libX11 libXrender libXfixes
%description
The xcursor-themes package contains the redglass and whiteglass animated cursor themes.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_prefix}/*
%changelog
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 1.0.4-1
-	initial version
