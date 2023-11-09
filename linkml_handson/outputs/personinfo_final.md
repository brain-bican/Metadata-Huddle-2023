```mermaid
erDiagram
NamedThing {
    string id  
    string name  
}
HasAliases {
    stringList aliases  
}
Person {
    string primary_email  
    string birth_date  
    integer age_in_years  
    GenderType gender  
    stringList aliases  
    string id  
    string name  
}
Organization {
    stringList aliases  
    string id  
    string name  
}



```

