set -g fish_greeting

alias sdecman="sudo decman"
alias ce="cd ~/dots && nvim"

function direnv_init_pixi
    echo -e 'watch_file pixi.lock\neval "$(pixi shell-hook)"' > .envrc
    direnv allow
end

if status is-interactive
	set -x EDITOR nvim

    direnv hook fish | source
    starship init fish | source
end
