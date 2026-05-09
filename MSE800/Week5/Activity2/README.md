# Explanation of Figure 6.2: Partial Use Case Context Diagram
 
## Diagram represents 
  A partial use case diagram for a NextGen retail POS(point of sale) system and this diagram illustrates actors interacting with the system and what are the specific functionalities they are performing. Note the diagram is intentionally kept partial as seen by the (`...`) at the bottom right of the system.
 
---
 
## Actors
 
There are Seven Actors (persons and external system) that are interacting with the system.
 
**Human Actors (2)**
1. **Cashier** — This actor is connected to the sales related use cases such as Process Sale, Handle Returns, Process Rental and cash in.
2. **System Administrator** — This actor is connected to the use cases of managing security and user accounts in the system.
**System Actors (5)**
3. **Sales Activity System** — This is an automated system that is related to the Analyse Activity use case.
4. **Payment Authorization Service** - This system actor is associated with NextGen to handle payment related operations for the use case Process sales and rentals.
5. **Tax Calculator** - This actor is providing tax computation services to the relevant use cases sales and rentals.
6. **Accounting System** - This actor is related to the use case of Process sale and rental from the NextGen system.
7. **HR System** - This actor is interacting with the system for cash related use case Cash In.

---
 
## Use Cases
 
The following seven use cases in this diagram:
 
1. **Process Sale** — for managing primary sale transaction functionality.
2. **Handle Returns** — for managing product returns from customers.
3. **Process Rental** — for handling rental based transactions.
4. **Cash In** — for managing cash related transactions.
5. **Analyse Activity** — mostly for viewing and reporting on sales activities.
6. **Manage Security** -  Admin use cases for maintaining system access accross the employees.
7. **Manage Users** — Admin use cases for managing users and their roles.
---
 
## Relationships
  
- The **Cashier** is connected and initiating all these operations Process Sale, Handle Returns, and Process Rental.
- The **System Administrator** is linked to Manage Security and Manage Users.
- External systems such as Tax Calculator and Accounting System are communicating with the NextGen system through dashed lines labelled as *communication*, signifying that they are providing supporting services to the use cases.
---
 
## Two Recommendations for Improvement
 
### Recommendation 1: Add `«include»` and `«extend»` Relationship Stereotypes
 
At present, all the relationship lines in the diagram are looking identical plain associations without any additional meaning. In a proper use case diagram, it is important to distinguish between different types of relationships such as
 
- **`«include»`** should be used when a use case is *always* invoking another for example, Process Sale will always be including Payment Authorization.
- **`«extend»`** should be used when a use case is *optionally* extending another — for instance, Handle Returns may be extending Process Sale only under certain conditions.
By adding these, the diagram will be convey much more meaningful information to the reader.
 
### Recommendation 2: Group External Actors into a Clearly Labelled Boundary
 
Currently in the use case diagram the human actors and system actors are scattered across the diagram without any grouping, which is less readable to distinguish between internal users and external integrations at a quick glance. It is recommended to enclose all the external system actors namely Payment Authorization Service, Tax Calculator, Accounting System, and HR System within a dedicated dashed boundary box labelled **"External Systems"**.
 

