#!/usr/bin/env bash
# 2021-01-23 RTK
#
# Raises all terminal windows (verdascend Ubuntu 20)
#

APP_STR="Terminal"

# Get current desktop 
cur_desk=$(wmctrl -d | grep "* DG" | awk '{print $1}')

# Get terminal window ids; Current desktop last (so don't switch to that desk)
# wmctrl -l lists window info; Number ID col 1, desktop col 2, name later
n_wins=$(wmctrl -l | grep $APP_STR | awk -v cd="$cur_desk" '$2 != cd' | awk '{print $1}')
c_wins=$(wmctrl -l | grep $APP_STR | awk -v cd="$cur_desk" '$2 == cd' | awk '{print $1}')

#echo "Cur desk $cur_desk"

for wid in ${n_wins}; do
    #echo "Non-cur $wid"
    wmctrl -i -a "${wid}"
done

for wid in ${c_wins}; do
    #echo "Current $wid"
    wmctrl -i -a "${wid}"
done

