import typer
import os


app = typer.Typer()


@app.command()
def bulk_rename(directory, newname):
    files = os.listdir(directory)

    counter = 0

    for file in files:
        filetype = file.split(".")[-1]

        os.rename(directory + "/" + file, directory + "/" + newname + str(counter) + "." + filetype)
        renamed_file = newname + str(counter) + "." + filetype
        print(f"Renamed {file} to {renamed_file}")

        counter += 1


if __name__ == "__main__":
    app()
