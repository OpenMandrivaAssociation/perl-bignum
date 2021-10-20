# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

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
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-devel

%description
All operators (including basic math operations) are overloaded. Integer and
floating-point constants are created as proper BigInts or BigFloats,
respectively.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
export PERL5LIB=%{perl_vendorlib}
perl Makefile.PL installdirs=vendor
%make_build

%check
export PERL5LIB=%{perl_vendorlib}/
make test

%install
%make_install

%files
%doc BUGS LICENSE TODO README CHANGES
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Math
%doc %{_mandir}/*/*
