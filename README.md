# SublimeText Decode YAML plugin

<p>What is the goal of Decode YAML plugin? Short answer is converting this YAML</p>
    a:3:{s:7:"enabled";b:1;s:15:"recursion_limit";i:35;s:5:"_core";a:1:{s:19:"default_config_hash";s:43:"X4YpfA5OdcR0yUAF6UsJxqmOdrviYYj45h_SAH_p4oU";}}
<p>to this: </p>
    enabled: true
    recursion_limit: 35
    _core:
      default_config_hash: X4YpfA5OdcR0yUAF6UsJxqmOdrviYYj45h_SAH_p4oU
    
<p>Want more? It can indent only selected sub array - including multiple selections. Decode YAML plugin won't mess up your keyboard shortcuts because it uses "chord" command Ctrl+D, Ctrl+Y (this mean hold Ctrl, press D then press Y, release Ctrl) and also available in "Selection" menu. </p>

## Supported Sublime Text versions
Indent plugin supports both Sublime Text 3

## Installation
 - In Sublime Text 3 - clone project from [Github](https://github.com/Lakshman-N/sublimetext_decodeyaml.git) into the user's Packages folder.
    - On Mac, "~/Library/Application Support/Sublime Text 3/Packages/"
    - On Windows, "C:\Users\\{user}\AppData\Roaming\Sublime Text 3\Packages"

## Usage ##
Click on Tools->Command Palette... (or Ctrl+shift+P if you're a keyboard guy) and then chose "Decode YAML"

## Feedback & Support
Available on [Github](https://github.com/Lakshman-N/sublimetext_decodeyaml.git)

## Contribution
...is always welcome! Same place - [Github](https://github.com/Lakshman-N/sublimetext_decodeyaml.git)

## License
This software is distributed under GPLv3 license (see License.txt for details)
