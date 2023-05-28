import re, subprocess

major_versions = ['3.10', '3.11']
for major_version in major_versions:
        minor_version_numbers = []
        lines = subprocess.run('curl -L https://www.python.org/ftp/python', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True).stdout.split('\n')
        for line in lines:
                if line.startswith(f'<a href="{major_version}.'):
                        minor_version_numbers.append(int(re.search('<a href="(.*)/">', line).group(1).replace(f'{major_version}.', '')))
        version = f'{major_version}.{max(minor_version_numbers)}'

        subprocess.run((
                f'wget https://www.python.org/ftp/python/{version}/Python-{version}.tgz \n'
                f'tar xzf Python-{version}.tgz \n'
                f'cd Python-{version} \n'
                f'./configure --enable-optimizations \n'
                'make \n'
                'cd .. \n'
                'ls -l'
        ), shell=True)
