# revision 29373
# category Package
# catalog-ctan /macros/latex/contrib/xcookybooky
# catalog-date 2013-03-13 15:44:34 +0100
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-xcookybooky
Version:	1.2
Release:	1
Summary:	Typeset (potentially long) recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcookybooky
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to typeset recipes, which could be
greater than one page. Above the recipe text two (optional)
pictures can be displayed. Other features are recipe name,
energy content, portions, preparation and baking time, baking
temperatures, recipe source and of course preparation steps and
required ingredients. At the bottom you may insert an optional
hint. The package depends on the Emerald fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xcookybooky/xcookybooky.cfg
%{_texmfdistdir}/tex/latex/xcookybooky/xcookybooky.sty
%doc %{_texmfdistdir}/doc/latex/xcookybooky/README
%doc %{_texmfdistdir}/doc/latex/xcookybooky/example/example.pdf
%doc %{_texmfdistdir}/doc/latex/xcookybooky/example/example.tex
%doc %{_texmfdistdir}/doc/latex/xcookybooky/example/pic/background.pdf
%doc %{_texmfdistdir}/doc/latex/xcookybooky/example/pic/glass.jpg
%doc %{_texmfdistdir}/doc/latex/xcookybooky/example/pic/ingredients.jpg
%doc %{_texmfdistdir}/doc/latex/xcookybooky/xcookybooky.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xcookybooky/xcookybooky.dtx
%doc %{_texmfdistdir}/source/latex/xcookybooky/xcookybooky.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
