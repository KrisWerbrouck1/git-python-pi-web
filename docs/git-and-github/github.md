# GitHub 

[GitHub](github.com) is a web-based hosting service for code. It is built upon Git and provides project management features, such as bug tracking, feature requests, task management, etc. GitHub is the largest host of source code in the world and hosts the largest open source community. It provides both public open source and private repositories. 

## Sign up 

Register your free account at https://github.com/

## Create a new repository

Once logged in, create a new repository. It's a good practice to create a new repository for each project.

Choose: 
* A repository name
* To make it public or private

Repository initialization depends on whether you start from GitHub or from a local Git repository.

* Starting from GitHub
    1. Check "initialize this repository with a README"
    2. Optionally choose a preconfigured gitignore file
    3. Optionally choose an open source license
    4. Clone the repository to desktop

* Starting from a local repository
    1. Do not check "initialize this repository with a README"
    2. In your local git repository
        ```
        > git remote add origin git@github.com:yourusername/repositoryname.git
        > git push origin master
        ```

## Repository overview

GitHub provides visuals of the Git repository
* View commits history with contributor, diff and hash
* View remote branches
* View releases (git tags)

## Forking and pull request

GitHub provides user authorization for each GitHub repository. Only team members can commit to the repository. However, by means of a pull request GitHub provides the possibility for someone who isn't a team member to contribute. The workflow for a pull request is:

1. In GitHub: fork the repository. This creates a clone of the repository in your account. In this repository you can do what you want, as it is your own repository.
2. Clone the forked repository to your local machine.
2. Create a feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push the branch to your GitHub repository (`git push origin feature/fooBar`)
5. Create a new Pull Request in the original repository on GitHub

Note: many projects have their own procedure how to contribute. This procedure is usually found in the project documentation. When this procedure is not provided, it might be a good idea to open an issue to explain the purpose of your pull request.

## GitHub Education

GitHub has an [education program](https://education.github.com/). Part of this education program is [GitHub Classroom](https://classroom.github.com/). With GitHub Classroom it is possible to manage classroom assignments. An assignment starts from a repository the teacher provides. Each student clones this repository and adds a solution. All solutions are easily aggregated with Classroom Assistant.