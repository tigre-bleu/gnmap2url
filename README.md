# gnmap2url
Simple tool to create an url list from gnmap results

## Usage

```
usage: gnmap2url.py [-h] [-p PROTOCOL] file

Generates a list of URL from a gnmap output from NMAP. Example: gnmap2url.py --protocol http,https file.gnmap

positional arguments:
  file                  NMAP .gnmap input file

optional arguments:
  -h, --help            show this help message and exit
  -p PROTOCOL, --protocol PROTOCOL
                        Protocols to include in the results. Default is "--protocol http --protocol https"
```
