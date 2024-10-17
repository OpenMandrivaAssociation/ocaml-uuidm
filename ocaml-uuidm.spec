%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Universally unique identifiers (UUIDs) for OCaml
Name:		ocaml-uuidm
Version:	0.9.5
Release:	2
License:	BSD
Group:		Development/Other
Url:		https://erratique.ch/software/uuidm
Source0:	http://erratique.ch/software/uuidm/releases/uuidm-%{version}.tbz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
Uuidm is an OCaml module implementing 128 bits universally unique identifiers 
version 3, 5 (name based with MD5, SHA-1 hashing) and 4 (random based)
according to RFC 4122: http://www.ietf.org/rfc/rfc4122.txt

%files
%doc README CHANGES
%{_bindir}/uuidtrip
%dir %{_libdir}/ocaml/uuidm
%{_libdir}/ocaml/uuidm/META
%{_libdir}/ocaml/uuidm/*.cmi
%{_libdir}/ocaml/uuidm/*.cma
%{_libdir}/ocaml/uuidm/*.cmxs

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc/
%{_libdir}/ocaml/uuidm/*.cmxa
%{_libdir}/ocaml/uuidm/*.cmx
%{_libdir}/ocaml/uuidm/*.a
%{_libdir}/ocaml/uuidm/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n uuidm-%{version}

%build
ocaml setup.ml -configure --prefix %{buildroot}/usr
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

