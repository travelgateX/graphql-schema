# gateway-gql

## Getting Started

These instructions will help you to extend and modify the current gateway schema.

### graphql-faker Instalation
```sh
yarn global add graphql-faker
```
github faker: https://github.com/APIs-guru/graphql-faker

## Use cases

### Modify schema
```sh
graphql-faker schemaMock.graphql
```
### Extend schema
```sh
graphql-faker schemaMock.graphql
```
Open new terminal.
```sh
graphql-faker -e http://localhost:9002/graphql -p 9003
```
## Introspection Query

Graphql.js (Facebook): https://github.com/graphql/graphql-js/blob/master/src/utilities/introspectionQuery.js

```sh
query IntrospectionQuery {
    __schema {
      queryType { name }
      mutationType { name }
      subscriptionType { name }
      types {
        ...FullType
      }
      directives {
        name
        description
        locations
        args {
          ...InputValue
        }
      }
    }
  }
  fragment FullType on __Type {
    kind
    name
    description
    fields(includeDeprecated: true) {
      name
      description
      args {
        ...InputValue
      }
      type {
        ...TypeRef
      }
      isDeprecated
      deprecationReason
    }
    inputFields {
      ...InputValue
    }
    interfaces {
      ...TypeRef
    }
    enumValues(includeDeprecated: true) {
      name
      description
      isDeprecated
      deprecationReason
    }
    possibleTypes {
      ...TypeRef
    }
  }
  fragment InputValue on __InputValue {
    name
    description
    type { ...TypeRef }
    defaultValue
  }
  fragment TypeRef on __Type {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                }
              }
            }
          }
        }
      }
    }
  }
https://apis.guru/graphql-voyager/
```

### Graph Viewer
```
https://apis.guru/graphql-voyager/

Process

1 - Copy introspection query into GraphQL-Faker and execute query
2 - Go to graph-voyager and paste the response into Custom Schema and press "Change Schema"

```


### Get gateway schema Introspection
```sh
curl 
    -X POST 
    -H "Content-Type: application/json" 
    -H "Authorization: Apikey q8ggxpoVDW76Kw918hwnnRvxlZmAP2QZ" 
    --data '{"query":"  query IntrospectionQuery {    __schema {      queryType { name }      mutationType { name }      subscriptionType { name }      types {        ...FullType      }      directives {        name        description        locations        args {          ...InputValue        }      }    }  }  fragment FullType on __Type {    kind    name    description    fields(includeDeprecated: true) {      name      description      args {        ...InputValue      }     type {        ...TypeRef      }      isDeprecated      deprecationReason    }    inputFields {      ...InputValue    }    interfaces {      ...TypeRef    }    enumValues(includeDeprecated: true) {      name      description      isDeprecated      deprecationReason    }    possibleTypes {      ...TypeRef    }  }  fragment InputValue on __InputValue {    name    description    type { ...TypeRef }    defaultValue  }  fragment TypeRef on __Type {    kind    name    ofType {      kind      name      ofType {        kind        name        ofType {          kind          name          ofType {            kind            name            ofType {              kind              name              ofType {                kind                name                ofType {                  kind                  name                }              }            }          }        }      }    }  }"}' 
    http://api-dev.travelgatex.com
```