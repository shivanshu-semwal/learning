## git and ssh

- if you are using git for multiple accounts, try using ssh keys

## adding remote repo

- usually we name it `origin`
- `git remote add origin <repo-url>`
- HTTPS format: `https://github.com/username/repository.git`
- SSH format: `git@github.com:username/repository.git`

## Effect of files permission on git?

#TODO

## Multiple git accounts

Put this in `ssh` config folder - `~/.ssh/config`

```toml
# default github account shivanshu-semwal
Host github.com
  HostName github.com
  IdentityFile ~/Documents/keys/shiv_github
  IdentitiesOnly yes

# other github
Host github-bug
  HostName github.com
  IdentityFile ~/Documents/keys/github2
  IdentitiesOnly yes

# another one
Host github-totoro
  HostName github.com
  IdentityFile ~/Documents/keys/totoro
  IdentitiesOnly yes
```

- when you use git do, `git [git@github.com](mailto:git@github.com):shivanshu-semwal/notes.git`
- change the host to the one in config, `github-bug[@github.com](mailto:git@github.com):shivanshu-semwal/notes.git`
- `host@github.com:user/repo`

https://www.youtube.com/watch?v=RxHJdapz2p0