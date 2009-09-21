Name:           ocaml-uuidm
Version:        0.9.3
Release:        %mkrel 1
Summary:        Universally unique identifiers (UUIDs) for OCaml
License:        BSD
Group:          Development/Other
URL:            http://erratique.ch/software/uuidm
Source0:        http://erratique.ch/software/uuidm/releases/uuidm-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib

%description
Uuidm is an OCaml module implementing 128 bits universally unique identifiers 
version 3, 5 (name based with MD5, SHA-1 hashing) and 4 (random based)
according to RFC 4122: http://www.ietf.org/rfc/rfc4122.txt

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uuidm-%{version}

%build
./build

%install
rm -rf %{buildroot}
INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/uuidm ./build install 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_libdir}/ocaml/uuidm
%{_libdir}/ocaml/uuidm/META
%{_libdir}/ocaml/uuidm/*.cmi
%{_libdir}/ocaml/uuidm/*.cmo
%{_libdir}/ocaml/uuidm/*.o

%files devel
%defattr(-,root,root)
%doc doc
%{_libdir}/ocaml/uuidm/*.cmx
%{_libdir}/ocaml/uuidm/*.ml
%{_libdir}/ocaml/uuidm/*.mli

