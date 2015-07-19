Name:           xmvn2-bootstrap
Version:        1
Release:        2
Summary:        Parent pom file for Apache projects

License:        ASL 2.0
BuildArch:      noarch

Requires:       apache-parent
Requires:	maven-parent
Requires:	maven-scm

Provides:	mvn(org.apache.maven.scm:maven-scm-providers-standard)
Provides:	mvn(org.apache:apache)
Provides:	mvn(org.apache.maven:maven-parent)

%description
This package allows us to transition to xmvn2 deps

%files
