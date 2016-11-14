name              'some-cookbook'
maintainer        'Some Org'
maintainer_email  'cookbooks@org.com'
license           'all_rights'
description       'Installs/Configures orderup'
long_description  'Installs/Configures orderup'
version           '2.0.2'
source_url        'https://github.com/nikogura/build-tools' if respond_to?(:source_url)
issues_url        'https://github.com/nikogura/build-tools/issues' if respond_to?(:issues_url)

# Platforms supported by this cookbook
%w(redhat centos oracle).each do |os|
  supports os
end

# Cookbook dependancies
depends 'chef-vault', '~> 1.3.3'
