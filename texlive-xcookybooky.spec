%global tl_name xcookybooky
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Typeset (potentially long) recipes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xcookybooky
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to typeset recipes, which could be greater
than one page. Above the recipe text two (optional) pictures can be
displayed. Other features are recipe name, energy content, portions,
preparation and baking time, baking temperatures, recipe source and of
course preparation steps and required ingredients. At the bottom you may
insert an optional hint. The package depends on the Emerald fonts.

