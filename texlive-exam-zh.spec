Name:		texlive-exam-zh
Version:	67505
Release:	1
Summary:	LaTeX template for Chinese exams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exam-zh
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-zh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-zh.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Although there are already several excellent exam packages or
classes like exam and bhcexam, these do not fit the Chinese
style very well, or they cannot be customized easily for
Chinese exams of all types, like exams in primary school,
junior high school, senior high school and even college. This
is the main reason why this package was created. This package
provides a class exam-zh.cls and several module packages like
exam-zh-question.sty and exam-zh-choices.sty, where these
module packages can be used individually. Using exam-zh you can
separate the format and the content very well; use the choices
environment to typeset choice items easily and automatically;
design the seal line easily; and more (see manual).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/exam-zh
%doc %{_texmfdistdir}/doc/xelatex/exam-zh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
