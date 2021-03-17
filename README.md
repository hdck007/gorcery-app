# This is the repository for the grocery-app project

### How to setup the repository on the local pc?
1. First fork this repository and click on the watch button too to be aware about the updates
2. Once you have forked the repository clone the forked repository using `git clone <remote repo url of the forked repo>` command
3. Now you will have a directory on your pc named `grocery-app` get into the directory using `cd grocery-app` make sure that this directory also contains **manage.py** and **requirements.txt** files
4. Once the above steps are done run the command `pip install -r requirements.txt` and wait for some time till it installs all the dependencies
5. Now create and switch to the branch according to the feature you are working. **eg: if you are working on adding filter use `git checkout -b filters`**
6.  Thats it!!!

### How do I run the project for the first time?
##### So I assume that you have done the setup and you want to run the app, get into the `grocery-app` directory and run the following commands as mentioned:
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver`
4. Done now you may open your browser on the mentioned url that you will get to see in the console.

### How do I develop things from now on?
1. Add the code that you want to contribute and always test whether everything is working or not by running `python manage.py runserver`
2. Once you are done editing the code do `git status` to check status
3. Add the files to staging using `git add <filename>`
4. Commit your changes using `git commit -m "<your commit message>"`
5. Push your changes to the remote repo using `git pusb -u origin <branch-name>`
6. Create a pull request and wait for further instruction.

> If you feel stuck feel free to contact me
> and once watch a tutorial about django and git so that you become a bit familiar
> Also click on the watch and star button just to be aware of the happennings.

# Do checkout the gist of what is needed to be done here [Gist](https://github.com/hdck007/gorcery-app/blob/master/gist.md)
