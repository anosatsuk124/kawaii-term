### KAWAII-TERMINAL!
export TERM=xterm-256color

FREE_MEM()
{
   python3 $HOME/kawaii-term/kawaii-term.py --mem
}

export PS1="\[\033[31m\][\D{%H:%M}, $(FREE_MEM)]*'-') \[\033[0m\]< \[\033[32m\]\w\[\033[0m\] $ "
