Summary:	A Linux reader for the Microsoft Tape Format used by NT Backup
Name:		mtf
Version:	0.2.1
Release:	%mkrel 11
License:	GPL
Group:		Archiving/Backup
URL:		http://www.layton-graphics.com/mtf/
Source:		%{name}-%{version}.tar.bz2
Patch0:		mtf-glibc28.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A bare-bones reader for Microsoft Tape Format tapes.
This program is based on Microsoft Tape Format Specification Version 1.00a.
Software compression and archives that span tapes are not yet supported.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build
make CFLAGS="%{optflags}"

%install
rm -fr %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install mtf %{buildroot}%{_bindir}

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,755)
%doc README
%{_bindir}/mtf
