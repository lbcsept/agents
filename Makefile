

install.uv:
	curl -LsSf https://astral.sh/uv/install.sh > /tmp/install-uv.sh
	sh /tmp/install-uv.sh
	rm /tmp/install-uv.sh
	echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc


install.ollama:
	curl -fsSL https://ollama.com/install.sh | sh



replicate_host_config:
	# removing backups *_OLD
	if [ -e ~/.ssh_OLD ]; then rm -rf ~/.ssh_OLD; fi 
	if [ -e ~/.saml2aws_OLD ]; then rm -rf ~/.saml2aws_OLD; fi 
	if [ -e ~/.aws_OLD ]; then rm -rf ~/.aws_OLD; fi
	if [ -e ~/.gitconfig_OLD ]; then rm -rf ~/.gitconfig_OLD; fi
	if [ -e ~/.bash_profile_OLD ]; then rm -rf ~/.bash_profile_OLD; fi
	if [ -e ~/.bash_history_OLD ]; then rm -rf ~/.bash_history_OLD; fi
	if [ -e ~/.pypirc_OLD ]; then rm -rf ~/.pypirc_OLD; fi
	if [ -e ~/.env_OLD ]; then rm -rf ~/.env_OLD; fi

	# moving current home files to backup
	if [ -e ~/.ssh ]; then mv ~/.ssh ~/.ssh_OLD; fi
	if [ -e ~/.saml2aws ]; then mv ~/.saml2aws ~/.saml2aws_OLD; fi
	if [ -e ~/.aws ]; then mv ~/.aws ~/.aws_OLD; fi
	if [ -e ~/.gitconfig ]; then mv ~/.gitconfig ~/.gitconfig_OLD; fi
	if [ -e ~/.bash_profile ]; then mv ~/.bash_profile ~/.bash_profile_OLD; fi
	if [ -e ~/.bash_history ]; then mv  ~/.bash_history ~/.bash_history_OLD; fi
	if [ -e ~/.pypirc ]; then mv ~/.pypirc ~/.pypirc_OLD; fi
	if [ -e ~/.env ]; then mv ~/.env ~/.env_OLD; fi

	# symlink current user to host user conf files
	if [ -e $(HOST_HOME)/.ssh ]; then ln -s $(HOST_HOME)/.ssh ~/.ssh; fi
	if [ -e $(HOST_HOME)/.saml2aws ]; then ln -s $(HOST_HOME)/.saml2aws ~/.saml2aws; fi
	if [ -e $(HOST_HOME)/.aws ]; then ln -s $(HOST_HOME)/.aws ~/.aws; fi
	if [ -e $(HOST_HOME)/.gitconfig ]; then ln -s $(HOST_HOME)/.gitconfig ~/.gitconfig ; fi
	if [ -e $(HOST_HOME)/.bash_profile ]; then ln -s $(HOST_HOME)/.bash_profile ~/.bash_profile; fi
	if [ -e $(HOST_HOME)/.bash_history ]; then ln -s $(HOST_HOME)/.bash_history ~/.bash_history; fi
	if [ -e $(HOST_HOME)/.pypirc ]; then ln -s $(HOST_HOME)/.pypirc ~/.pypirc; fi
	if [ -e $(HOST_HOME)/.env ]; then ln -s $(HOST_HOME)/.env ~/.env; fi
	echo "Host configuration replicated"

