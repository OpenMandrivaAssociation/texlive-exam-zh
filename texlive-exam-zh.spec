%global tl_name exam-zh
%global tl_revision 79661

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.0
Release:	%{tl_revision}.1
Summary:	LaTeX template for Chinese exams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/exam-zh
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-zh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exam-zh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Although there are already several excellent exam packages or classes
like exam and bhcexam, these do not fit the Chinese style very well, or
they cannot be customized easily for Chinese exams of all types, like
exams in primary school, junior high school, senior high school and even
college. This is the main reason why this package was created. This
package provides a class exam-zh.cls and several module packages like
exam-zh-question.sty and exam-zh-choices.sty, where these module
packages can be used individually. Using exam-zh you can separate the
format and the content very well; use the choices environment to typeset
choice items easily and automatically; design the seal line easily; and
more (see manual).

