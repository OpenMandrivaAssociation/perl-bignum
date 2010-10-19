%define upstream_name	 bignum
%define upstream_version 0.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Transparent BigNumber support for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-Math-BigInt >= 1.87
BuildRequires: perl-Math-BigRat >= 0.20
BuildRequires: perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
All operators (including basic math operations) are overloaded. Integer and
floating-point constants are created as proper BigInts or BigFloats,
respectively.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL5LIB=%{perl_vendorlib}
%{__perl} Makefile.PL installdirs=vendor
%make

%check
export PERL5LIB=%{perl_vendorlib}/
make test

%clean 
rm -rf %buildroot

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root)
%doc BUGS LICENSE TODO README CHANGES
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Math
%{_mandir}/*/*
