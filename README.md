# arubacloud-createserver
Easy way to create multiple smart servers on ArubaCloud

# Usage
Clone repository and install requirements
```
git clone https://github.com/Valian/arubacloud-createserver
cd arubacloud-createserver
# optionally create and activate virtualenv here: 
# mkvirtualenv
pip install -r requirements.txt
```
and then use entrypoint script
```
Usage: entrypoint.py [OPTIONS] COMMAND [ARGS]...

Options:
  -u, --username TEXT             [required]
  -p, --password TEXT             [required]
  -v, --debug                     Show all performed operations
  -d, --datacenter [1|2|3|4|5|6]  DC1: Italy
                                  DC2: Italy
                                  DC3: Chech Republic
                                  DC4: France
                                  DC5: Germany
                                  DC6: UK  [required]
  --help                          Show this message and exit.

Commands:
  create_server
  show_templates
```

## Show templates command
Get and print list of all available smart server templates on ArubaCloud. Use --name option to search
```
Usage: entrypoint.py show_templates [OPTIONS]

Options:
  -n, --name TEXT  Show only templates with provided string in description
  --help           Show this message and exit.
```
Example:
```
$ python entrypoint.py -u username -p password -d 5 show_templates --name Ubuntu
Logging to ArubaCloud DC5
Getting list of hypervisors...
[Template Name: Ubuntu Server 11.04 32bit, Hypervisor: SMART, Id: 347, Enabled: False,
 Template Name: Ubuntu Server 11.04 64bit, Hypervisor: SMART, Id: 348, Enabled: False,
 Template Name: Ubuntu Server 10.04 LTS 32bit, Hypervisor: SMART, Id: 352, Enabled: False,
 Template Name: Ubuntu Server 10.04 LTS 64bit, Hypervisor: SMART, Id: 353, Enabled: False,
 Template Name: Ubuntu Virtual Desktop 32bit, Hypervisor: SMART, Id: 355, Enabled: True,
 Template Name: Ubuntu Virtual Desktop 64bit, Hypervisor: SMART, Id: 356, Enabled: True,
 Template Name: Ubuntu Server 12.04 LTS 32bit, Hypervisor: SMART, Id: 383, Enabled: False,
 Template Name: Ubuntu Server 12.04 LTS 64bit, Hypervisor: SMART, Id: 384, Enabled: False,
 Template Name: Ubuntu Server 14.04 LTS 64bit, Hypervisor: SMART, Id: 419, Enabled: True,
 Template Name: Ubuntu Server 16.04 LTS 64bit, Hypervisor: SMART, Id: 482, Enabled: True]
```

## Create server command
Command to create one or more SmartServers. Available options: 
```
Usage: entrypoint.py create_server [OPTIONS] NAMES...

Options:
  --admin-password TEXT           Admin password for root user to connect by
                                  ssh  [required]
  -t, --template-id INTEGER       Server template ID. Run "show_templates" to
                                  see all options  [required]
  -s, --size [small|medium|large|extralarge]
                                  [required]
  --help                          Show this message and exit.
```
Example 
```
$ python entrypoint.py -u username -p pass -d 5 create_server -t 482 -s small --admin-password password server1 server2
Logging to ArubaCloud DC5
Creating SmartVm server1...
Server successfully created

Creating SmartVm server1...
Server successfully created
```

## Docker
```
$ docker build -t arubacloud-createserver .
$ docker run --rm -it arubacloud-createserver --help
```

# LICENSE
MIT 
