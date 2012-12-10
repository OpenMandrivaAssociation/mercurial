%define		rel	1

Summary:	A fast, lightweight distributed source control management system
Name:		mercurial
Version:	2.2.2
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



%changelog
* Tue Jun 12 2012 Lev Givon <lev@mandriva.org> 2.2.2-1
+ Revision: 805290
- Update to 2.2.2.

* Tue May 15 2012 Lev Givon <lev@mandriva.org> 2.2.1-1
+ Revision: 799028
- Update to 2.2.1.

* Wed Apr 11 2012 Lev Givon <lev@mandriva.org> 2.1.2-1
+ Revision: 790337
- Update to 2.1.2.

* Mon Mar 05 2012 Lev Givon <lev@mandriva.org> 2.1.1-1
+ Revision: 782197
- Update to 2.1.1.

* Sun Feb 05 2012 Lev Givon <lev@mandriva.org> 2.1-1
+ Revision: 771286
- Update to 2.1.

* Mon Jan 02 2012 Lev Givon <lev@mandriva.org> 2.0.2-1
+ Revision: 748675
- Update to 2.0.2.

* Fri Dec 02 2011 Lev Givon <lev@mandriva.org> 2.0.1-1
+ Revision: 737255
- Update to 2.0.1.

* Wed Nov 02 2011 Lev Givon <lev@mandriva.org> 2.0-1
+ Revision: 712245
- Update to 2.0.

* Mon Oct 03 2011 Lev Givon <lev@mandriva.org> 1.9.3-1
+ Revision: 702637
- Update to 1.9.3.

* Wed Sep 21 2011 Lev Givon <lev@mandriva.org> 1.9.2-1
+ Revision: 700731
- Update to 1.9.2.

* Tue Sep 20 2011 Lev Givon <lev@mandriva.org> 1.9.1-1
+ Revision: 700638
- Update to 1.9.1.

* Thu Jun 02 2011 Lev Givon <lev@mandriva.org> 1.8.4-1
+ Revision: 682451
- Update to 1.8.4.

* Sun May 01 2011 Lev Givon <lev@mandriva.org> 1.8.3-1
+ Revision: 661296
- Update to 1.8.3.

* Thu Apr 28 2011 Lev Givon <lev@mandriva.org> 1.8.2-1
+ Revision: 660153
- Update to 1.8.2.

* Tue Mar 15 2011 Lev Givon <lev@mandriva.org> 1.8.1-1
+ Revision: 645030
- Update to 1.8.1.

* Wed Mar 02 2011 Lev Givon <lev@mandriva.org> 1.8-1
+ Revision: 641279
- Update to 1.8.

* Sun Jan 02 2011 Lev Givon <lev@mandriva.org> 1.7.3-1mdv2011.0
+ Revision: 627547
- Update to 1.7.3.

* Thu Dec 02 2010 Lev Givon <lev@mandriva.org> 1.7.2-1mdv2011.0
+ Revision: 604819
- Update to 1.7.2.

* Wed Nov 17 2010 Lev Givon <lev@mandriva.org> 1.7.1-1mdv2011.0
+ Revision: 598134
- Update to 1.7.1.

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 1.6.4-3mdv2011.0
+ Revision: 590353
- rebuild for python 2.7

* Fri Oct 08 2010 Lev Givon <lev@mandriva.org> 1.6.4-1mdv2011.0
+ Revision: 584245
- Update to 1.6.4.

* Fri Aug 27 2010 Lev Givon <lev@mandriva.org> 1.6.3-1mdv2011.0
+ Revision: 573469
- Update to 1.6.3.

* Tue Aug 03 2010 Lev Givon <lev@mandriva.org> 1.6.2-1mdv2011.0
+ Revision: 565216
- Update to 1.6.2.

* Mon Jul 19 2010 Lev Givon <lev@mandriva.org> 1.6-1mdv2011.0
+ Revision: 554965
- Update to 1.6.

* Tue Jun 01 2010 Lev Givon <lev@mandriva.org> 1.5.4-1mdv2010.1
+ Revision: 546850
- Update to 1.5.4.
- Update to 1.5.3.

* Fri Apr 02 2010 Lev Givon <lev@mandriva.org> 1.5.1-1mdv2010.1
+ Revision: 530772
- Update to 1.5.1.

* Sun Mar 07 2010 Lev Givon <lev@mandriva.org> 1.5-1mdv2010.1
+ Revision: 515466
- Update to 1.5.

* Mon Feb 01 2010 Lev Givon <lev@mandriva.org> 1.4.3-1mdv2010.1
+ Revision: 499245
- Update to 1.4.3.

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 1.4.2-1mdv2010.1
+ Revision: 484958
- update to new version 1.4.2

* Wed Dec 02 2009 Lev Givon <lev@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 472619
- Update to 1.4.1.

* Tue Nov 17 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4-1mdv2010.1
+ Revision: 467008
- update to new version 1.4

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 399117
- update to new version 1.3.1

* Fri Jul 03 2009 Lev Givon <lev@mandriva.org> 1.3-1mdv2010.0
+ Revision: 391921
- Update to 1.3.

* Sat Mar 21 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 359983
- update to new version 1.2.1

* Sun Mar 08 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2-1mdv2009.1
+ Revision: 352891
- update to new version 1.2

* Sat Jan 03 2009 Jérôme Soyer <saispo@mandriva.org> 1.1.2-1mdv2009.1
+ Revision: 323882
- New upstream release

* Thu Dec 25 2008 Michael Scherer <misc@mandriva.org> 1.1-2mdv2009.1
+ Revision: 318497
- rebuild for new python

* Sat Dec 20 2008 Olivier Thauvin <nanardon@mandriva.org> 1.1-1mdv2009.1
+ Revision: 316544
- 1.1

* Fri Aug 15 2008 Lev Givon <lev@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 272385
- Update to 1.0.2.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 268141
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 01 2008 Lev Givon <lev@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 214142
- Update to 1.0.1.

* Sun Apr 13 2008 Lev Givon <lev@mandriva.org> 1.0-1mdv2009.0
+ Revision: 192649
- Update to 1.0.

* Sat Mar 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.5-2mdv2008.1
+ Revision: 177399
- Fix group
- Sync spec file with fedora
  Add cgi files (Bug #36194)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.5-1mdv2008.1
+ Revision: 107084
- New release

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.4-1mdv2008.0
+ Revision: 53115
- New release


* Tue Dec 19 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.3-1mdv2007.0
+ Revision: 100353
- 0.9.3

* Mon Dec 18 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.2-2mdv2007.1
+ Revision: 98735
- bump release
- 0.9.2

* Wed Dec 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.9-2mdv2007.1
+ Revision: 91457
- rebuild with new python

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - import mercurial-0.9-1mdk

* Sat May 13 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.9-1mdk
- New release 0.9

* Wed Feb 01 2006 Gaetan Lehmann <glehmann@deborah.mandriva.com> 0.8-2mdk
- fix build on x86_64 (drop patch0)

* Tue Jan 31 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.8-1mdk
- New release 0.8

* Fri Oct 21 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.7-2mdk
- Fix BuildRequires

* Wed Oct 05 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.7-1mdk
- New release 0.7

* Fri Sep 09 2005 Gaetan Lehmann <glehmann@mandrakesoft.com> 0.6c-1mdk
- New release 0.6c
- generate doc with asciidoc
- make tests
- patch0: better detection of lib name to allow tests to run on 32 bits
  system with a /usr/lib64 directory (like n4 on mandriva cluster)

* Fri Jun 03 2005 Frederic Lepied <flepied@mandriva.com> 0.5b-1mdk
- initial package

