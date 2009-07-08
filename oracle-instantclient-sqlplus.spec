# NOTE:
# - see "URL:" for download links
# - if you want to build 32-bit version, you don't have to download Source1.
#   Just comment it out.
# - if you want to build 64-bit version, comment out Source0

%define         major   11.1
%define         minor   0.7
%define         rel     0

Summary:	Oracle database client
Summary(pl.UTF-8):	Klient bazy danych Oracle
Name:		oracle-instantclient-sqlplus
Version:	%{major}.%{minor}.%{rel}
Release:	0.1
License:	OTN (proprietary, non-distributable)
Group:		Applications
Source0:	instantclient-sqlplus-linux32-%{major}.%{minor}.zip
# NoSource0-md5:	b911354a45b110d78d3691460c2bc491
Source1:	sqlplus-%{version}-linux-x86_64.zip
# NoSource1-md5:	ec20fe7fdb0a8fddd8a737b1ea9422f4
NoSource:	0
NoSource:	1
URL:		http://www.oracle.com/technology/software/tech/oci/instantclient/index.html
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		srcdir	instantclient_%(echo %{major} | tr . _)

%description
Oracle database client.

%description -l pl.UTF-8
Klient bazy danych Oracle.

%prep
%ifarch %{ix86}
%setup -q -c -T -b 0
%endif

%ifarch %{x8664}
%setup -q -c -T -b 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus}

install %{srcdir}/libsqlplusic.so $RPM_BUILD_ROOT%{_libdir}/libsqlplusic.so
install %{srcdir}/libsqlplus.so $RPM_BUILD_ROOT%{_libdir}/libsqlplus.so
install %{srcdir}/sqlplus $RPM_BUILD_ROOT%{_bindir}/sqlplus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsqlplusic.so
%attr(755,root,root) %{_libdir}/libsqlplus.so
%attr(755,root,root) %{_bindir}/sqlplus
%doc %{srcdir}/SQLPLUS_README
