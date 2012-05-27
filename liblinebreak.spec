Summary:	Unicode line breaking library
Summary(pl.UTF-8):	Biblioteka łamania wierszy zgodnie z Unikodem
Name:		liblinebreak
Version:	2.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/vimgadgets/%{name}-%{version}.tar.gz
# Source0-md5:	9fe73b4b230434765be2305e50f8fe45
URL:		http://vimgadgets.sourceforge.net/liblinebreak/
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liblinebreak is an implementation of the line breaking algorithm as
described in Unicode 6.0.0 Standard Annex 14, Revision 26. It breaks
lines that contain Unicode characters. It is designed to be used in a
generic text renderer. FBReader is one real-world example, and you may
also check some simple sample code, like showbreak and breaktext.

%description -l pl.UTF-8
Liblinebreak to implementacja algorytmu łamania wierszy opisanego w
standardzie Unicode 6.0.0, Annex 14, Revision 26. Obsługuje łamanie
wierszy zawierających znaki unikodowe. Jest zaprojektowana do używania
w ogólnym kodzie renderującym tekst. Rzeczywistym przykładem jest
FBReader, prostsze programy przykładowe to showbreak i breaktext.

%package devel
Summary:	Header files for liblinebreak library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblinebreak
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for liblinebreak library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblinebreak.

%package static
Summary:	Static liblinebreak library
Summary(pl.UTF-8):	Statyczna biblioteka liblinebreak
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblinebreak library.

%description static -l pl.UTF-8
Statyczna biblioteka liblinebreak.

%package apidocs
Summary:	liblinebreak API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki liblinebreak
Group:		Documentation

%description apidocs
API and internal documentation for liblinebreak library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki liblinebreak.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENCE NEWS README
%attr(755,root,root) %{_libdir}/liblinebreak.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblinebreak.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblinebreak.so
%{_libdir}/liblinebreak.la
%{_includedir}/linebreak*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblinebreak.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
