# Build system has issues with debugsource creation
%global _empty_manifest_terminate_build 0

Summary:   A fast, lightweight distributed source control management system
Name:      mercurial
Version:	6.1.3
Release:	1
License:   GPLv2+
Group:     Development/Other
URL: 	   http://www.selenic.com/mercurial/
Source0:   http://www.selenic.com/mercurial/release/%{name}-%{version}.tar.gz
BuildRequires: pkgconfig(python3)
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: python-docutils
Provides: hg = %{version}-%{release}

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed
projects. 


%prep
%autosetup -p1

%build
export HGPYTHON3=1
%make_build all

%install
export HGPYTHON3=1
PYTHONDONTWRITEBYTECODE= %__python setup.py install -O1 --root %{buildroot} --prefix %{_prefix}
make install-doc DESTDIR=%{buildroot} MANDIR=%{_mandir}

install contrib/hgk          %{buildroot}%{_bindir}
install contrib/hg-ssh       %{buildroot}%{_bindir}

bash_completion_dir=%{buildroot}%{_sysconfdir}/bash_completion.d
mkdir -p $bash_completion_dir
install -m 644 contrib/bash_completion $bash_completion_dir/mercurial.sh

zsh_completion_dir=%{buildroot}%{_datadir}/zsh/site-functions
mkdir -p $zsh_completion_dir
install -m 644 contrib/zsh_completion $zsh_completion_dir/_mercurial

lisp_dir=%{buildroot}%{_datadir}/emacs/site-lisp
mkdir -p $lisp_dir
install -m 644 contrib/mercurial.el $lisp_dir
install -m 644 contrib/mq.el $lisp_dir

xlisp_dir=%{buildroot}%{_datadir}/xemacs/site-packages/lisp
mkdir -p $xlisp_dir
install -m 644 contrib/mercurial.el $xlisp_dir
install -m 644 contrib/mq.el $xlisp_dir

%files
%doc CONTRIBUTORS COPYING doc/README doc/hg*.txt doc/hg*.html *.cgi contrib/*.fcgi
%doc %attr(644,root,root) contrib/*.svg
%{_mandir}/man*/*
%{_sysconfdir}/bash_completion.d/mercurial.sh
%{_datadir}/zsh/site-functions/_mercurial
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/xemacs/site-packages/lisp/*.el
%{_bindir}/hg
%{_bindir}/hgk
%{_bindir}/hg-ssh
%{_libdir}/python*/site-packages/hgdemandimport
%{_libdir}/python*/site-packages/hgext
%{_libdir}/python*/site-packages/hgext3rd
%{_libdir}/python*/site-packages/mercurial
%{_libdir}/python*/site-packages/mercurial*.egg-info
