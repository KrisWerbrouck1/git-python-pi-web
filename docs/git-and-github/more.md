# GitHub: more than Version Control

GitHub is not only used as a version control system, but also contains project management as well documentation and integration with other tools. 

## Documentation with Markdown

Markdown is a basic markup language, which is typically translated to HTML. It is extensively used in GitHub projects to provide documentation. For instance, if a README.MD file is provided, the HTML output will be featured on the GitHub repository web page. 

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides an overview/ 

## Deploy websites with GitHub Pages or Netlify

A GitHub repository can be used to host a website, for instance containing project documentation or a course on GitHub. The site contents are typically provided in markdown and together with other assets, such as Cascading Style Sheets (CSS), images, etc. stored in a repository. After a git push, a deploy script is triggered which generates the HTML and deploys it in on a webserver. [GitHub Pages](https://help.github.com/en/articles/what-is-github-pages) offers a static site generator, based on [Jekyll](https://jekyllrb.com/). [Netlify](https://www.netlify.com/) provides more configuration possiblities.

For example this site is hosted on [GitHub](https://github.com/VIVES-Elektronica-ICT-Brugge/git-python-pi-web), deployed and hosted with Netlify. Upon pushing to the repository on GitHub, Netlify is triggered to start a [VuePress](https://v0.vuepress.vuejs.org/) build. Half a minute later, the changes are already deployed on the website. 

## More on Git & GitHub

* [Interactive visual presentation of commits, branches and merges](http://git-school.github.io/visualizing-git/)
* [PoshGit: Enhance Powershell with Git](https://github.com/dahlbyk/posh-git)
* [Pro Git by Scott Chacon and Ben Straub](https://git-scm.com/book/en/v2)