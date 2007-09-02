%define module	bignum
%define name	perl-%{module}
%define version 0.22
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Transparent BigNumber support for Perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.gz
BuildRequires:  perl-Math-BigInt >= 1.87
BuildRequires:  perl-Math-BigRat >= 0.20
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
All operators (including basic math operations) are overloaded. Integer and
floating-point constants are created as proper BigInts or BigFloats,
respectively.

%prep
%setup -q -n %{module}-%{version}

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

