## Welcome to Management & Processing of Large-scale Data

### Viewing the Lectures Online

If you simply want to view the lecture materials online (note: you won't be able to interact with the code examples), you can do so using the Jupyter nbviewer site:

[https://nbviewer.jupyter.org/mooneymi/large_scale_data](https://nbviewer.org/github/mooneymi/large_scale_data/tree/master/)

To view any lecture, follow the link above then click on any of the .ipynb (Jupyter notebooks) or .md (Markdown) files listed. When viewing notebooks on the nbviewer site, there will be a download icon in the upper right corner if you want to download and run the notebook on your local machine.


### Cloning the Repo

The simplest way to get all the class materials is to click the "Code" button above and then "Download ZIP". However, this won't create a Git repository on your local machine (you'll simply be copying the files). Following the steps below to clone the repo on your local computer will give you some familiarity with Github and the Git version control system, which will definitely come in handy in the future.

#### Git on the Command-line

I encourage you to try using Git on the command-line. Mac and Linux users should already have git installed on their computers. You can check with the following command:

`git --version`

If you don't have Git installed, you can get it at the link below (available for all operating systems):

[https://git-scm.com/downloads](https://git-scm.com/downloads)

[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Once you have Git installed, from the command-line you can simply change to the directory where you want to clone this repo and then run the following:

`git clone https://github.com/mooneymi/large_scale_data.git`


#### Github Desktop

If you're not comfortable using the command-line, there is a Github Desktop app available at the link below:

[https://desktop.github.com/](https://desktop.github.com/)

To clone this repository, follow the instructions here (note: keep this page open, because you'll need to click the "Clone or download" button above):

[https://help.github.com/desktop/guides/contributing/cloning-a-repository-from-github-to-github-desktop/](https://help.github.com/desktop/guides/contributing/cloning-a-repository-from-github-to-github-desktop/)


### Running the Jupyter Notebooks

*Note: Please make sure you have installed the Anaconda Python distribution ([https://www.continuum.io/downloads](https://www.continuum.io/downloads)) before trying to run the Jupyter Notebooks.*

Once you've cloned the repo to you computer, open a terminal and go to the directory containing the repo. Then type the following command to start the Jupyter Notebook server:

`jupyter notebook`

A new tab should open in your web browser that lists all the available lectures. Click on the link for "BMI535_Week_2.1_Python_Data_Solutions.ipynb". This should open the notebook in a new tab.


### Conda, Jupyter, and R

Note that one of the notebooks for the class is written in R. If you haven't used used Jupyter with R before, more info on using Conda to create an R environment can be found here (the `r-essentials` package will allow you to use R in Jupyter): [https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/](https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/)
