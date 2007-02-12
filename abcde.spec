Summary:	A Better CD Encoder
Summary(pl.UTF-8):	A Better CD Encoder - lepszy koder CD
Name:		abcde
Version:	2.3.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.hispalinux.es/~data/files/%{name}_%{version}.orig.tar.gz
# Source0-md5:	94877d1e410ae420630b1048e82907d3
URL:		http://www.hispalinux.es/~data/abcde.php
Requires:	cd-discid >= 0.7
Requires:	wget >= 1.8.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abcde is a frontend to cdparanoia, wget, cd-discid, id3, and your
favorite Ogg/MP3 encoder (Oggenc is the default). It grabs an entire
CD and converts each track to Ogg/MP3, then comments or ID3-tags each
file, all with one command. It supports parallelization, SMP, HTTP
proxies, customizable filename organization and munging, playlist
generation, and remote distributed encoding via distmp3.

%description -l pl.UTF-8
Abcde jest nakładką na takie programy jak cdparanoia, wget, cd-discid,
id3 oraz Twój ulubiony kodek Ogg/MP3 (standardowym kodekiem jest
Oggenc). Abcde ściąga wszystkie ścieżki z kompaktu, konwertuje je do
odpowiedniego formatu, a następnie dodaje do utworzonych plików tagi
ID3 - wszystko za pomocą jednej komendy. Skrypt umożliwia równoległą
pracę poszczególnych komponentów, wspiera SMP, proxy HTTP oraz zdalne
kodowanie za pomocą distmp3.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install abcde cddb-tool $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install abcde.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog TODO FAQ
%attr(755,root,root) %{_bindir}/*
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/abcde.conf
%{_mandir}/man1/*
