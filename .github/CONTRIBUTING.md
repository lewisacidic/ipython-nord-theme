# Contributing

Thank you for your interest in ipython-nord-theme!
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome - head over to the [Issue Tracker](../issues) to get started!

Please note that we have a [code of conduct](#code-of-conduct); please follow it in all your interactions with the project.


## Bug reports and feature requests

The project uses the GitHub Issue Tracker](../issues) to track all bugs and feature requests; feel free to open an issue if you think you have found a bug or have an idea for a new feature.
Before you do, however, please attempt to check that the issue is not currently being addressed by another in the issue tracker.
If you are making a bug report, please read the next section.


### Bug Reports

If you are making a bug report, please describe the bug in a clear and concise manner.

All bug reports should contain a **short, reproducible code snippet**, formatted using [appropriate code blocks](https://help.github.com/en/articles/creating-and-highlighting-code-blocks).
Please **provide the full traceback** if an exception is raised.
If the snippet is longer than 50 lines, you can create a [gist](https://gist.github.com/) or set up an example repository.

Please **include a link any external data used** or if this is sensitive, produce dummy data that reproduces the bug.

Finally, include **operating system type and version**, **Python version**, **ipython-nord-theme version**, and the **installation procedure** you used.


## Contributing code

When contributing to ipython-nord-theme, please first discuss the change you wish to make via the [Issue Tracker](../issues) before writing any substantial code.
This will make sure we are on the same page, allows all features to be tracked consistently, and avoid any wasted time and/or disappointment if your contribution does not end up merged. 
*We aim to have at least one issue for every pull request.*

Once the issue is documented, you can get started with the code! 

Please follow the [below guide](#setting-up-the-environment) to set up a consistent development environment.
Make your changes, and submit a [Pull Request](../pulls) against the master branch.
Our Continuous Integration suite will then run against your code, if the tests pass, there are no formatting errors, and the maintainers are happy, we will make a new release with your contribution!


### Setting up the environment

First, **fork the code** using the `Fork` button on [the source page](..).

Then, **clone the code** with `git`, and change into the source directory (if you haven't used `git` before, a good place to start is [GitHub's help pages](https://help.github.com/en)).

```shell
git clone https://github.com/<your username>/ipython-nord-theme
cd ipython-nord-theme
```

Next, **check out a feature branch**:

```shell
git checkout -b feature/<name of feature>
```

ipython-nord-theme uses [`conda`](https://conda.io/) to maintain a consistent development environment.
If you have not yet done so, please **install `conda`**; this is easiest done using the [miniconda installer](https://docs.conda.io/en/latest/miniconda.html):

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-<your os>-<your arch>.sh | bash
```

making sure to replace `os` and `arch` with values appropriate to your machine (or find a link from the miniconda website).
Ensure the `conda` executable was added to your `$PATH`.

Next, **create the development environment**:

```shell
conda env create -f envs/dev.yml
```

Once this is set up, **activate the environment**:

```shell
conda activate ipython-nord-theme-dev
```

You should now be good to go. Check this by **running the tests**:

```shell
pytest
```

With any luck, they should pass!
Go ahead and make your changes, write tests to check them, ensure your code is formatted correctly, and make a [pull request](../pulls).


## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies within all project spaces, and it also applies when
an individual is representing the project or its community in public spaces.
Examples of representing a project or community include using an official
project e-mail address, posting via an official social media account, or acting
as an appointed representative at an online or offline event. Representation of
a project may be further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
