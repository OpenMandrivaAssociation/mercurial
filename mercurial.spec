Summary:   A fast, lightweight distributed source control management system
Name:      mercurial
Version:   1.5.4
Release:   %mkrel 1
License:   GPLv2+
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
projects. Major features include:

* Extremely high-performance delta-compressed storage scheme
* Optimized for disk layout and access efficiency
* Complete cross-indexing of files and changesets
* Bandwidth and CPU efficient HTTP and SSH sync protocols 
* Distributed development model supports unlimited numbers of developers
* Allows arbitrary merging between developer branches
* Doesn't significantly degrade with large numbers of files or changesets
* No waiting for locks! 
* SHA1 integrity checking on repository data
* Append-only storage model with transaction journalling
* Fast full-repository verification
* Convenient backup 
* Most commands are familiar to users of CVS and other systems
* Built-in command help
* Integrated stand-alone web interface (example)
* Works with various GUI tools 
* Runs on UNIX, MacOS X, and Windows
* Conversion tools available for many popular SCMs
* Allows a variety of usage models
* Supports user-defined hooks and extensions 
* Source code available under the GPL license
* Actively community supported and developed

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
%{_datadir}/emacs/site-lisp/mercurial.el
%{_datadir}/xemacs/site-packages/lisp/mercurial.el
%{_bindir}/hgk
%{_bindir}/hg-ssh
%{_bindir}/hg-viz
%{_bindir}/git-rev-tree
%{_bindir}/mercurial-convert-repo

