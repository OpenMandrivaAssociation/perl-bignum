%define upstream_name	 bignum
%define upstream_version 0.51

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Transparent BigNumber support for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Math-BigInt >= 1.87
BuildRequires:	perl-Math-BigRat >= 0.20
BuildRequires:	perl-devel

%description
All operators (including basic math operations) are overloaded. Integer and
floating-point constants are created as proper BigInts or BigFloats,
respectively.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL5LIB=%{perl_vendorlib}
perl Makefile.PL installdirs=vendor
%make

%check
export PERL5LIB=%{perl_vendorlib}/
make test

%install
%makeinstall_std

%files
%doc BUGS LICENSE TODO README CHANGES
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Math
%{_mandir}/*/*

%changelog
* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2011.0
+ Revision: 586763
- new version

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 402087
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.23-2mdv2009.0
+ Revision: 268897
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.0
+ Revision: 193749
- update to new version 0.23

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.0
+ Revision: 78390
- import perl-bignum


* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.0
- first mdv release
