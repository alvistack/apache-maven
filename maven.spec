# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global __strip /bin/true

%global __brp_mangle_shebangs /bin/true

Name: maven
Epoch: 100
Version: 3.9.5
Release: 1%{?dist}
BuildArch: noarch
Summary: Java project management and project comprehension tool
License: Apache-2.0
URL: https://github.com/apache/maven/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: rsync
Requires: java

%description
Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a
project's build, reporting and documentation from a central piece of
information.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -d %{buildroot}%{_datadir}/bash-completion/completions
install -Dpm755 -d %{buildroot}%{_datadir}/maven
install -Dpm755 -t %{buildroot}%{_datadir}/bash-completion/completions usr/share/bash-completion/completions/mvn
rsync -av usr/share/maven/ %{buildroot}%{_datadir}/maven
ln -fs /usr/share/maven/bin/mvn %{buildroot}%{_bindir}/mvn
ln -fs /usr/share/maven/bin/mvnDebug %{buildroot}%{_bindir}/mvnDebug

%check

%files
%license LICENSE
%{_bindir}/*
%{_datadir}/bash-completion/completions/mvn
%{_datadir}/maven

%changelog
