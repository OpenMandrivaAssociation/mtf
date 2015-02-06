Summary:	A Linux reader for the Microsoft Tape Format used by NT Backup
Name:		mtf
Version:	0.2.1
Release:	12
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-11mdv2011.0
+ Revision: 620414
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.1-10mdv2010.0
+ Revision: 430111
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-9mdv2009.0
+ Revision: 239078
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-8mdv2008.0
+ Revision: 83804
- rebuild


* Mon Aug 14 2006 Luca Berra <bluca@comedia.it>
+ 2006-08-13 02:32:39 (55789)
- misc spec fixes

* Mon Aug 14 2006 Luca Berra <bluca@comedia.it>
+ 2006-08-13 01:49:34 (55786)
- import mtf-0.2.1-6mdk

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-6mdk
- rebuild

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.2.1-5mdk
- build release

