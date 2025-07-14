Summary:	GLAsteroids - 3D clone of the arcade classic
Summary(pl.UTF-8):	GLAsteroids - klon 3D klasycznej gry
Name:		glast
Version:	0.91
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://projectz.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	4396d28150067a527b6cf6abcc8df21e
Patch0:		%{name}-libgl.patch
URL:		http://projectz.ath.cx/?id=90
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
Requires:	OpenGL
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_scoredir	/var/games/glast

%description
GLAsteroids is a 3D clone of the arcade classic 'Asteroids' coded in C
using OpenGL and SDL. It features sounds effects, a menu system, a
high score table, and fuel drops. You can 'fly' around in outer space
blowing up chunks of spinning space rock with a high power dual plasma
cannon until you get smashed to pieces, run out of fuel, or save the
earth from being pulverized.

%description -l pl.UTF-8
GLAsteroids to trójwymiarowy klon klasycznej gry "Asteroids" napisany
w C przy użyciu OpenGL i SDL. Ma efekty dźwiękowe, systemowe menu,
tablicę rekordów i zrzuty paliwa. Gracz może latać w przestrzeni
kosmicznej rozbijając fragmenty obracających się ciał kosmicznych przy
pomocy dużej mocy karabinu plazmowego, dopóki nie zostanie
roztrzaskany na kawałki, nie skończy się paliwo, lub nie ocali Ziemi
od zniszczenia.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{sounds,textures},%{_scoredir}}

cp %{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
cp sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp textures/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/textures
cp textures/*.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/textures

touch $RPM_BUILD_ROOT%{_scoredir}/.highscore

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
%dir %{_scoredir}
%attr(666,root,root) %{_scoredir}/.highscore
%dir %{_datadir}/%{name}/sounds
%{_datadir}/%{name}/sounds/*.wav
%dir %{_datadir}/%{name}/textures
%{_datadir}/%{name}/textures/*
