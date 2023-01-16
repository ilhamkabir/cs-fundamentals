# Gang of 4 Design Patterns

Design Patterns are model solutions to common design problems. They are tools that can make our code more readable, easier to understand, and easier to test--provided we remember 2 things:

    1.	Just like any tool, Design Patterns should be used sparingly.

        Footnote: We don't go into every hardware problem inclined to use a tool. We shouldn't go into every software problem inclined to use a design pattern. 

    2.	Just like the 30 most common screw drivers won't fit every screw head, the 30 most common Design Patterns won't fit every design problem. Sometimes, a design problem will demand it's own unique design solution. 

## 3 common types of Design Patterns

1. Creational Design Patterns: Provides or modifies the interface for creating objects.

2. Structural Design Patterns: Defines how different classes combine to form larger structures. 

3. Behavioral Design Patterns: Assigns responsibilities to individual classes so that each class/object can interact with other classes/objects in a larger system.  

### 1\. Creational Design Patterns

Creational Patterns provide or modify the interface for creating objects.

#### 6 Common Creational Design Patterns

1. [Builder](/design_patterns/creational/builder)
```
The Builder Pattern seperates an object's initialization from its construction and then decomposes its initialization into lots of smaller operations that can be called on independent of one another. 

This pattern requires 3 classes:
1. Product Class: The end goal is to have instances of this object. 
2. Builder Class: Has functions to add parts of to the Product object.
3. Director Class: Constructs/retrieves an unique representation of Product.

Benefits:
1. Usually fewer initialization parameters. 

2. Only run the initialization operations you need.

3. The same creation can have more representations.
```

2. [Factory Pattern](/design_patterns/creational/factory.py)
```
Alternative name: Virtual Constructor Pattern

A "Factory Object" is an object that creates other objects.

The Factory Pattern creates a specific representation of ONE class. So classes are usually really simple since it only has one factory method.
```

3. [Abstract Factory](/design_patterns/creational/abstract_factory.py)
```
The Factory Pattern on steroids.

Where the Factory Pattern can create a new representation of ONE class, The Abstract Factory Pattern can create representations of several classes (so it'll have several factory methods).
```

4. [Prototype](/design_patterns/creational/prototype.py)
```
A fully initialized instance to be coppied or cloned.
```

5. [Singleton](/design_patterns/creational/singleton.py)
```
A class of which only a single instance can exist.
```

6. [Object Pool](/design_patterns/creational/object_pool.py)
```
Provides a mechanism to reuse/reshare objects

This pattern requires 2 classes:
1. ObjectPool Class: The store for all the objects
2. Client Class: Instances of the Client Class will use the object in the Object Pool. 
```

### 2\. Structural Design Patterns

Structural Patterns define how different classes combine to form larger structures. 

#### 8 Common Behavioral Structural Patterns

1. [Adapter](/design_patterns/structural/adapter.py)
```
Alternative name: Wrapper Patern

Provides a common interface to interact with different classes.

Benefit:
- Makes it easier to comply with the Liskov Substitution Principal!
```

2. [Bridge](/design_patterns/structural/bridge.py)
```
Alternative name: "Handle Pattern" or "Body Pattern"

Decouple implmentation details from abstractions.

Benefit:
- Don't need conditionals to find out what implementation you're looking for.
```

3. Composite
(no example)
```
Compose objects into a tree structure represented by part-whole hierarchies.
```

4. [Decorator](/design_patterns/structural/decorator.py)
```
Alternative name: Wrapper Pattern

Dynamically add responsabilities to objects at runtime (instead of compile time). 

Benefits:
- Saves unecessary operations at compile time. 
- Allows objects to dynamically adjust their representations at runtime. 
```

5. [Facade](/design_patterns/structural/facade.py)
```
A single class that represents an entire subsystems.

Basically just an interface that delegates client requests to the appropriate subsystem. 
```

6. [Flyweight](/design_patterns/structural/flyweight.py)
```
Lets you fit more objects into available RAM by sharing intrinsic members of the objects.
```

7. [Private Class Data](/design_patterns/structural/private_class_data.py)
```
Encapsulate private data in a seperate class and then create a proxy class with controlled access to it.
```

8. Proxy
(no example)
```
An intermediary object to another object

4 types of proxy classes:
1. Remote Proxy: A local represntation of a remote object.
2. Vritual Proxy: Creates expensive objects on demand (lazy evaluation)
3. Protection Proxy: Controlls access to another object.
4. Smart Reference Proxy: Performs additional actions when an object is accessed.
```

### 3\. Behavioral Design Patterns 

Behavioral Design Patterns assign responsibilities to individual classes so that each class/object can interact with other classes/objects in a larger system.

#### 12 Common Behavioral Design Patterns

1. [Chain of Responsability](/design_patterns/behavioral/chain_of_responsability.py)
```
A chain of responsabilities (or a "list of responsabilities")

An organized way of handling reuqests that need to be performed in a specific order.
```

2. [Command](/design_patterns/behavioral/command.py)
```
Alternative names: Action Pattern or Transaction Pattern

Encapsulate commands/requests in an "execute" and "undo" method.
```

3. Iterator
(no example)
```
Provides sequential access to elements in a collection.
```

4. Interpreter
(no example)
```
Provides consistent language elements.

- Backus Normal Form (BNF): Provides an Abstract Syntax Tree (AST) so that Domain Specific Language (DSL; for example: SQL, CSS, HTML, JSON, PHP) have similar language elements.
- 
```

5. [Mediator](/design_patterns/behavioral/mediator.py)
```
A mediator provides an interface to communicate between multiple concrete classes.

A manager is a mediator for his/her employees. Tasks are given to managers for them to delegate to their employees. 

Not a fan b/c mediator classes usually turn into monoliths!
```

6. [Memento](/design_patterns/behavioral/memento.py)
```
Used to capture and restore a snapshot of an object's state.

(Basically just storing a pickled object)

Handy for games where you don't want to start from level 0 if your computer crashes. 
```

7. [Null Object](/design_patterns/behavioral/null_object.py)
```
Alternative name: Mini pattern

Provides a default value for an object.
```

8. [Observer](/design_patterns/behavioral/observer.py)
```
Alternative Names: Dependents Pattern or Publisher-Subscriber Pattern

"Subject" notifies changes to several "observers".
```

9. [Strategy](/design_patterns/behavioral/strategy.py)
```
Alternative name: Policy Pattern

Provide the operator an encapsulated algorithm to run.
```

10. [State](/design_patterns/behavioral/state.py)
```
Alter's an object's functionality depending on the state that it's in.
```

11. [Template](/design_patterns/behavioral/template.py)
```
Include the steps of an algorithm in the abstract/interface class.

(The abstract class needs at least one non-abstract method)

```

12. [Visitor Method](/design_patterns/behavioral/visitor.py)
```
Extend the functionality of a class by encapsulating it in a "visitor" class.

(Pass the "Visitor" in, which contains the new/specific functionality)

In Python, decorators can replace visitors!
```
