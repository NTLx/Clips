---
title: "Using Git with coding agents - Agentic Engineering Patterns"
source: "https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/"
author:
  - "[[Simon Willison]]"
published:
created: 2026-04-10
description: "Using Git with coding agents - Agentic Engineering Patterns"
tags:
  - "clippings"
---
## Using Git with coding agents

Git is a key tool for working with coding agents. Keeping code in version control lets us record how that code changes over time and investigate and reverse any mistakes. All of the coding agents are fluent in using Git's features, both basic and advanced.

This fluency means we can be more ambitious about how we use Git ourselves. We don't need to memorize *how* to do things with Git, but staying aware of what's possible means we can take advantage of the full suite of Git's abilities.

## Git essentials

Each Git project lives in a **repository** - a folder on disk that can track changes made to the files within it. Those changes are recorded in **commits** - timestamped bundles of changes to one or more files accompanied by a **commit message** describing those changes and an **author** recording who made them.

Git supports **branches**, which allow you to construct and experiment with new changes independently of each other. Branches can then be **merged** back into your main branch (using various methods) once they are deemed ready.

Git repositories can be **cloned** onto a new machine, and that clone includes both the current files and the full history of changes to them. This means developers - or coding agents - can browse and explore that history without any extra network traffic, making history diving effectively free.

Git repositories can live just on your own machine, but Git is designed to support collaboration and backups by publishing them to a **remote**, which can be public or private. GitHub is the most popular place for these remotes but Git is open source software that enables hosting these remotes on any machine or service that supports the Git protocol.

## Core concepts and prompts

Coding agents all have a deep understanding of Git jargon. The following prompts should work with any of them:

Start a new Git repo here

To turn the folder the agent is working in into a Git repository - the agent will probably run the `git init` command. If you just say "repo" agents will assume you mean a Git repository.

Commit these changes

Create a new Git commit to record the changes the agent has made - usually with the `git commit -m "commit message"` command.

Add username/repo as a github remote

This should configure your repository for GitHub. You'll need to create a new repo first using [github.com/new](https://github.com/new), and configure your machine to talk to GitHub.

Review changes made today

Or "recent changes" or "last three commits".

This is a great way to start a fresh coding agents session. Telling the agent to look at recent changes causes it to run `git log`, which can instantly load its context with details of what you have been working on recently - both the modified code and the commit messages that describe it.

Seeding the session in this way means you can start talking about that code - suggest additional fixes, ask questions about how it works, or propose the next change that builds on what came before.

Integrate latest changes from main

Run this on your main branch to fetch other contributions from the remote repository, or run it in a branch to integrate the latest changes on main.

There are multiple ways to merge changes, including merge, rebase, squash or fast-forward. If you can't remember the details of these that's fine:

Discuss options for integrating changes from main

Agents are great at explaining the pros and cons of different merging strategies, and everything in git can always be undone so there's minimal risk in trying new things.

Sort out this git mess for me

I use this universal prompt surprisingly often! Here's [a recent example](https://gisthost.github.io/?2aa2ee2fbd08d272528bbfc3b54a1a7d/page-001.html) where it fixed a cherry-pick for me that failed with a merge conflict.

There are plenty of ways you can get into a mess with Git, often through pulls or rebase commands that end in a merge conflict, or just through adding the wrong things to Git's staging environment.

Unpicking those used to be the most difficult and time consuming parts of working with Git. No more! Coding agents can navigate the most Byzantine of merge conflicts, reasoning through the intent of the new code and figuring out what to keep and how to combine conflicting changes. If your code has automated tests (and [it should](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)) the agent can ensure those pass before finalizing that merge.

Find and recover my code that does...

If you lose code that you are working on that's previously been committed (or saved with `git stash`) your agent can probably find it for you.

Git has a mechanism called the `reflog` which can often capture details of code that hasn't been committed to a permanent branch. Agents can search that, and search other branches too.

Just tell them what to find and watch them dive in.

Use git bisect to find when this bug was introduced:...

Git bisect is one of the most powerful debugging tools in Git's arsenal, but it has a relatively steep learning curve that often deters developers from using it.

When you run a bisect operation you provide Git with some kind of test condition and a start and ending commit range. Git then runs a binary search to identify the earliest commit for which your test condition fails.

This can efficiently answer the question "what first caused this bug". The only downside is the need to express the test for the bug in a format that Git bisect can execute.

Coding agents can handle this boilerplate for you. This upgrades Git bisect from an occasional use tool to one you can deploy any time you are curious about the historic behavior of your software.

## Rewriting history

Let's get into the fun advanced stuff.

The commit history of a Git repository is not fixed. The data is just files on disk after all (tucked away in a hidden `.git/` directory), and Git itself provides tools that can be used to modify that history.

Don't think of the Git history as a permanent record of what actually happened - instead consider it to be a deliberately authored story that describes the progression of the software project.

This story is a tool to aid future development. Permanently recording mistakes and cancelled directions can sometimes be useful, but repository authors can make editorial decisions about what to keep and how best to capture that history.

Coding agents are really good at using Git's advanced history rewriting features.

### Undo or rewrite commits

Undo last commit

It's common to commit code and then regret it - realize that it includes a file you didn't mean to include, for example. The git recipe for this is `git reset --soft HEAD~1`. I've never been able to remember that, and now I don't have to!

Remove uv.lock from that last commit

You can also perform more finely grained surgery on commits - rewriting them to remove just a single file, for example.

Combine last three commits with a better commit message

Agents can rewrite commit messages and can combine multiple commits into a single unit.

I've found that frontier models usually have really good taste in commit messages. I used to insist on writing these myself but I've accepted that the quality they produce is generally good enough, and often even better than what I would have produced myself.

### Building a new repository from scraps of an older one

A trick I find myself using quite often is extracting out code from a larger repository into a new one while maintaining the key history of that code.

One common example is library extraction. I may have built some classes and functions into a project and later realized they would make more sense as a standalone reusable code library.

Start a new repo at /tmp/distance-functions and build a Python library there with the lib/distance\_functions.py module from here - build a similar commit history copying the author and commit dates in the new repo

This kind of operation used to be involved enough that most developers would create a fresh copy detached from that old commit history. We don't have to settle for that any more!

← [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)

[Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/) →

**Chapters in this guide**

1. **Principles**
	1. [What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
		2. [Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)
		3. [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)
		4. [AI should help us produce better code](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/)
		5. [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
2. **Working with coding agents**
	1. [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)
		2. **Using Git with coding agents**
		3. [Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)
3. **Testing and QA**
	1. [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
		2. [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)
		3. [Agentic manual testing](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)
4. **Understanding code**
	1. [Linear walkthroughs](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)
		2. [Interactive explanations](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/)
5. **Annotated prompts**
	1. [GIF optimization tool using WebAssembly and Gifsicle](https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/)
6. **Appendix**
	1. [Prompts I use](https://simonwillison.net/guides/agentic-engineering-patterns/prompts/)

Created: 21st March 2026  
Last modified: 23rd March 2026  
[5 changes](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/changes/)

**Previous:** [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)

**Next:** [Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)