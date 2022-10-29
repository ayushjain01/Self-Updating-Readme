# Self-Updating README

Step-by-step for creating a self-updating README file.

Have you ever wanted to update a piece of content automatically in your `README` file? If yes, then this is the simplest tutorial for building a Self-Updating README file. 

For example, consider the lines below, these lines get updated on the first day of every month. That is you’ll see a new joke here, every month. 

### Here's a Joke for you -

<pre>My wife asked me to go get 6 cans of Sprite from the grocery store.
I realized when I got home that I had picked 7 up.
</pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre></pre>
Let’s see how we can build this.

### Contents:

- [Introduction](#introduction)
- [Step-1 : Setup](#setup)
- [Setp-2 : Jokes.txt](#jokes)
- [Step-3 : README.md](#readmeheading)
- [Step-4 : update.py](#update)
- [Step-5 : flow.yml](#flow)

<h2 id = "introduction">📕 Introduction</h2>

This Repository will help you automatically update your `README` file. In this tutorial, we change the joke in the joke section of this file, at **00:00** on the **first day** of **every month**. We randomly pick a joke from the files `Jokes.txt` and replace the joke in this file with the new joke.

We will update the contents of the `README` file using `Python` and automate this task using `[GitHub Actions](https://docs.github.com/en/actions)`. Let’s get started

<h2 id = "setup">⚙ Setup</h2>

You’ll need to add the following files to your existing repository. 

- `.github/workflows/build.yaml`

- `Jokes.txt`

- `README.md`

- `update.py`


<h2 id = "jokes">😜 Jokes.txt</h2>

This is a normal text file that contains a set of two-lined jokes each separated by a new line character. 

<h2 id = "readmeheading">📘 README.md</h2>

There’s nothing extra that you need to add to your `README` file. You can start building your `README` file like how you’d normally do. 

<h2 id = "update">🐍 update.py</h2>

This file involves reading text from the existing `README` file and `jokes.txt`, storing it in a list, randomly selecting a new joke from the `jokes.txt` file, and replacing the current joke in the `README` file with this new joke. This file is quite self-explanatory and I’ve added comments everywhere making it simpler to understand what each line of code does. 

<h2 id = "flow">🔄 flow.yml</h2>

So far we have created all the required files. We have a README file and a `update.py` file which reads the contents of both the README file and the jokes.txt file and makes changes to the README file. Now the only thing left is automating this process. This is where we will be using [GitHub Actions](https://docs.github.com/en/actions).  GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository or deploy merged pull requests to production. In simpler words, GitHub Actions will help us automatically run the `update.py` file based on our schedule. 

Below I have split the sections of the yml file, making it simpler for you to understand what each section of the workflow is doing. Just a couple of things to keep in mind before we get started -

1. To enable GH Actions on your repository you first need to create a directory called `.github/workflows`
2. In the `.github/workflows` directory, create a new file with the name you want for your workflow and the extension `yml`. For example, mine is: `flow.yml`

For the sake of understanding this tutorial, it is important to have an overview of the [vocabulary](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) related to GH Actions.

Now let’s try to understand what each section of this workflow is doing.

### name

Defines the name of the workflow that will appear in the Actions tab of your GitHub repository.

### on

Specifies the event that will automatically trigger the workflow file. This example is scheduled using cron but you can use various other triggers such as push events, etc.

If you plan to schedule a workflow, I recommend [crontab.guru](http://crontab.guru) to construct your cron expressions.

### jobs

Groups together all the jobs that run in your yml workflow file. Each step is either a shell script that will be executed or an action that will be run. 

```yaml
name: checkout repo content
```

Checks out your repository, and downloads it to the runner, allowing your workflow to access the contents of this repo and run actions against your code. You must use the checkout action any time your workflow will run against the repository’s code or you are using an action defined in the repository. In this example, we are using an action (`update,py`) defined in our repository.

```yaml
name: setup python
```

Since we are required to execute the file `update,py,` we are required to install python on our runner. This job does that. You can choose either `python-version: '3.x'` which installs the latest version of python 3 available, or a specific version of python such as `python-version: '3.7.7'`. In this example, we install the latest version of python 3. 

```yaml
name: execute py script
```

Here we execute the file `update,py` allowing us to update our `README` file.

```yaml
name: commit and push
```

Once the changes are made, it is important to commit these changes and push them. This job does that. Remember to change the user.name and user.email in this section to your username and email.

With that, you have successfully created your own Self Updating README file. 

**Feel free to experiment around and come up with better versions and share them with me. Contributions are welcomed.**
