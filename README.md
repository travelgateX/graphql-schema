# TravelgateX GraphQL schema

[![Travis](https://api.travis-ci.org/travelgateX/graphql-schema.svg?branch=master)](https://travis-ci.org/travelgateX/graphql-schema)
[![Slack](https://slack.travelgatex.com/badge.svg)](https://slack.travelgatex.com)


## Getting Started

These instructions will help you to extend and modify the current gateway schema.

### graphql-moker Instalation

```npm i graphql-mocker```

https://github.com/travelgateX/graphql-mocker

## Modify/extend your schema

1. Create an issue + branch
2. Mock your schema on graphql-faker editor: http://localhost:9003/editor
    ```sh
    yarn run mock /$HOME/projects/graphql/gateway-gql/ api-folder
    ```
    
3. Split your mocked schema
    ```sh
    yarn run split /$HOME/projects/graphql/gateway-gql/api-folder/merged_schema.graphql /$HOME/projects/graphql/gateway-gql/api-folder 
    ```

4. Check yours changes
5. Commit and Push in your branch
6. Merge Request to master, close issue and del branch


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
curl \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Apikey q8ggxpoVDW76Kw918hwnnRvxlZmAP2QZ" \
    --data '{"query":"  query IntrospectionQuery {    __schema {      queryType { name }      mutationType { name }      subscriptionType { name }      types {        ...FullType      }      directives {        name        description        locations        args {          ...InputValue        }      }    }  }  fragment FullType on __Type {    kind    name    description    fields(includeDeprecated: true) {      name      description      args {        ...InputValue      }     type {        ...TypeRef      }      isDeprecated      deprecationReason    }    inputFields {      ...InputValue    }    interfaces {      ...TypeRef    }    enumValues(includeDeprecated: true) {      name      description      isDeprecated      deprecationReason    }    possibleTypes {      ...TypeRef    }  }  fragment InputValue on __InputValue {    name    description    type { ...TypeRef }    defaultValue  }  fragment TypeRef on __Type {    kind    name    ofType {      kind      name      ofType {        kind        name        ofType {          kind          name          ofType {            kind            name            ofType {              kind              name              ofType {                kind                name                ofType {                  kind                  name                }              }            }          }        }      }    }  }"}' \
    http://api.travelgatex.com
```
