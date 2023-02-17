2023-02-16 RTK

Notes from 2021-01-24

what, and the "favorites" icon just shows little pix of each window, which
can be guessed at one at a time!), created script to raise all terminal
windows. Then, create an "app" and icon and attach this to favorites so it's
easy to click / use.

Following in part this:

    https://averagelinuxuser.com/ubuntu_custom_launcher_dock

The script is in scripts dir, and icon below that (just need path)
(The script uses 'wmctrl -l' to find terminals, then "raise" them)

    raise_term.sh
    $sdir/icons/raise.png

To get this callable via icon, and visible when you "search" "activities" to
find programs, etc, need a ".desktop" file in /usr/share/applications. The
file should be executable. Also, paths need to be full ($sdir doesn't work).
Short file, so here's the whole thing:


    cat /usr/share/applications/raise_term.desktop
    #!/usr/bin/env xdg-open
    [Desktop Entry]
    Version=1.0
    Type=Application
    Terminal=false
    #Exec=${sdir}/raise_term.sh
    Exec=/home/ryan/scripts/raise_term.sh
    Name=raise_term
    Comment=Script to raise all term windows
    #Icon=${sdir}/icons/raise.png


------------------------
Set terminal title name
2021-01-28 RTK

Changing the name of a terminal is useful to hide some terminal windows from
my 'raise_term.sh' script (above); If the window isn't named "Terminal" then
it's not raised.

Story for this:

    https://unix.stackexchange.com/questions/177572/how-to-rename-terminal-tab-title-in-gnome-terminal

Defining this function (e.g. in .bash startup) then lets you change the name
inside the terminal.

    function set-title() {
        if [[ -z "$ORIG" ]]; then
            ORIG=$PS1
        fi
        TITLE="\[\e]2;$*\a\]"
        PS1=${ORIG}${TITLE}
    }

To use:

    set-title New-Sham-Title


