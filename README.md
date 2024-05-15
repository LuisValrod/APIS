# JSON and APIs

## JSON

### What does it stand for?

- JSON stands for "JavaScript Object Notation." 
JS: Javascript <br>
O: Object <br>
N: Notation
### What is it used for?

- JSON is commonly used for transmitting data between a server and a web application, as well as for storing 
configuration data and transmitting structured data over network connections.

### What is it written in?
- It is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse 
and generate. JSON is based on a subset of JavaScript syntax, but it is language-independent, meaning that it can be 
used with most programming languages.


### What data types can it store/use?

- JSON can represent several basic data types and data structures commonly used in programming languages. These data types include:

  - Numbers: JSON supports numeric data types, including integers and floating-point numbers. For example: 42, 3.14.

  - Strings: JSON represents text strings enclosed in double quotes ("). For example: "hello", "JSON".

  - Boolean values: JSON supports boolean values true and false.

  - Arrays: JSON arrays are ordered collections of values, separated by commas and enclosed in square brackets ([]). Arrays can contain values of any JSON data type, including other arrays (nested arrays). For example: [1, 2, 3], ["apple", "banana", "orange"].

  - Objects: JSON objects are unordered collections of key-value pairs, where keys are strings and values can be any JSON data type, including other objects (nested objects). Objects are enclosed in curly braces ({}). For example: {"name": "John", "age": 30}, {"student": true, "grades": [85, 90, 95]}.

  - Null: JSON represents null values as null.

### What is the JSON syntax for:
JSON is often used as an alternative to XML because of its simplicity and ease of use. JSON data is represented as key-value pairs and structured in a way that is similar to JavaScript objects, making it familiar to developers who are already familiar with JavaScript

- Name-value pairs: In JSON, name-value pairs are represented as a combination of a key (name) and a value, separated by a colon (:). Name-value pairs are used within objects to represent the properties or attributes of the object. For example:
```JSON
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

- Objects: JSON objects are enclosed in curly braces ({}). They consist of zero or more name-value pairs separated by commas. Each name-value pair represents a property or attribute of the object. The name (key) must be a string, and the value can be any valid JSON data type. For example:

- Separating data objects: In JSON, multiple data objects can be separated by commas. For example, an array of objects or a list of objects would have each object separated by commas. 

```JSON
[
  {"name": "John", "age": 30},
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 35}
]
```

- JSON arrays: JSON arrays are enclosed in square brackets ([]). They contain zero or more values, separated by commas. Arrays can contain values of any valid JSON data type, including objects, arrays, strings, numbers, booleans, or null values. 

```JSON
[["apple", "banana", "orange"],
[
  {"name": "John", "age": 30},
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 35}
]]
```
JSON arrays are similar to lists in Python, as they can contain an ordered collection of values, including other arrays or objects.
