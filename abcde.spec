Summary:	A Better CD Encoder
Summary(pl.UTF-8):	A Better CD Encoder - lepszy koder CD
Name:		abcde
Version:	2.9.3
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	https://abcde.einval.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	24a6e89f0e04acb6111e6be913643b12
URL:		https://abcde.einval.com/wiki/
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
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

install abcde abcde-musicbrainz-tool cddb-tool $RPM_BUILD_ROOT%{_bindir}
cp -p *.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p abcde.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ README changelog
%attr(755,root,root) %{_bindir}/abcde
%attr(755,root,root) %{_bindir}/abcde-musicbrainz-tool
%attr(755,root,root) %{_bindir}/cddb-tool
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/abcde.conf
%{_mandir}/man1/abcde.1*
%{_mandir}/man1/cddb-tool.1*
