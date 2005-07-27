Summary:	GTK2 client for MPD
Name:		glurp
Version:	0.11.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/glurp/%{name}-%{version}.tar.gz
# Source0-md5:	17d1c780fe006b51886d774e387d0269
URL:		http://www.musicpd.org/glurp.shtml
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK2 based graphical MPD client with simple and clean interface.

%prep
%setup -q 

%build
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
