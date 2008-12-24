Summary:   A fast, lightweight distributed source control management system 
Name:      mercurial
Version:   1.1
Release:   %mkrel 2
License:   GPLv2
Group:     Development/Other
URL: 	   http://www.selenic.com/mercurial/
Source0:   http://www.selenic.com/mercurial/release/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
BuildRequires: xmlto
BuildRequires: asciidoc
Provides: hg = %{version}-%{release}

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
make all

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install -O1 --root $RPM_BUILD_ROOT --prefix %{_prefix} --record=%{name}.files
make install-doc DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}

install contrib/hgk          $RPM_BUILD_ROOT%{_bindir}
install contrib/convert-repo $RPM_BUILD_ROOT%{_bindir}/mercurial-convert-repo
install contrib/hg-ssh       $RPM_BUILD_ROOT%{_bindir}
install contrib/git-viz/{hg-viz,git-rev-tree} $RPM_BUILD_ROOT%{_bindir}

bash_completion_dir=$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mkdir -p $bash_completion_dir
install -m 644 contrib/bash_completion $bash_completion_dir/mercurial.sh

zsh_completion_dir=$RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
mkdir -p $zsh_completion_dir
install -m 644 contrib/zsh_completion $zsh_completion_dir/_mercurial

lisp_dir=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
mkdir -p $lisp_dir
install -m 644 contrib/mercurial.el $lisp_dir
xlisp_dir=$RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp
mkdir -p $xlisp_dir
install -m 644 contrib/mercurial.el $xlisp_dir
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mercurial/hgrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc CONTRIBUTORS COPYING doc/README doc/hg*.txt doc/hg*.html doc/ja *.cgi
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%_mandir/man*/*
%{_sysconfdir}/bash_completion.d/mercurial.sh
%{_datadir}/zsh/site-functions/_mercurial
%{_datadir}/emacs/site-lisp/mercurial.el
%{_datadir}/xemacs/site-packages/lisp/mercurial.el
%{_bindir}/hgk
%{_bindir}/hg-ssh
%{_bindir}/hg-viz
%{_bindir}/git-rev-tree
%{_bindir}/mercurial-convert-repo
