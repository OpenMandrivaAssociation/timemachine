Summary:	Records audio up to ten seconds ago
Name:		timemachine
Version:	0.3.4
Release:	1
License:	GPLv2+
Group:		Sound
Url:		http://plugin.org.uk/timemachine/
Source0:	https://github.com/swh/timemachine/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:	timemachine-0.3.4-use-GtkType-instead-of-guint.patch
Patch1:	timemachine-0.3.4-use-ladish-instead-of-lash.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblash) >= 1.1.1
BuildRequires:	pkgconfig(liblo) >= 0.24
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)

%description
I used to always keep a mini-disc recorder in my studio running in a mode where
when you pressed record it wrote the last 10 seconds of audio to the disk and
then caught up to real-time and kept recording. The recorder died and haven't
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


%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/openmandriva-%{name}.desktop

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build


%install
%make_install

# Install a menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/openmandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=JACK TimeMachine
Comment=Records audio from ten seconds ago
Exec=%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-OpenMandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
Encoding=UTF-8
EOF


