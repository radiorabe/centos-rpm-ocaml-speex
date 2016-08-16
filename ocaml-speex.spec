Name:     ocaml-speex

Version:  0.2.1
Release:  1
Summary:  OCaml bindings for speex
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-speex
Source0:  https://github.com/savonet/ocaml-speex/releases/download/%{version}/ocaml-speex-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes
BuildRequires: ocaml-ogg
BuildRequires: speex-devel
BuildRequires: libogg-devel
Requires:      speex
Requires:      libogg

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/speex/META
/usr/lib64/ocaml/speex/speex.a
/usr/lib64/ocaml/speex/speex.cma
/usr/lib64/ocaml/speex/speex.cmi
/usr/lib64/ocaml/speex/speex.cmxa
/usr/lib64/ocaml/speex/speex.mli
/usr/lib64/ocaml/speex/ocaml-speex.h
/usr/lib64/ocaml/speex/speex_demuxer.cmi
/usr/lib64/ocaml/speex/speex_demuxer.mli
/usr/lib64/ocaml/speex/libspeex_stubs.a
/usr/lib64/ocaml/stublibs/dllspeex_stubs.so
/usr/lib64/ocaml/stublibs/dllspeex_stubs.so.owner

%description
OCAML bindings for speex


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-speex.spec
