
Summary:	A Better CD Encoder
Name:		abcde
Version:	2.0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://lly.org/~rcw/abcde/%{name}_%{version}.orig.tar.gz
URL:		http://lly.org/~rcw/abcde/page/
Requires:	cd-discid >= 0.7
Requires:	wget >= 1.8.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abcde is a frontend to cdparanoia, wget, cd-discid, id3, and your favorite
Ogg/MP3 encoder (Oggenc is the default). It grabs an entire CD and converts
each track to Ogg/MP3, then comments or ID3-tags each file, all with one
command. It supports parallelization, SMP, HTTP proxies, customizable
filename organization and munging, playlist generation, and remote
distributed encoding via distmp3.

%description -l pl
Abcde jest nak³adk± na takie programy jak cdparanoia, wget, cd-discid, id3
oraz Twój ulubiony kodek Ogg/Mp3 (standardowym kodekiem jest Oggenc).
Abcde ¶ci±ga wszystkie ¶cie¿ki z kompaktu,  konwertuje je do odpowiedniego
formatu, a nastêpnie dodaje do utworzonych plików tagi ID3 - wszystko za
pomoc± jednej komendy. Skrypt umo¿liwia równoleg³± pracê poszczególnych
komponentów, wspiera SMP, proxy HTTP oraz zdalne kodowanie za pomoc±
distmp3.

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
%doc README changelog TODO
%attr(755,root,root) %{_bindir}/*
%verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/abcde.conf
%{_mandir}/man1/*
