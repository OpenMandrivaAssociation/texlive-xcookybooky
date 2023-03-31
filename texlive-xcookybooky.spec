Name:		texlive-xcookybooky
Version:	36435
Release:	2
Summary:	Typeset (potentially long) recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcookybooky
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcookybooky.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/xcookybooky
%doc %{_texmfdistdir}/doc/latex/xcookybooky
#- source
%doc %{_texmfdistdir}/source/latex/xcookybooky

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
