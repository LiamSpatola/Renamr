<img src="https://raw.githubusercontent.com/LiamSpatola/Images/main/Renamr.png">

# Renamr #

A lightweight piece of software for renaming files in bulk from the command line.

## Installation ##
Install the software via the `Renamr-v2.0.2-Installer.msi` installer.

## Command Usage ##
The command should be used as follows:

```bash
Renamr [OPTIONS] DIRECTORY NEWNAME DELIMETER
```

The `DIRECTORY` is the folder which contains the files you wish to rename.

The `NEWNAME` is the name to remain the files to.

The `DELIMETER` is the seperator between the new name and number. For instance, if your new name is `Europe_Trip`, the file name would become for instance `Europe_Trip_1.txt`. The delimeter is the underscore in the above example.

## Further Options ##

Further options you can use are:

- `--skip-confirmation`: This option forgoes the usual confirmation to confirm the renaming operation.
- `--verbose`: This option prints each file, and it's new name to the standard output.
- `--help`: This option brings up the help page.

## Warnings ##

- ALL files inside the target folder WILL be renamed, and this cannot be undone. Please be careful to specify the correct target directory.

- Please do not use a delimeter which is used elswhere for something else in windows. For example, do not use a `.` as a delimeter, a file extension, or a special character like `§`. This may cause windows to do something unexpected, or even corrupt the file. `_` and `-` are great delimeters to use instead.
## Licensing ##

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/LiamSpatola/Renamr">Renamr</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/LiamSpatola">LiamSpatola</a> is licensed under <a href="http://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

## Closing Notes ##

Thank you for using Renamr! If you have suggestions or want to report a bug, please raise an issue on the github page:

https://github.com/LiamSpatola/Renamr/issues
