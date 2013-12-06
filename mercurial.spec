Summary:	A fast, lightweight distributed source control management system
Name:		mercurial
Version:	2.7.2
Release:	3
License:	GPLv2+
Group:		Development/Other
Url:		http://www.selenic.com/mercurial/
Source0:	http://www.selenic.com/mercurial/release/%{name}-%{version}.tar.gz
BuildRequires:	asciidoc
BuildRequires:	python-docutils
BuildRequires:	xmlto
BuildRequires:	pkgconfig(python)
Provides:	hg = %{version}-%{release}

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed
projects. 

%prep
%setup -q

%build
%make all

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install -O1 \
	--root %{buildroot} \
	--prefix %{_prefix} \
	--record=%{name}.files

make install-doc \
	DESTDIR=%{buildroot} \
	MANDIR=%{_mandir}

install contrib/hgk          %{buildroot}%{_bindir}
install contrib/convert-repo %{buildroot}%{_bindir}/mercurial-convert-repo
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

mkdir -p %{buildroot}/%{_sysconfdir}/mercurial/hgrc.d
install -m 644 contrib/mergetools.hgrc %{buildroot}/%{_sysconfdir}/mercurial/hgrc.d/mergetools.rc

%files -f %{name}.files
%doc CONTRIBUTORS COPYING doc/README doc/hg*.txt doc/hg*.html *.cgi contrib/*.fcgi
%doc %attr(644,root,root) contrib/*.svg contrib/sample.hgrc
%dir %{_sysconfdir}/mercurial
%dir %{_sysconfdir}/mercurial/hgrc.d
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/mergetools.rc
%{_mandir}/man*/*
%{_sysconfdir}/bash_completion.d/mercurial.sh
%{_datadir}/zsh/site-functions/_mercurial
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/xemacs/site-packages/lisp/*.el
%{_bindir}/hgk
%{_bindir}/hg-ssh
%{_bindir}/mercurial-convert-repo

