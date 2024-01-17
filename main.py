import typer
import os


app = typer.Typer()


@app.command()
def renameFiles(directory: str, newname: str, delimeter: str, skip_confirmation: bool = typer.Option(default=False, help="Skip the usual confirmation of the renaming operation."), verbose: bool = typer.Option(default=False, help="Use verbose mode")):

    counter = 0
    files = os.listdir(directory)


    if not skip_confirmation:
        confirm = typer.confirm("This operation will rename everything in the target directory. Do you wish to proceed?")
        if not confirm:
            typer.Abort()


    for file in files:
        filetype = file.split(".")[-1]

        os.rename(directory + "/" + file, directory + "/" + newname + delimeter + str(counter) + "." + filetype)
        

        if verbose:
            renamedFile = newname + delimeter + str(counter) + "." + filetype
            print(f"Renamed {file} to {renamedFile}")

        counter += 1


if __name__ == "__main__":
    app()
