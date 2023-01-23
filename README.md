# TravelgateX GraphQL schema

[![Travis](https://api.travis-ci.org/travelgateX/graphql-schema.svg?branch=master)](https://travis-ci.org/travelgateX/graphql-schema)
[![Slack](https://slack.travelgatex.com/badge.svg)](https://slack.travelgatex.com)

### Schema Graph

https://api.travelgatex.com/voyager

### Get gateway schema Introspection

```sh
curl \
    -X POST \
    -H "Content-Type: application/json" \
    --data '{"query":"  query IntrospectionQuery {    __schema {      queryType { name }      mutationType { name }      subscriptionType { name }      types {        ...FullType      }      directives {        name        description        locations        args {          ...InputValue        }      }    }  }  fragment FullType on __Type {    kind    name    description    fields(includeDeprecated: true) {      name      description      args {        ...InputValue      }     type {        ...TypeRef      }      isDeprecated      deprecationReason    }    inputFields {      ...InputValue    }    interfaces {      ...TypeRef    }    enumValues(includeDeprecated: true) {      name      description      isDeprecated      deprecationReason    }    possibleTypes {      ...TypeRef    }  }  fragment InputValue on __InputValue {    name    description    type { ...TypeRef }    defaultValue  }  fragment TypeRef on __Type {    kind    name    ofType {      kind      name      ofType {        kind        name        ofType {          kind          name          ofType {            kind            name            ofType {              kind              name              ofType {                kind                name                ofType {                  kind                  name                }              }            }          }        }      }    }  }"}' \
    https://api.travelgatex.com
```
