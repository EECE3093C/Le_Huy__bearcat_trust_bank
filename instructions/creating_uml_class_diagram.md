# Creating a UML Class Diagram

**Objective**: Objective: Create a UML Class Diagram to visually represent the relationships and hierarchy between the `Bank`, `Account`, `SavingsAccount`, and `CheckingAccount` classes, as well as their attributes and methods. The diagram should clearly illustrate how these classes interact to model a banking system with different types of accounts, enabling easier understanding and communication of the system's design among stakeholders.

## Instructions:

1. Review your **completed code** for the `Bank`, `Account`, `SavingsAccount`, and `CheckingAccount` classes.
2. Create a UML Class Diagram using the [mermaid.js](https://mermaid-js.github.io) syntax that includes the following classes:
    * Bank
    * Account
    * SavingsAccount
    * CheckingAccount
3. Add your UML Sequence Diagram to the [uml_class_diagram.md file](/docs/uml_class_diagram.md).  
<br/>

> **Note**
> Save your Mermaid diagram inside a fenced code block with the mermaid language identifier, for example:
>
> ````
> ```mermaid
> classDiagram
>    class GameObject {
>       -String Name
>       -int PosX
>       -int PosY
>       +Despawn() void
>   }
>   class DamageableObject {
>       +int MaxHealth
>       -int Health
>       +IsDead() bool
>       +TakeDamage(int damage) void
>       +OnKilled() void
>   }
>    GameObject <|-- DamageableObject
> ```
> ````

<br/>

### Resources:
1. For help with the mermaid.js syntax for class diagrams review the [mermaid.js documentation](https://mermaid.js.org/syntax/classDiagram.html) 
2. The [Mermaid live editor](https://mermaid.live/) can be used to interactively design the UML Sequence Diagram. 
3. Review GitHub's [Creating Mermaid diagrams]([https://mermaid.live/](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams) documentation for help on including a Mermaid diagram in a Markdown file hosted on GitHub.
