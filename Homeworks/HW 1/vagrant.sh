#!/bin/bash

# Initialize Vagrant configuration
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096
    vb.cpus = 4
  end
  
  config.vm.synced_folder "qemu", "/", type: "virtualbox"
  
  config.vm.provision "shell", path: "vagrant_setup.sh"
end
