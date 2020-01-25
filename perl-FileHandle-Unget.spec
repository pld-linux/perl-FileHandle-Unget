#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	FileHandle
%define	pnam	Unget
Summary:	FileHandle::Unget - FileHandle which supports multi-byte unget
Summary(pl.UTF-8):	FileHandle::Unget - FileHandle który wspiera wielobajtowe zwracanie znaków
Name:		perl-FileHandle-Unget
Version:	0.1623
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FileHandle/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27df2a78e60e30b1950bbf41740eae13
URL:		http://search.cpan.org/dist/FileHandle-Unget/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FileHandle::Unget operates exactly the same as FileHandle, except that it
provides a version of ungetc that allows you to unget more than one character.
It also provides ungets to unget a string.

This module is useful if the filehandle refers to a stream for which you can't
just seek() backwards. Some operating systems support multi-byte
ungetc(), but this is not guaranteed. Use this module if you want a
portable solution. In addition, on some operating systems, eof() will not be
reset if you ungetc after having read to the end of the file.

NOTE: Using sysread() with ungetc() and other buffering functions is
still a bad idea.

%description -l pl.UTF-8
FileHandle::Unget działa dokładnie tak samo jak FileHandle, za wyjątkiem tego,
że dostarcza wersję ungetc, która umożliwia na zwrócenie więcej niż jednego znaku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%dir %{perl_vendorlib}/FileHandle
%{perl_vendorlib}/FileHandle/Unget.pm
%{_mandir}/man3/*
