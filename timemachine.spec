%define name	timemachine
%define version	0.3.1
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Records audio up to ten seconds ago
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://plugin.org.uk/timemachine/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig
BuildRequires:	alsa-lib-devel jackit-devel libsamplerate-devel gtk2-devel libsndfile-devel lash-devel

%description
I used to always keep a minidisc recorder in my studio running in a mode where
when you pressed record it wrote the last 10 seconds of audio to the disk and
then caught up to realtime and kept recording. The recorder died and haven't
been able to replace it, so this is a simple jack app to do the same job. It
has the advantage that it never clips and can be wired to any part of the jack
graph.

The idea is that I doodle away with whatever is kicking around in my studio
and when I heard an interesting noise, I'd press record and capture it,
without having to try and recreate it. :)

I've been using it to record occasional bursts of interesting noise from jack
apps feeding back into each other. It seems to be stable for me, but there
could be threading issues and race condidtions if run without SCHED_FIFO (ie.
without jackd -R).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall}

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=JACK TimeMachine
Comment=Records audio from ten seconds ago
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
Encoding=UTF-8
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

