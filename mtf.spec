Summary:	A Linux reader for the Microsoft Tape Format used by NT Backup
Name:		mtf
Version:	0.2.1
Release:	%mkrel 8
License:	GPL
Group:		Archiving/Backup
URL:		http://www.layton-graphics.com/mtf/
Source:		%{name}-%{version}.tar.bz2

%description
A bare-bones reader for Microsoft Tape Format tapes.
This program is based on Microsoft Tape Format Specification Version 1.00a.
Software compression and archives that span tapes are not yet supported.

%prep
%setup -q -n %{name}-%{version}

%build
make CFLAGS="%{optflags}"

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install mtf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc README
%{_bindir}/mtf
