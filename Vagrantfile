# This Vagrantfile can be used to develop Vagrant. Note that VirtualBox
# doesn't run in VirtualBox so you can't actually _run_ Vagrant within
# the VM created by this Vagrantfile, but you can use it to develop the
# Ruby, run unit tests, etc.

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.04"
  config.vm.hostname = "vagrant"
  # config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  ["virtualbox"].each do |provider|
    config.vm.provider provider do |v, override|
      v.memory = "2048"
    end
  end

  # We split apart `install_rvm` from `setup_tests` because rvm says to
  # logout and log back in just after installing RVM.
  # https://github.com/rvm/ubuntu_rvm#3-reboot
  # config.vm.provision "shell", path: "scripts/install_rvm"

  # config.vm.provision "shell", path: "scripts/setup_tests"

  config.vm.provision "shell", path: "scripts/dependencies.sh"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 30080, host: 30080

  # config.push.define "www", strategy: "local-exec" do |push|
  #   push.script = "scripts/website_push_www.sh"
  # end

  # config.push.define "docs", strategy: "local-exec" do |push|
  #   push.script = "scripts/website_push_docs.sh"
  # end
end

