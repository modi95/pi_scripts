#Ruby install log

#Install XCode dev tools
xcode-select --install

#Installing brew package manager
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install wget

brew install rbenv ruby-build

# Add rbenv to bash so that it loads every time you open a terminal
echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile
source ~/.bash_profile

# Install Ruby
rbenv install 2.2.1
rbenv global 2.2.1
ruby -v

#Installing Rails
sudo gem install nokogiri
sudo gem install rails
rbenv rehash
rails -v

#Should already have SQLite3 through XCode command line toosl
#Add code for DB of choice here.
