Summary:	A Better CD Encoder
Name:		abcde
Version:	-
Release:	-
Epoch:		-
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		-
Source0:	http://lly.org/~rcw/abcde/%{name}_%{version}.orig.tar.gz
Source1:	-
Patch0:		-
URL:		http://lly.org/~rcw/abcde/page/
BuildRequires:	-
PreReq:		-
Requires:	-
Requires(pre,post):	-
Requires(preun):	-
Requires(postun):	-
Provides:	-
Obsoletes:	-
Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abcde is a frontend to cdparanoia, wget, cd-discid, id3, and your favorite
Ogg/MP3 encoder (Oggenc is the default). It grabs an entire CD and converts
each track to Ogg/MP3, then comments or ID3-tags each file, all with one
command. It supports parallelization, SMP, HTTP proxies, customizable
filename organization and munging, playlist generation, and remote
distributed encoding via distmp3.


%package subpackage
Summary:	-
Summary(pl):	-
Group:		-

%description subpackage

%description subpackage -l pl

%prep
%setup -q -n %{name}-%{version}.orig -a 1
%patch0 -p1

%build
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files subpackage
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
