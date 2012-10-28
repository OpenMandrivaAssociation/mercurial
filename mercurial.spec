%define		rel	1

Summary:	A fast, lightweight distributed source control management system
Name:		mercurial
Version:	2.3.2
%if %mdkversion < 201100
Release:	%mkrel %rel
%else
Release:	%rel
%endif
License:	GPLv2+
Group:		Development/Other
URL:		http://www.selenic.com/mercurial/
Source0:	http://www.selenic.com/mercurial/release/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: python-docutils
Provides: hg = %{version}-%{release}

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed
projects. 

%prep
%setup -q

%build
%make all

%install
%__rm -rf $RPM_BUILD_ROOT
PYTHONDONTWRITEBYTECODE= %__python setup.py install -O1 --root $RPM_BUILD_ROOT --prefix %{_prefix} --record=%{name}.files
make install-doc DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}

install contrib/hgk          $RPM_BUILD_ROOT%{_bindir}
install contrib/convert-repo $RPM_BUILD_ROOT%{_bindir}/mercurial-convert-repo
install contrib/hg-ssh       $RPM_BUILD_ROOT%{_bindir}

bash_completion_dir=$RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mkdir -p $bash_completion_dir
install -m 644 contrib/bash_completion $bash_completion_dir/mercurial.sh

zsh_completion_dir=$RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
mkdir -p $zsh_completion_dir
install -m 644 contrib/zsh_completion $zsh_completion_dir/_mercurial

lisp_dir=$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
mkdir -p $lisp_dir
install -m 644 contrib/mercurial.el $lisp_dir
install -m 644 contrib/mq.el $lisp_dir

xlisp_dir=$RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp
mkdir -p $xlisp_dir
install -m 644 contrib/mercurial.el $xlisp_dir
install -m 644 contrib/mq.el $xlisp_dir

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mercurial/hgrc.d
install -m 644 contrib/mergetools.hgrc $RPM_BUILD_ROOT/%{_sysconfdir}/mercurial/hgrc.d/mergetools.rc

%clean
%__rm -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
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

