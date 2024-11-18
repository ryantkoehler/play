# 4/28/16 RTK
#   Updating for toma mac
# 8/3/16 RTK; Add -k to dirw and dirt (first col kb, not 'blocks')
# 8/11/17 RTK; Update for verdascend with ubuntu 16.06 and bash
# 11/26/17 RTK; Add classes alias
# 1/4/18 RTK; Clean up (mainly perl, anaconda in path; remove from .bashrc) 
# 12/1/18 RTK; Revisit to force on Ubuntu 18.4 (verdascend)
# 10/18/19 RTK; Update / sync machines (verdascend, tomac, splitmac)
#

# Get system for system-specific shams...
is_mac=0
if [ `hostname | grep -i verd` ]; then
    this_sys='verd'
elif [ `uname | grep -i darwin` ] && [ `hostname | grep -i ryan` ] && [ `hostname | grep Pro` ] ; then
    this_sys='tomac'
    is_mac=1
elif [ `uname | grep -i darwin` ] && [ `hostname | grep -i ryan` ] && [ `hostname | grep Air` ] ; then
    this_sys='splitmac'
    is_mac=1
else
    this_sys='generic'
fi


# Alias collection
alias vi="vim"
alias dir="ls"
alias dirw="ls -laskF"
alias dirt="ls -latrkF"
alias dirc="ls -C1"
alias dirp="ls -ald * | grep '^-..x'"
alias subdir="ls -ald * | grep '^d'"
alias subdirt="ls -latrd * | grep '^d'"
alias c="clear"
alias his="history | grep -i --color"
alias proc="ps -ef | grep -i --color"
alias igrep="grep -i --color"
alias xdo="chmod a+x"
alias undo="chmod a-x"
# Mac / not dependent
if [[ $is_mac -lt 1 ]]; then
    alias open="xdg-open"
fi

export EDITOR="vim"


#   Dir collection
export toma="$HOME/Toma"
export split="$HOME/Split"
export tdir="$HOME/tran"
export play="$HOME/play"
export Ryan="$HOME/Ryan"
export classes="$HOME/Ryan/classes"
export wdir="$HOME/VerdAscend/work"
export tex="$HOME/tex-unix"
export pix="$HOME/pix"
export data="$HOME/data"
export seqs="$HOME/data_seqs"
export cdir="$HOME/code"
export gitdir="$HOME/git"
export progs="$HOME/programs"
export tests="$HOME/prog_tests"
export srcdir="$HOME/src_libs"
export webdir="/var/www/html"
export cgidir="/usr/lib/cgi-bin"


# Executable and code library paths
export bdir="$HOME/linbin"
export sdir="$HOME/scripts"
export pbdir="$HOME/p-linbin"
# Python stuff
export pydir="$play/Python/pylib"
export PYTHONPATH="$pydir"
# Perl stuff
export perldir="$play/Perl/perlib"
export PERL5LIB="$perldir"
# mySQL
export mysql_bin="/usr/local/mysql/bin/mysql"

# bioinfo stuff
#   BLAST databases
export BLASTDB="$seqs/Blast"
#   Picard java sham 
alias picard="java -jar /Users/ryan/programs/Picard/picard.jar"
#   NCBI path
export ncbipath="$progs/NCBI/sratoolkit/bin"

#   Path
export PATH=".:$bdir:$sdir:$pbdir:$mysql_bin:$PATH"

#   For sort (not tested too much???)
export LC_ALL=C    


#
#   Prompt
#       \\u = user, \\h = host, \\w = working dir
#   Color... 
#       First \[\e[1;32m\] starts; Last \[\e resets to white
#       0:32 = normal green, 1:33 = bold yellow, 1:37 = bold white
#    30 = grey
#    31 = red
#    32 = green
#    33 = yellow
#    34 = blue
#    35 = magenta
#    36 = cyan
#    37 = white
#

if [[ $this_sys = 'verd' ]]; then
    export PS1="\[\e[1;32m\]\\u@\h \\w> \[\e[1;37m\]"
elif [[ $this_sys = 'splitmac' ]]; then
    export PS1="\[\e[1;36m\]\\u@\h \\w> \[\e[1;37m\]"
else
    export PS1="\[\e[1;33m\]\\u@\h \\w> \[\e[1;37m\]"
fi

#   Special things to make bash behave nicer
#   $OLDPWD automatically set as previous directory 
alias back='cd "$OLDPWD"'
#   This is intended to stop tab-completion from escaping $env vars
#
# 3/1/16 RTK; Doesn't fly on mac ...?
# 12/1/18 RTK; Revisit to force on Ubuntu 18.4 (verdascend)
#shopt -s direxpand

