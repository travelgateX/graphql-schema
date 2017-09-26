# gateway-gql

## Getting Started

These instructions will help you to extend and modify the current gateway schema.

### graphql-faker Instalation

1- yarn global add graphql-faker

github faker: https://github.com/APIs-guru/graphql-faker

## Use cases

### Modify schema

1- graphql-faker schemaMock.graphql

### Extend schema

1- graphql-faker schemaMock.graphql

Open new terminal.

2- graphql-faker -e http://localhost:9002/graphql -p 9003

## Get gateway schema Introspection

curl 
    -X POST 
    -H "Content-Type: application/json" 
    -H "Authorization: Apikey q8ggxpoVDW76Kw918hwnnRvxlZmAP2QZ" 
    --data '{"query":"  query IntrospectionQuery {    __schema {      queryType { name }      mutationType { name }      subscriptionType { name }      types {        ...FullType      }      directives {        name        description        locations        args {          ...InputValue        }      }    }  }  fragment FullType on __Type {    kind    name    description    fields(includeDeprecated: true) {      name      description      args {        ...InputValue      }     type {        ...TypeRef      }      isDeprecated      deprecationReason    }    inputFields {      ...InputValue    }    interfaces {      ...TypeRef    }    enumValues(includeDeprecated: true) {      name      description      isDeprecated      deprecationReason    }    possibleTypes {      ...TypeRef    }  }  fragment InputValue on __InputValue {    name    description    type { ...TypeRef }    defaultValue  }  fragment TypeRef on __Type {    kind    name    ofType {      kind      name      ofType {        kind        name        ofType {          kind          name          ofType {            kind            name            ofType {              kind              name              ofType {                kind                name                ofType {                  kind                  name                }              }            }          }        }      }    }  }"}' 
    http://api-dev.travelgatex.com
    
### Introspection from graphql.js
https://github.com/graphql/graphql-js/blob/master/src/utilities/introspectionQuery.js