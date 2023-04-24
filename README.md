# Bearcat Trust Bank - Extra Credit Assignment (25 pts)

Before you begin, read these instructions in full.  I will be in the classroom on Tuesday from 2:15 - 4:15pm.  If you get stuck, as for help.

## Instructions

1. Create a GitHub repo from the bearcat_trust_bank repository template
    * Browse to the [EECE3093C/bearcat_trust_bank template](https://github.com/EECE3093C/bearcat_trust_bank) repository
    * Select **Use this template**, followed by **Create new repository**
    * On the **Create a new repository** page:
        * Change the **Owner** to `EECE3093C`
        * Change the **Repository name** to `{lastname}_{firstname}_bearcat_trust_bank`

2. Create a GitHub project for the Bearcat Trust Bank project
    * The project must be located in the [EECE3093C organization](https://github.com/EECE3093C)
    * The project must be named `{lastname}_{firstname}_bearcat_trust_bank`
    * When the **Select a template** dialog appears, select the **Feature template** listed under **Project templates**

3. In your GitHub Project, create the following 8 issues.  It is recommended that you work on the issues in the order they are listed.

    <br/>
    
    > **Note**
    > Complete instructions on all of the following issues can be found in the [instructions](/instructions/.) folder.
    <br/>
    
    * Add `init` method to the `Account` class.
    * Add `deposit` method to the `Account` class.
    * Add `withdraw` method to the `Account` class.
    * Add `init` method to the `SavingsAccount` class.
    * Add `init` method to the `CheckingAccount` class.
    * Fix the GitHub Actions workflow (`.github\workflows\run_tests.yml`) to run the defined test (`tests\test_bank.py`, `tests\test_account.py`).   
    * Create a UML class diagram showing the relationships between `Bank` and `Account` classes
    * Create a UML sequence diagram for the interaction between a user and the bank system.
    <br/>
    <br/>

    > **Warning**
    > Issues must be clear, concise, and actionable.  This means all of the relevant information you can think of must be included when creating the issue, it needs to be complete enough that someone else can take over the task without additional information.

<br/>

## Additional Requirements

1. All issues must be linked to the GitHub repository, be assigned (to yourself), have appropriate label(s), belong to an iteration (sprint).
2. All added Python code must follow [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)

Applying the single responsibility principle ...

3. You must use an issue branching strategy (one branch for each issue). See [Creating a branch for an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-a-branch-for-an-issue#creating-a-branch-for-an-issue)
4. A pull request (PR) must only contain code changes for a single issue.
5. Each pull request (PR) must be linked to an issue.  See [Linking a pull request to an issue using a keyword](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
