#
# TODO: move score file(s) to /var/games
#
Summary: 	GLAsteroids - 3D clone of the arcade classic
Summary(pl):	GLAsteroids - klon 3D klasycznej gry
Name:		glast
Version:	0.9
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://projectz.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	e55eddc69ff5925ea710c2208a1e57bc
Patch0:		%{name}-libgl.patch
URL:		http://projectz.ath.cx/?id=90
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
Requires:	OpenGL
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GLAsteroids is a 3D clone of the arcade classic 'Asteroids' coded in C
using OpenGL and SDL. It features sounds effects, a menu system, a
high score table, and fuel drops. You can 'fly' around in outer space
blowing up chunks of spinning space rock with a high power dual plasma
cannon until you get smashed to pieces, run out of fuel, or save the
earth from being pulverized.
 
%description -l pl
GLAsteroids to trójwymiarowy klon klasycznej gry "Asteroids" napisany
w C przy u¿yciu OpenGL i SDL. Ma efekty d¼wiêkowe, systemowe menu,
tablicê rekordów i zrzuty paliwa. Gracz mo¿e lataæ w przestrzeni
kosmicznej rozbijaj±c fragmenty obracaj±cych siê cia³ kosmicznych przy
pomocy du¿ej mocy karabinu plazmowego, dopóki nie zostanie
roztrzaskany na kawa³ki, nie skoñczy siê paliwo, lub nie ocali Ziemi
od zniszczenia.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{sounds,textures}}

cp %{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
cp sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp textures/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/textures
cp textures/*.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/textures

touch $RPM_BUILD_ROOT%{_datadir}/%{name}/.highscore

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
./%{name} \$@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
# MOVE TO /var/games!!!
%attr(666,root,root) %{_datadir}/%{name}/.highscore
%dir %{_datadir}/%{name}/sounds
%{_datadir}/%{name}/sounds/*.wav
%dir %{_datadir}/%{name}/textures
%{_datadir}/%{name}/textures/*
