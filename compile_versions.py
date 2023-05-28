import re, subprocess

def get_run(command):
        return subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True).stdout
def run(command):
        subprocess.run(command, shell=True)

run((
        'sudo apt update \n'
        'sudo apt install -y wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev'
))

major_versions = ['3.10', '3.11']
for major_version in major_versions:
        minor_version_numbers = []
        lines = get_run('curl -L https://www.python.org/ftp/python').split('\n')
        for line in lines:
                if line.startswith(f'<a href="{major_version}.'):
                        minor_version_numbers.append(int(re.search('<a href="(.*)/">', line).group(1).replace(f'{major_version}.', '')))
        version = f'{major_version}.{max(minor_version_numbers)}'

        run((
                f'wget https://www.python.org/ftp/python/{version}/Python-{version}.tgz \n'
                f'tar xzf Python-{version}.tgz \n'
                f'cd Python-{version} \n'
                f'./configure --enable-optimizations \n'
                'make \n'
                'cd .. \n'
                'ls -l'
        ))
