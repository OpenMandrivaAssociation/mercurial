Summary: Scalable distributed SCM
Name: mercurial
Version: 0.9.3
Release: %mkrel 1
Source0: http://www.selenic.com/mercurial/release/%{name}-%{version}.tar.bz2
URL: http://www.selenic.com/mercurial/
License: GPL
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: python-devel
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: rcs

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed
projects. Features include:

    * O(1) delta-compressed file storage and retrieval scheme
    * Complete cross-indexing of file and changesets for efficient exploration
    of project history
    * Robust SHA1-based integrity checking and append-only storage model
    * Decentralized development model with arbitrary merging between trees
    * High-speed HTTP-based network merge protocol
    * Easy-to-use command-line interface
    * Integrated stand-alone web interface
    * Small Python codebase

%prep
%setup -q

%build
python setup.py build

# build doc
(
cd doc
%make
)

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%_mandir/man1
install -m644 doc/*.1 $RPM_BUILD_ROOT%_mandir/man1/

mkdir -p $RPM_BUILD_ROOT%_mandir/man5
install -m644 doc/*.5 $RPM_BUILD_ROOT%_mandir/man5/

%check
# to avoid problems with nfs
export TMPDIR=/tmp
cd tests
./run-tests.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING CONTRIBUTORS README
%{py_platsitedir}/*
%_bindir/hg*
%_mandir/man*/*



